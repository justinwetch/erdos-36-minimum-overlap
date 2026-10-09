"""Exact independent hat-kernel and hybrid-assembly diagnostics."""
import argparse,copy,hashlib,json,random,time
from fractions import Fraction as F
from pathlib import Path
from hybrid_functionals import validate,knots,affine
from hybrid_certificate import pieces,verify,ctx,A
from circle_certificate import verify as base_verify
from verify_integer_hypermetric import compile_families
from verify_phase_gram import compile_dual
from phase_functional_cut import hat_integral

ROOT=Path(__file__).resolve().parent
def need(ok,message):
    if not ok:raise AssertionError(message)
def direct(fs,t):
    return sum((f['mu']*sum((g*(2 if k==0 else 1)/(2*f['a'])*max(F(0),1-abs(t-k*f['a'])/f['a'])
        for k,g in enumerate(f['gamma'])),F(0)) for f in fs),F(0))
def integral(fs,l,r):
    return sum((f['mu']*sum((g*(2 if k==0 else 1)/(2*f['a'])*hat_integral(l,r,k*f['a'],f['a'])
        for k,g in enumerate(f['gamma'])),F(0)) for f in fs),F(0))
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--certificate',type=Path,default=ROOT/'certificates/hybrid6-grid-proposal.json')
    ap.add_argument('--report',type=Path,default=ROOT/'runs/hybrid-mapping-checks.json');args=ap.parse_args()
    start=time.time();checks=0;rng=random.Random(360524);ctx.prec=200
    path=args.certificate;data=json.loads(path.read_text());mean=F('.002042269461')
    fs,premises=validate(data,mean)
    fixtures=[fs]
    for N in (2,3,7,24):
        fixtures.append([{'N':N,'a':F(2,N),'gamma':[F(rng.randrange(-30,31),13) for _ in range(N+1)],'mu':F(7,11)}])
    fixtures.append(fixtures[1]+fixtures[2]+fixtures[3])
    for functions in fixtures:
        ts=sorted(knots(functions))
        for l,r in zip(ts,ts[1:]):
            u,v=affine(functions,(l+r)/2)
            for q in (F(0),F(1,7),F(1,2),F(5,7),F(1)):
                t=l+q*(r-l);need(u+v*t==direct(functions,t),'affine/direct hat mismatch');checks+=1
            need(u*(r-l)+v*(r*r-l*l)/2==integral(functions,l,r),'affine/hat integral mismatch');checks+=1
        for _ in range(80):
            l,r=sorted((F(rng.randrange(2001),1000),F(rng.randrange(2001),1000)))
            boundaries=sorted({l,r}|{t for t in ts if l<t<r});s=F(0)
            for a,b in zip(boundaries,boundaries[1:]):
                u,v=affine(functions,(a+b)/2);s+=u*(b-a)+v*(b*b-a*a)/2
            need(s==integral(functions,l,r),'cross-knot integral mismatch');checks+=1
    # Independent periodic-family compiler, evaluated on every hybrid piece.
    base=dict(data,schema=data['base_schema']);parts,B=compile_families(base);index=0
    for l,r,u,v in pieces(data,fs):
        c=(l+r)/2
        while parts[index][1]<=c:index+=1
        need(parts[index][0]<=l and r<=parts[index][1],'piece crosses step jump')
        need(u+v*c==parts[index][2]+direct(fs,c),'combined step/hat assembly');checks+=1
    # Changing the radius cannot alter PSD; preserve signed mean dependence.
    for row,f in zip(data['functional_rows'],fs):
        cert=copy.deepcopy(row['certificate']);cert['mean_abs_max']='0';G0,L0=compile_dual(cert)
        for radius in (F(0),mean,F(1,9),F(1)):
            cert['mean_abs_max']=str(radius);G,L=compile_dual(cert)
            need(G==G0 and L==L0+f['mean_coefficient']*radius**2,'mean radius recompilation');checks+=1
    # Zero-functional reduction: both engines enclose the same base function.
    zero=dict(data,functional_rows=[]);D,L,L0,c,info=verify(zero,mean,F('1e-7'),4)
    oldD,oldL,_=base_verify(base,'1e-7',4)
    oldL+=A(min(F(0),F(base['y2'])/2)*mean**2)
    need((L-oldL).contains(0),'zero-functional numerator reduction')
    need(abs(float(D-oldD))<1e-12,'zero-functional integral reduction');checks+=2
    bad=copy.deepcopy(data);bad['functional_rows'][0]['multiplier']='-1'
    try:validate(bad,mean)
    except ValueError:checks+=1
    else:raise AssertionError('negative multiplier accepted')
    out={'status':'PASS','exact_fixture_checks':checks,'scope':'kernel, primitive, independent periodic mapping, radius and zero-functional controls; analytic premises remain in proof documents',
         'certificate_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'implementation_hashes':{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in
             ('hybrid_functionals.py','hybrid_certificate.py','circle_certificate.py','verify_integer_hypermetric.py','verify_phase_gram.py','phase_functional_cut.py')},
         'elapsed':time.time()-start}
    args.report.write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
