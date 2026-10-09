"""Exact quartet identities and independently solved constant-cost fixtures."""
import argparse,hashlib,json
from fractions import Fraction as F
from pathlib import Path
import numpy as np
from probe_odd_lipschitz_capacity import capacity
R=Path(__file__).resolve().parent
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();count=0;M=F(3,5)
    for A in map(F,[-2,0,3]):
        for B in map(F,[-1,0,2]):
            for s in map(F,[-3,0,4]):
                for d in [-M,F(0),M/3,M]:
                    e=[abs(d),2*M-abs(d)];got=max(A*x+B*y+s*d for x in e for y in e);want=2*M*(max(A,0)+max(B,0))-(abs(A)+abs(B))*abs(d)+s*d;assert got==want;count+=1
    densities=0
    for h in [[F(1,5),F(3,5),F(4,5),F(2,5)],[F(1,2)]*4,list(map(F,[0,0,1,1])),list(map(F,[1,0,0,1]))]:
        assert sum(h)/2==1
        def H(t):return sum(v*max(F(0),min(F(1,2),t-F(i,2))) for i,v in enumerate(h))
        d=lambda t:H(t)+H(2-t)-1
        area=sum((d(F(i,2))+d(F(i+1,2)))/4 for i in range(2));hx=sum(v*(F(i+1,2)**2-F(i,2)**2)/2 for i,v in enumerate(h));m=2-2*hx
        assert 2*area==m and d(0)==0 and all(abs(d(F(i+1,2))-d(F(i,2)))<=F(1,2) for i in range(2));densities+=1
    lp=[]
    for A,B,s in [(1,1,0),(-1,-1,0),(1,-1,0),(1,1,3)]:
        for lip in [False,True]:
            r=capacity(np.full(8,A),np.full(8,B),np.full(8,s),.3,.1,lip);want=.6*(max(A,0)+max(B,0))-.05*(abs(A)+abs(B))+.05*s;assert abs(r['capacity_midpoint_model']-want)<1e-10 and r['maximum_inequality_violation']<1e-9 and abs(r['mean_residual'])<1e-9
            lp.append({'A':A,'B':B,'s':s,'lipschitz':lip,'expected_capacity':want,'computed_capacity':r['capacity_midpoint_model']})
    result={'status':'PASS','exact_quartet_fixtures':count,'exact_density_area_fixtures':densities,'independent_constant_cost_lp_fixtures':lp,'scope':'algebra and LP-model controls; no continuum return for variable coefficients','implementation_hashes':{n:hashlib.sha256((R/n).read_bytes()).hexdigest() for n in [Path(__file__).name,'probe_odd_lipschitz_capacity.py']}}
    a.out.write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))
if __name__=='__main__':main()
