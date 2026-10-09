"""Independent-backend upper enclosure of an even kernel's derivative energy."""
import argparse,hashlib,json,time
from fractions import Fraction as F
from pathlib import Path
R=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def polynomial_square_integral(a,b,c,h):return h*a*a+h**3*(b*b+a*c)/12+h**5*c*c/320
def controls():
    count=0
    for a,b,c,h in [(F(1),F(0),F(0),F(2)),(F(0),F(1),F(0),F(2)),(F(0),F(0),F(2),F(2)),(F(1),F(2),F(3),F(3,5))]:
        p=[a,b,c/2];square=[sum(p[i]*p[j] for i in range(3) for j in range(3) if i+j==k) for k in range(5)];r=h/2;want=sum(v*(r**(k+1)-(-r)**(k+1))/(k+1) for k,v in enumerate(square));assert polynomial_square_integral(a,b,c,h)==want;count+=1
    return {'status':'PASS','exact_polynomial_energy_fixtures':count,'scope':'Taylor polynomial square integration; analytic fourth-derivative remainder is a reviewed premise'}
def main():
    ap=argparse.ArgumentParser();ap.add_argument('seed',type=Path);ap.add_argument('--mode',choices=['arb','integer'],required=True);ap.add_argument('--width',default='1/2048');ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();start=time.time();d=json.loads(a.seed.read_text());assert F(d['theta_outer'])==0 and d['outer']['active']==[];width=F(a.width);assert width>0;checked=controls();nodes=0
    if a.mode=='arb':
        from circle_certificate import ctx,arb,reference
        from hybrid_certificate import A
        from verify_hybrid_outer_blend import compile_blend
        from verify_fourth_order import q_jet,fourth_derivative_bound
        from verify_shared_mean_return import ball_interval
        ctx.prec=240;terms,parts,premise=compile_blend(d);terms=[t for t in terms if t.lam!=0];assert all(t.kind in {'cos','-cos','t2','-t2'} for t in terms);M4=fourth_derivative_bound(terms);total=arb(0)
        def energy(left,right,slope):
            h=A(right-left);radius=h/2;_,p,q,r=q_jet(terms,A((left+right)/2));p+=A(slope);remainder=M4*radius**3/6;pm=p.abs_upper()+q.abs_upper()*radius+r.abs_upper()*radius*radius/2
            return polynomial_square_integral(p,q,r,h)+2*h*pm*remainder+h*remainder*remainder
        def accumulate(v):
            nonlocal total
            assert v.upper()>=0;total+=reference.pos_upper(v)
    else:
        from verify_integer_hybrid_outer_blend import BlendChecker
        from verify_integer_circle import I,SCALE
        checker=BlendChecker(d);assert checker.linear==0 and all(t[2].lo==t[2].hi==0 for t in checker.terms);parts=checker.parts;total=I(0)
        def energy(left,right,slope):
            h=I(right-left);radius=h/2;_,p,q,r=checker.jet((left+right)/2);p+=I(slope);remainder=checker.M4*radius*radius*radius/6;pm=I.raw(0,p.abs_upper())+I.raw(0,q.abs_upper())*radius+I.raw(0,r.abs_upper())*radius*radius/2
            # I has no exponent operator; the same polynomial is assembled
            # explicitly through independent dyadic interval operations.
            h2=h*h;h3=h2*h;h5=h3*h2;integral=h*p*p+h3*(q*q+p*r)/12+h5*r*r/320
            return integral+2*h*pm*remainder+h*remainder*remainder
        def accumulate(v):
            nonlocal total
            assert v.hi>=0;total+=I.raw(0,v.hi)
    for left,right,constant,slope in parts:
        if right<=0:continue
        assert left>=0;stack=[(left,right)]
        while stack:
            lo,hi=stack.pop()
            if hi-lo>width:mid=(lo+hi)/2;stack.extend([(lo,mid),(mid,hi)]);continue
            accumulate(energy(lo,hi,slope));nodes+=1
            if nodes%1000==0:print(json.dumps({'mode':a.mode,'energy_cells':nodes,'elapsed':time.time()-start}),flush=True)
    if a.mode=='arb':upper=ball_interval((2*total).str(70))[1]
    else:upper=F(2*total.hi,SCALE)
    assert upper>0
    modules=[Path(__file__).name,'verify_hybrid_outer_blend.py','verify_integer_hybrid_outer_blend.py','hybrid_certificate.py','hybrid_functionals.py','verify_phase_gram.py','circle_certificate.py','verify_fourth_order.py','verify_integer_hybrid.py','verify_integer_circle.py','verify_shared_mean_return.py','shared_mean_numerator.py','sources/lower-bound/certificate/prove_erdos_0380554275_arb.py']
    result={'status':'PASS','scope':'full-line derivative-energy upper enclosure of the even normalized central kernel; no mu bound by itself','mode':a.mode,'energy_upper_exact':str(upper),'energy_upper_display':float(upper),'positive_half_energy_cells':nodes,'maximum_cell_width':str(width),'controls':checked,'seed_sha256':sha(a.seed),'implementation_hashes':{n:sha(R/n) for n in modules},'elapsed':time.time()-start};a.out.write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result),flush=True)
if __name__=='__main__':main()
