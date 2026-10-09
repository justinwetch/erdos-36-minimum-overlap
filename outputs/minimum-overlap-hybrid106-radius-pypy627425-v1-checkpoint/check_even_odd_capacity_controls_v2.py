"""Exact controls for the physical capacity return; no LP solver required."""
import argparse,hashlib,json,random,subprocess,sys,tempfile
from fractions import Fraction as F
from pathlib import Path
from verify_even_odd_capacity import sqrt_upper
from integer_block_primitive import controls as block_controls
R=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def controls():
    # Sharp covariance fixture f'=t(h-t), g=t; integrate polynomials exactly.
    covariance=[]
    for h in [F(1),F(2,3),F(1,16384)]:
        f=[F(0),F(0),h/2,F(-1,3)];g=[0,1]
        integral=lambda p:sum((F(c)*h**(i+1)/(i+1) for i,c in enumerate(p)),F(0))
        fg=[F(0)]*(len(f)+1)
        for i,c in enumerate(f):fg[i+1]=c
        cov=integral(fg)-integral(f)*integral(g)/h
        energy=integral([0,0,h*h,-2*h,1])
        assert cov==h**5/60 and energy==h**5/30 and cov*cov==h**5*energy/120
        covariance.append(str(h))
    block=block_controls();assert block['status']=='PASS'
    rng=random.Random(360700);flows=0
    for case in range(160):
        n=3+case%13;weights=[F(rng.randrange(1,10)) for _ in range(n)];h=[x/sum(weights) for x in weights]
        # A piecewise constant slope in [-1,1] gives exact admissible averages.
        slopes=[F(rng.randrange(-7,8),7) for _ in range(n)];z=[];d=F(0)
        for hi,s in zip(h,slopes):z.append(d+s*hi/2);d+=s*hi
        M=max([abs(x) for x in z]+[F(1,3)]);assert abs(z[0])<=h[0]/2
        assert all(abs(z[i+1]-z[i])<=(h[i]+h[i+1])/2 for i in range(n-1))
        C=[F(rng.randrange(0,100),31) for _ in h];k=[F(rng.randrange(-10,11),10) for _ in h];v=[F(rng.randrange(-50,51),19) for _ in range(n-1)];tau=F(rng.randrange(-20,21),23);kap=F(rng.randrange(-20,21),29)
        div=[-v[0]]+[a-b for a,b in zip(v,v[1:])]+[v[-1]]
        residual=[-ki*ci-2*tau*hi-di-(kap if i==0 else 0) for i,(ki,ci,hi,di) in enumerate(zip(k,C,h,div))]
        m=2*sum((hi*zi for hi,zi in zip(h,z)),F(0));T=sum((abs(v[i])*(h[i]+h[i+1])/2 for i in range(n-1)),F(0))+abs(kap)*h[0]/2
        lhs=-sum((ci*abs(zi) for ci,zi in zip(C,z)),F(0));linear=-sum((ki*ci*zi for ki,ci,zi in zip(k,C,z)),F(0))
        identity=tau*m+sum((v[i]*(z[i+1]-z[i]) for i in range(n-1)),F(0))+kap*z[0]+sum((ri*zi for ri,zi in zip(residual,z)),F(0))
        assert linear==identity and lhs<=linear<=tau*m+T+M*sum(map(abs,residual));flows+=1
    for q in [F(0),F(1),F(2,3),F(10000,7)]:
        u=sqrt_upper(q);assert u*u>=q and (u==0 or (u-F(1,10**30))**2<q)
    return {'status':'PASS','sharp_covariance_fixtures':covariance,'block_primitive_controls':block,'exact_flow_fixtures':flows,'outward_sqrt_fixtures':4,'scope':'exact algebra and covariance sharp examples; the analytic Lipschitz and continuum-return lemmas remain documented proof premises'}
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',required=True,type=Path);a=ap.parse_args();r=controls();r['implementation_hashes']={n:sha(R/n) for n in ['check_even_odd_capacity_controls_v2.py','verify_even_odd_capacity.py','verify_even_odd_capacity_v2.py','integer_block_primitive.py']};a.out.write_text(json.dumps(r,indent=2),encoding='utf-8');print(json.dumps(r))
if __name__=='__main__':main()
