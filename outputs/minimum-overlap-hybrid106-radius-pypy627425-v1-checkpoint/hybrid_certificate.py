"""Continuous Arb verification of periodic/Fourier/Gram-functional duals."""
import argparse,hashlib,json,time
from fractions import Fraction as F
from pathlib import Path
from circle_certificate import arb,ctx,offsets,family_coefficients,q_jet,fourth_derivative_bound,reference
from hybrid_functionals import validate,knots,affine

def A(value):
    value=F(value);return arb(value.numerator)/value.denominator

def pieces(data,functions):
    base=dict(data,schema=data['base_schema']);n=base['cells']
    if type(n)!=int or n<2 or n&(n-1):raise ValueError('power-of-two base cells')
    steps=offsets(base);h=F(2,n);boundaries=knots(functions)
    boundaries.update(h*i for i in range(1,n) if steps[i]!=steps[i-1])
    boundaries=sorted(boundaries);out=[]
    for left,right in zip(boundaries,boundaries[1:]):
        center=(left+right)/2;u,v=affine(functions,center)
        out.append((left,right,steps[int(center//h)]+u,v))
    return out

def verify(data,mean,width,order):
    functions,premises=validate(data,mean);parts=pieces(data,functions)
    y0,y2=A(data['y0']),A(data['y2']);terms=[]
    if F(data['y2']):
        negative=F(data['y2'])<0
        terms.append(reference.Term('t2' if negative else '-t2',None,-y2 if negative else y2,arb(0)))
    L0=y0+y2*A(F(2,3));mean_coefficient=F(data['y2'])/2
    for family in data['families']:
        _,bound=family_coefficients(family);L0+=bound*sum((A(v) for v in family['z']),arb(0))
    for row in data['cos']:
        if F(row['z'])>0 or not F(row['xi']):raise ValueError('cosine row')
        z,xi=A(row['z']),A(row['xi']);terms.append(reference.Term('cos',row['xi'],-z,arb(0)))
        L0+=z*(xi.sin()/xi)**2
    for f in functions:
        L0+=A(f['mu']*f['L0']);mean_coefficient+=f['mu']*f['mean_coefficient']
    L=L0+A(min(F(0),mean_coefficient)*mean*mean)
    M4=fourth_derivative_bound(terms)
    M2=2*y2.abs_upper()+sum((t.lam.abs_upper()*t.xi.abs_upper()**2 for t in terms if t.kind=='cos'),arb(0))
    total=arb(0);nodes=positive=negative=ambiguous=0
    for left,right,constant,slope in parts:
        shift=A(F(data['y0'])-1+constant);sl=A(slope);stack=[(left,right)]
        while stack:
            aF,bF=stack.pop();a,b=A(aF),A(bF);c,r=(a+b)/2,(b-a)/2
            q,q1,q2,q3=q_jet(terms,c);q+=shift+sl*c;q1+=sl
            radius=q1.abs_upper()*r
            if order==4:radius+=q2.abs_upper()*r*r/2+q3.abs_upper()*r**3/6+M4*r**4/24
            else:radius+=M2*r*r/2
            nodes+=1
            if nodes>10000000:raise RuntimeError('node budget')
            if q+radius<=0:negative+=1;continue
            if q-radius>=0:
                total+=(reference.Q(terms,b)-reference.Q(terms,a)+shift*(b-a)+sl*(b*b-a*a)/2).upper();positive+=1
            elif bF-aF<=width:
                total+=(b-a)*reference.pos_upper(q+radius);ambiguous+=1
            else:
                mid=(aF+bF)/2;stack.extend(((aF,mid),(mid,bF)))
    return (2*total).upper(),L,L0,mean_coefficient,{'nodes':nodes,'positive':positive,'negative':negative,
        'ambiguous':ambiguous,'pieces':len(parts),'functional_premises':premises}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('certificate',type=Path);ap.add_argument('--mean-max',default='0')
    ap.add_argument('--target',required=True);ap.add_argument('--width',default='1e-7');ap.add_argument('--order',type=int,choices=[2,4],default=4)
    ap.add_argument('--prec',type=int,default=200);ap.add_argument('--report',type=Path,required=True);args=ap.parse_args();start=time.time()
    ctx.prec=args.prec;mean,width,target=map(F,(args.mean_max,args.width,args.target))
    if width<=0 or target<=0:raise ValueError('parameters')
    data=json.loads(args.certificate.read_text(encoding='utf-8'));D,L,L0,c,info=verify(data,mean,width,args.order)
    bound=L/D;passed=bool(L>0 and D>0 and bound>A(target))
    result={'passed':passed,'scope':'central mean interval only; embedded Gram matrices replayed exactly',
        'mean_abs_max':args.mean_max,'target':args.target,'order':args.order,'width':args.width,'precision_bits':ctx.prec,
        'lower_bound_ball':bound.str(70),'numerator_ball':L.str(70),'mean0_numerator_ball':L0.str(70),
        'mean_square_coefficient_exact':str(c),'positive_integral_upper_ball':D.str(70),'elapsed':time.time()-start,
        'certificate_sha256':hashlib.sha256(args.certificate.read_bytes()).hexdigest(),
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),**info}
    result['implementation_hashes']={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
        for name in ('hybrid_functionals.py','verify_phase_gram.py','circle_certificate.py','verify_fourth_order.py')}
    args.report.write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result,indent=2),flush=True)
    if not passed:raise SystemExit(1)
if __name__=='__main__':main()
