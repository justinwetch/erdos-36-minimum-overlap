"""Numerical capacity relaxation using the actual odd-overlap Lipschitz law."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,hashlib,json,time
from fractions import Fraction as F
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix
from dual_diagnostic import source,ROOT
from circle_certificate import ctx
from verify_hybrid_outer_blend import compile_blend
from shared_mean_numerator import coefficients,value
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def capacity(A,B,s,M,m,lipschitz):
    n=len(A);h=1/n;count=2*n+1;c=abs(A)+abs(B);cost=np.zeros(count);cost[:n]-=h*s/2;cost[1:n+1]-=h*s/2;cost[n+1:]=h*c
    ri=[];ci=[];vv=[];rhs=[]
    def row(entries,b):
        k=len(rhs);rhs.append(b)
        for j,v in entries:ri.append(k);ci.append(j);vv.append(v)
    for i in range(n):
        row([(i,.5),(i+1,.5),(n+1+i,-1)],0);row([(i,-.5),(i+1,-.5),(n+1+i,-1)],0)
        if lipschitz:row([(i,-1),(i+1,1)],h);row([(i,1),(i+1,-1)],h)
    ub=coo_matrix((vv,(ri,ci)),shape=(len(rhs),count)).tocsr();area=np.zeros(count);area[:n+1]=2*h;area[[0,n]]=h
    bounds=[(0,0)]+[(-M,M)]*n+[(0,M)]*n;start=time.time();r=linprog(cost,A_ub=ub,b_ub=rhs,A_eq=coo_matrix(area[None,:]).tocsr(),b_eq=[m],bounds=bounds,method='highs')
    assert r.success,r.message;baseline=2*M*float(np.sum(np.maximum(A,0)+np.maximum(B,0)))*h
    return {'capacity_midpoint_model':baseline-r.fun,'iterations':r.nit,'maximum_inequality_violation':float(max(0,max(ub@r.x-np.array(rhs)))),'mean_residual':float(area@r.x-m),'maximum_slope':float(max(abs(np.diff(r.x[:n+1])))/h),'elapsed':time.time()-start}
def main():
    ap=argparse.ArgumentParser();ap.add_argument('seed',type=Path);ap.add_argument('--name',required=True);ap.add_argument('--mean',required=True);ap.add_argument('--peak',default='.380626300');ap.add_argument('--grids',default='2048,4096,8192');a=ap.parse_args();start=time.time();run=ROOT/'runs'/a.name;run.mkdir();ctx.prec=200;d=json.loads(a.seed.read_text());poly,_=coefficients(d);L=value(poly,F(a.mean));terms,parts,_=compile_blend(d);ft=[]
    for v in terms:
        param=[float(v.xi),float(v.alpha)] if v.kind=='cos+asin' else float(v.xi) if v.kind in {'cos','-cos','sin','-sin'} else None
        ft.append((v.kind,param,float(v.lam),float(v.B)))
    left=np.array([float(p[0]) for p in parts]);constant=np.array([float(p[2]) for p in parts]);slope=np.array([float(p[3]) for p in parts])
    def q(x):
        i=np.maximum(0,np.minimum(len(parts)-1,np.searchsorted(left,x,side='right')-1));return source.q_vec(ft,x)+constant[i]+slope[i]*x
    rows=[];M,m=float(F(a.peak)),float(F(a.mean))
    for n in map(int,a.grids.split(',')):
        x=(np.arange(n)+.5)/n;qt,qmt,qc,qmc=q(x),q(-x),q(2-x),q(x-2);A=(qt+qmt)/2;B=(qc+qmc)/2;s=(qt-qmt+qc-qmc)/2
        pointwise=M*float(np.mean(A+B+np.maximum(abs(A)+abs(B),abs(s))));free=capacity(A,B,s,M,m,False);lip=capacity(A,B,s,M,m,True)
        row={'grid':n,'exact_expectation_lower_at_mean':str(L),'expectation_lower_display':float(L),'folded_pointwise_capacity_midpoint':pointwise,'mean_constrained':free,'mean_and_lipschitz_constrained':lip,'lipschitz_capacity_reduction_same_grid':free['capacity_midpoint_model']-lip['capacity_midpoint_model'],'candidate_gap_midpoint_model':float(L)-lip['capacity_midpoint_model']};rows.append(row);print(json.dumps(row),flush=True)
    result={'status':'NUMERICAL_CAPACITY_DISCRIMINATOR_ONLY','scope':'midpoint objective and piecewise linear odd-profile LP; no continuum upper capacity certificate, mu bound, or optimality claim','mean':a.mean,'tested_peak':a.peak,'rows':rows,'seed_sha256':sha(a.seed),'implementation_sha256':sha(Path(__file__)),'elapsed':time.time()-start};(run/'summary.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps({'status':result['status'],'elapsed':result['elapsed']}),flush=True)
if __name__=='__main__':main()
