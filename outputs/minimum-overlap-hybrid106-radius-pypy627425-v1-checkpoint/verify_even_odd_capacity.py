"""Certify all-mean capacity polynomials from an even kernel and flow duals."""
import argparse,bisect,hashlib,json,math,time
from fractions import Fraction as F
from pathlib import Path
from shared_mean_numerator import coefficients,value
R=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def sqrt_upper(q,digits=30):
    q=F(q);assert q>=0;s=10**digits;k=math.isqrt(q.numerator*s*s//q.denominator)
    if k*k*q.denominator<q.numerator*s*s:k+=1
    assert F(k,s)**2>=q;return F(k,s)
def main():
    ap=argparse.ArgumentParser();ap.add_argument('bundle',type=Path);ap.add_argument('--adapter',type=Path,required=True);ap.add_argument('--energy',type=Path,required=True);ap.add_argument('--mode',choices=['arb','integer'],required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();start=time.time();bundle=json.loads(a.bundle.read_text());assert bundle['schema']=='even-odd-capacity-bundle-v1';seed=R/bundle['kernel'];d=json.loads(seed.read_text());assert sha(seed)==bundle['kernel_sha256'] and F(d['theta_outer'])==0 and d['outer']['active']==[]
    adapter=json.loads(a.adapter.read_text());energy=json.loads(a.energy.read_text());assert adapter['status']=='PASS' and adapter['wrapper_sha256']==sha(seed) and energy['status']=='PASS' and energy['mode']==a.mode and energy['seed_sha256']==sha(seed)
    assert adapter['implementation_sha256']==sha(R/'adapt_even_central_reports.py')
    bindings={str(p.resolve()):sha(p) for p in [a.bundle,a.adapter,a.energy,seed,Path(__file__)]}
    for path,h in adapter['bindings'].items():p=R/path;assert sha(p)==h;bindings[str(p.resolve())]=h
    for n,h in energy['implementation_hashes'].items():assert sha(R/n)==h;bindings[str((R/n).resolve())]=h
    poly,_=coefficients(d);assert list(map(str,poly))==adapter['polynomial_exact'];D=F(adapter['maximum_wrapped_denominator_exact']);assert D>0
    bounds=list(map(F,bundle['boundaries_exact']));assert bounds[0]==0 and bounds[-1]==1 and all(x<y for x,y in zip(bounds,bounds[1:]));h=[y-x for x,y in zip(bounds,bounds[1:])];n=len(h);duals=[]
    for row in bundle['duals']:
        k=list(map(F,row['k']));v=list(map(F,row['v']));tau,kappa=F(row['tau']),F(row['kappa']);assert len(k)==n and len(v)==n-1 and all(abs(x)<=1 for x in k)
        div=[-v[0]]+[x-y for x,y in zip(v,v[1:])]+[v[-1]];T=sum((abs(v[i])*(h[i]+h[i+1])/2 for i in range(n-1)),F(0))+abs(kappa)*h[0]/2;duals.append({'k':k,'v':v,'tau':tau,'kappa':kappa,'div':div,'T':T,'residual':0,'search_mean':row['search_mean']})
    assert duals;E=max(h)**2*sqrt_upper(F(energy['energy_upper_exact'])/120)
    if a.mode=='arb':
        from circle_certificate import ctx,arb,reference
        from hybrid_certificate import A
        from verify_hybrid_outer_blend import compile_blend
        from verify_shared_mean_return import ball_interval
        ctx.prec=240;terms,parts,_=compile_blend(d);terms=[t for t in terms if t.lam!=0];assert all(t.kind in {'cos','-cos','t2','-t2'} for t in terms)
        def kernel_primitive(x):return reference.Q(terms,A(x))
        def number(x):return A(x)
        def absolute(x):return abs(x)
        def residual_upper(x):return ball_interval(x.abs_upper().str(70))[1]
    else:
        from verify_integer_hybrid_outer_blend import BlendChecker
        from verify_integer_circle import I,SCALE
        checker=BlendChecker(d);parts=checker.parts;assert checker.linear==0 and all(t[2].lo==t[2].hi==0 for t in checker.terms)
        def kernel_primitive(x):return checker.primitive(x)
        def number(x):return I(x)
        def absolute(x):
            if x.lo>=0:return x
            if x.hi<=0:return -x
            return I.raw(0,x.abs_upper())
        def residual_upper(x):return F(x.abs_upper(),SCALE)
    required={F(0),F(1)}
    for p in parts:
        for x in p[:2]:
            for y in [x,-x,2-x,2+x]:
                if 0<=y<=1:required.add(y)
    assert required<=set(bounds),'capacity cells cross an affine-kernel breakpoint; covariance energy would omit a jump'
    left=[p[0] for p in parts];prefix=[F(0)]
    for lo,hi,c,s in parts:prefix.append(prefix[-1]+c*(hi-lo)+s*(hi*hi-lo*lo)/2)
    cache={}
    def P(x):
        if x not in cache:
            i=min(len(parts)-1,bisect.bisect_right(left,x)-1);assert i>=0;lo,hi,c,s=parts[i];assert lo<=x<=hi
            cache[x]=kernel_primitive(x)+number(prefix[i]+c*(x-lo)+s*(x*x-lo*lo)/2)
        return cache[x]
    for i,(lo,hi) in enumerate(zip(bounds,bounds[1:])):
        IA=P(hi)-P(lo);IB=P(2-lo)-P(2-hi);c_integral_lower=absolute(IA)+absolute(IB)
        for row in duals:
            residual=-number(row['k'][i])*c_integral_lower-number(2*row['tau']*h[i]+row['div'][i]+(row['kappa'] if i==0 else 0));row['residual']+=residual_upper(residual)
        if (i+1)%1000==0:print(json.dumps({'mode':a.mode,'capacity_cells':i+1,'total_cells':n,'primitive_points':len(cache),'elapsed':time.time()-start}),flush=True)
    rows=[]
    for i,row in enumerate(duals):
        numerator=(poly[0]-row['T']-E,poly[1]-row['tau'],poly[2]);denominator=D+row['residual'];m=F(row['search_mean']);rows.append({'index':i,'numerator_polynomial_exact':list(map(str,numerator)),'denominator_upper_exact':str(denominator),'flow_cost_exact':str(row['T']),'covariance_error_upper_exact':str(E),'residual_l1_upper_exact':str(row['residual']),'tau_exact':str(row['tau']),'search_mean':str(m),'lower_bound_at_search_mean_display':float(value(numerator,m)/denominator)})
    for n in ['verify_even_odd_capacity.py','adapt_even_central_reports.py','shared_mean_numerator.py','verify_shared_mean_return.py']:bindings[str((R/n).resolve())]=sha(R/n)
    assert all(sha(Path(p))==v for p,v in bindings.items()),'proof input changed during capacity verification'
    result={'status':'PASS','scope':'all-mean conditional quadratic returns from physical odd-profile Lipschitz capacity; complete mean cover and fresh replay remain separate obligations','mode':a.mode,'kernel_sha256':sha(seed),'bundle_sha256':sha(a.bundle),'cells':len(h),'primitive_points':len(cache),'energy_upper_exact':energy['energy_upper_exact'],'maximum_cell_width_exact':str(max(h)),'rows':rows,'bindings':bindings,'implementation_sha256':sha(Path(__file__)),'elapsed':time.time()-start};a.out.write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps({'status':result['status'],'mode':a.mode,'bounds_at_search_means':[r['lower_bound_at_search_mean_display'] for r in rows],'elapsed':result['elapsed']}),flush=True)
if __name__=='__main__':main()
