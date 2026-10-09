"""New explicit common-bin blend checker; existing proof checkers unchanged."""
import argparse,hashlib,json,time
from pathlib import Path
from fractions import Fraction as F
from hybrid_certificate import A,pieces
from hybrid_functionals import validate
from circle_certificate import arb,ctx,family_coefficients,reference
from verify_fourth_order import q_jet,fourth_derivative_bound

ACCEPTED={'t','-t','t2','-t2','cos','-cos','sin','-sin','cos+asin'}

def scale_terms(terms,scale):
    return [reference.Term(t.kind,t.param,t.lam*scale,t.B) for t in terms]

def derivative_bounds(terms):
    M2=arb(0)
    for t in terms:
        if t.kind in {'t','-t'}:continue
        if t.kind in {'t2','-t2'}:M2+=2*t.lam.abs_upper();continue
        amplitude=(1+t.alpha*t.alpha).sqrt().abs_upper() if t.kind=='cos+asin' else arb(1)
        M2+=t.lam.abs_upper()*t.xi.abs_upper()**2*amplitude
    return M2.upper(),fourth_derivative_bound(terms)

def integrate(terms,parts,width,order,limit=2000000):
    M2,M4=derivative_bounds(terms);total=arb(0);nodes=pos=neg=amb=0
    for left,right,constant,slope in parts:
        shift=A(constant);sl=A(slope);stack=[(left,right)]
        while stack:
            aF,bF=stack.pop();a,b=A(aF),A(bF);c,r=(a+b)/2,(b-a)/2
            q,q1,q2,q3=q_jet(terms,c);q+=shift+sl*c;q1+=sl
            radius=q1.abs_upper()*r
            if order==4:radius+=q2.abs_upper()*r*r/2+q3.abs_upper()*r**3/6+M4*r**4/24
            else:radius+=M2*r*r/2
            nodes+=1
            if nodes>limit:raise RuntimeError('node budget')
            if q+radius<=0:neg+=1;continue
            if q-radius>=0:
                v=reference.Q(terms,b)-reference.Q(terms,a)+shift*(b-a)+sl*(b*b-a*a)/2
                if v.upper()<0:raise ArithmeticError('negative positive-piece integral')
                total+=reference.pos_upper(v);pos+=1
            elif bF-aF<=width:
                total+=(b-a)*reference.pos_upper(q+radius);amb+=1
            else:
                mid=(aF+bF)/2;stack.extend(((aF,mid),(mid,bF)))
    return total.upper(),{'nodes':nodes,'positive':pos,'negative':neg,'ambiguous':amb,'pieces':len(parts)}

def controls():
    errors=[]
    h=[reference.Term('cos','1.25',A('0.7'),arb(0))]
    o=[reference.Term('t',None,A('.3'),A('.1')),reference.Term('cos+asin',['.8','-.2'],A('.4'),A('.7'))]
    for theta in map(F,['0','.17','1']):
        hs=(1-theta)*F(7,5);terms=scale_terms(h,A(hs))+scale_terms(o,A(theta))
        for x in map(F,['-.9','.13','1.7']):
            hj=q_jet(h,A(x));oj=q_jet(o,A(x));j=q_jet(terms,A(x))
            shift=hs*F(2,3)+theta-1;slope=hs*F(-2,7)
            j=(j[0]+A(shift+slope*x),j[1]+A(slope),j[2],j[3])
            expected=(A(hs)*(hj[0]+A(F(2,3)-1+F(-2,7)*x))+A(theta)*oj[0],
                      A(hs)*(hj[1]+A(F(-2,7)))+A(theta)*oj[1],A(hs)*hj[2]+A(theta)*oj[2],A(hs)*hj[3]+A(theta)*oj[3])
            assert all((a-b).contains(0) for a,b in zip(j,expected));errors.append(True)
    for order in [2,4]:
        for shift,slope,expected in [(0,0,4),(-2,0,0),(-1,1,2)]:
            D,_=integrate([],[(F(-2),F(2),F(shift),F(slope))],F(1,10**8),order)
            assert D>=A(expected) and D-A(expected)<A('1e-12')
    return {'status':'PASS','merged_jet_fixtures':len(errors),'polynomial_integrals':6,
            'scope':'blend normalization and full-line affine integration; universal input inequalities are reviewed premises'}

