"""Discovery-only positive-part integration and cross-bin certificate reuse."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'deps'))
sys.path.insert(0,str(ROOT/'sources/lower-bound/certificate'))
import copy,json,math
import numpy as np
from scipy.optimize import brentq
import prove_erdos_0380554275_arb as source
from flint import arb,ctx
ctx.prec=160

def approximate_D(cert,samples=20001):
    terms,fterms,_,_=source.prepare_bin(cert,arb('1e-14'))
    roots=source.speed_roots(fterms,samples)
    endpoints=np.array([-2.]+roots+[2.])
    mid=(endpoints[:-1]+endpoints[1:])/2
    positive=source.q_vec(fterms,mid)>0
    def anti(x):
        val=x.copy()
        for k,p,l,b in fterms:
            val+=l*b*x
            if k=='t': primitive=x*x/2
            elif k=='-t': primitive=-x*x/2
            elif k=='t2': primitive=x*x*x/3
            elif k=='-t2': primitive=-x*x*x/3
            elif k=='cos': primitive=np.sin(float(p)*x)/float(p)
            elif k=='-cos': primitive=-np.sin(float(p)*x)/float(p)
            elif k=='sin': primitive=-np.cos(float(p)*x)/float(p)
            elif k=='-sin': primitive=np.cos(float(p)*x)/float(p)
            elif k=='cos+asin': primitive=(np.sin(float(p[0])*x)-float(p[1])*np.cos(float(p[0])*x))/float(p[0])
            else: raise ValueError(k)
            val-=l*primitive
        return val
    D=float(np.sum(np.diff(anti(endpoints))[positive]))
    return D,len(roots)

def main():
    data=json.loads((ROOT/'sources/lower-bound/certificate/erdos_aug_central_gridF400.json').read_text(),parse_float=str)
    rows=[]
    for upper in np.linspace(0,.00625,26):
        choices=[]
        for idx in [85,86,87,88]:
            c=copy.deepcopy(data['bins'][idx]); c['lo']=str(max(0,upper-.00025)); c['hi']=str(upper)
            d,roots=approximate_D(c)
            choices.append({'source_bin':idx,'D_float':d,'bound_float':1/d,'roots':roots})
        best=min(choices,key=lambda r:r['D_float'])
        row={'mean_interval':[max(0,float(upper)-.00025),float(upper)],'best':best,'choices':choices}
        rows.append(row)
        print(json.dumps({'mean':float(upper),'best':best}),flush=True)
    (ROOT/'runs/dual-cross-bin-diagnostic.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')

if __name__=='__main__': main()