def compile_blend(data):
    if data['schema']!='hybrid-outer-blend-v1':raise ValueError('schema')
    theta=F(data['theta_outer']);low=F(data['hybrid_numerator_lower'])
    if not 0<=theta<=1 or low<=0:raise ValueError('blend weights')
    hybrid,outer=data['hybrid'],data['outer'];lo,hi=F(outer['lo']),F(outer['hi'])
    if not -1<=lo<=hi<=1:raise ValueError('mean bin')
    mean=max(abs(lo),abs(hi));functions,premises=validate(hybrid,mean)
    terms=[];y0,y2=F(hybrid['y0']),F(hybrid['y2']);L0=A(y0+y2*F(2,3));coefficient=y2/2
    if y2:terms.append(reference.Term('t2' if y2<0 else '-t2',None,A(abs(y2)),arb(0)))
    for family in hybrid['families']:
        _,bound=family_coefficients(family);L0+=A(bound*sum(map(F,family['z'])))
    for row in hybrid['cos']:
        z,xi=F(row['z']),F(row['xi'])
        if z>0 or not xi:raise ValueError('cosine row')
        terms.append(reference.Term('cos',row['xi'],A(-z),arb(0)));L0+=A(z)*(A(xi).sin()/A(xi))**2
    for f in functions:L0+=A(f['mu']*f['L0']);coefficient+=f['mu']*f['mean_coefficient']
    numerator=L0+A(min(F(0),coefficient)*mean**2)
    if not numerator>=A(low):raise ValueError('unproved hybrid numerator lower')
    for row in outer['active']:
        if row['kind'] not in ACCEPTED or F(row['lambda'])<0:raise ValueError('outer row')
        if row['kind'] in {'cos','-cos','sin','-sin'} and not F(row['param']):raise ValueError('zero frequency')
        if row['kind']=='cos+asin' and not F(row['param'][0]):raise ValueError('zero frequency')
    outerterms,_,_,_=reference.prepare_bin(outer,arb(0))
    hs=(1-theta)/low;combined=scale_terms(terms,A(hs))+scale_terms(outerterms,A(theta));parts=[]
    for a,b,constant,slope in pieces(hybrid,functions):
        shift=hs*(y0+constant)+theta-1;sl=hs*slope
        parts.extend([(a,b,shift,sl),(-b,-a,shift,-sl)])
    parts.sort()
    assert parts[0][0]==-2 and parts[-1][1]==2 and all(a[1]==b[0] for a,b in zip(parts,parts[1:]))
    return combined,parts,{'mean_bin':[str(lo),str(hi)],'hybrid_numerator_ball':numerator.str(70),
                           'hybrid_numerator_lower_exact':str(low),'mean_square_coefficient_exact':str(coefficient),'functional_premises':premises}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('certificate',type=Path);ap.add_argument('--target',required=True)
    ap.add_argument('--width',default='1e-7');ap.add_argument('--order',type=int,choices=[2,4],default=4)
    ap.add_argument('--out',type=Path,required=True);args=ap.parse_args();start=time.time();ctx.prec=200
    target,width=F(args.target),F(args.width)
    if target<=0 or width<=0:raise ValueError('parameters')
    checked=controls();data=json.loads(args.certificate.read_text());terms,parts,premises=compile_blend(data)
    D,info=integrate(terms,parts,width,args.order);passed=bool(D>0 and 1/D>A(target))
    result={'passed':passed,'scope':'single mean bin only; new blend grammar with complete continuous outward integration',
            'target':args.target,'positive_integral_upper_ball':D.str(70),'lower_bound_ball':(1/D).str(70),
            'order':args.order,'width':args.width,'controls':checked,'premises':premises,**info,'elapsed':time.time()-start,
            'certificate_sha256':hashlib.sha256(args.certificate.read_bytes()).hexdigest(),
            'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    result['implementation_hashes']={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
        for name in ['hybrid_certificate.py','hybrid_functionals.py','verify_phase_gram.py','circle_certificate.py','verify_fourth_order.py']}
    result['reference_sha256']=hashlib.sha256(Path(reference.__file__).read_bytes()).hexdigest()
    args.out.write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result),flush=True)
    if not passed:raise SystemExit(1)

if __name__=='__main__':main()
