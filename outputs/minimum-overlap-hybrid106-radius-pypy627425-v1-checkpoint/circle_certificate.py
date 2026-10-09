"""Extract and certify a continuous periodic-triangle dual.

The optimizer's objective and residuals are not trusted. Decimal multipliers
define a fresh continuous function, integrated on every exact step cell using
outward Arb Taylor bounds. See CIRCLE_PROOF.md for the universal inequalities.
"""
import sys, argparse, hashlib, json, time
from pathlib import Path
from decimal import Decimal, getcontext
from fractions import Fraction
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'deps'))
import numpy as np
from flint import arb,ctx
from verify_fourth_order import q_jet,fourth_derivative_bound,reference

def offsets(data):
    if data['schema']=='periodic-hypermetric-dual-v2':
        n=int(data['cells']); h=Fraction(2,n); u=[Fraction(0)]*n
        for family in data['families']:
            coefficients,bound=family_coefficients(family)
            z=list(map(Fraction,family['z']))
            if len(z)!=n or any(v>0 for v in z): raise ValueError('invalid hypermetric multipliers')
            for i,value in enumerate(z):
                if not value: continue
                for k,c in coefficients.items():
                    for j in range(k): u[(k*i+j)%n]+=value*c/k
        return [(u[j]+u[n-1-j])/(2*h) for j in range(n)]
    n=int(data['cells']); h=Decimal(2)/n
    low=list(map(Decimal,data['low'])); high=list(map(Decimal,data['high']))
    if len(low)!=n or len(high)!=n: raise ValueError('circle multiplier length')
    if any(v>0 for v in low+high): raise ValueError('positive inequality multiplier')
    u=[Decimal(0)]*n
    for i,(a,b) in enumerate(zip(low,high)):
        u[i]+=2*(b-a)
        u[2*i%n]+=(a+b)/2; u[(2*i+1)%n]+=(a+b)/2
    return [Fraction((u[j]+u[n-1-j])/(2*h)) for j in range(n)]

def family_coefficients(family):
    positions=family['positions']; b=family['b']
    if len(positions)!=len(b) or len(set(positions))!=len(positions): raise ValueError('family dimensions')
    if any(type(v)!=int for v in positions+b) or min(positions)<0: raise ValueError('integer family required')
    coefficients={}
    for i in range(len(b)):
        for j in range(i+1,len(b)):
            k=abs(positions[i]-positions[j])
            coefficients[k]=coefficients.get(k,0)+b[i]*b[j]
    return {k:c for k,c in coefficients.items() if c},sum(b)**2//4

def extract(path,out,cutoff):
    a=np.load(path); n=int(a['cells']); k=len(a['frequencies'])
    if not bool(a['circle']) or int(a['extra_count'])!=0: raise ValueError('unsupported LP')
    z=a['inequality']
    def clean(v): return repr(float(v)) if float(v)<-cutoff else '0'
    data={'schema':'periodic-triangle-dual-v1','cells':n,
          'y0':repr(float(a['equality'][0])),'y2':repr(float(a['equality'][1])),
          'cos':[{'xi':repr(float(x)),'z':clean(v)} for x,v in zip(a['frequencies'],z[:k]) if v < -cutoff],
          'low':[clean(v) for v in z[k+n:k+2*n]],
          'high':[clean(v) for v in z[k+2*n:k+3*n]],
          'discovery_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
          'scope':'continuous dual proposal; requires verification'}
    count=int(a['circle_multiples']) if 'circle_multiples' in a else 1
    hyper=json.loads(str(a['hypermetric_families'])) if 'hypermetric_families' in a else []
    if count>1 or hyper:
        data['schema']='periodic-hypermetric-dual-v2'; data.pop('low'); data.pop('high'); families=[]; at=k+n
        for m in range(1,count+1):
            for b in ([1,-1,1],[1,1,1]):
                families.append({'positions':[0,1,m+1],'b':b,'z':[clean(v) for v in z[at:at+n]]}); at+=n
        for family in hyper:
            families.append({'positions':family.get('positions',list(range(len(family['b'])))),'b':family['b'],'z':[clean(v) for v in z[at:at+n]]}); at+=n
        if at!=len(z): raise ValueError('LP dual ordering mismatch')
        data['families']=[f for f in families if any(Decimal(v)!=0 for v in f['z'])]
    offsets(data)
    out.write_text(json.dumps(data,indent=2),encoding='utf-8')

def verify(data,width,order):
    if data['schema']=='periodic-interval-dual-v4':
        from verify_interval_data import verify as interval_verify
        return interval_verify(data,width,order)
    if data['schema'] not in {'periodic-triangle-dual-v1','periodic-hypermetric-dual-v2'}: raise ValueError('schema')
    n=int(data['cells'])
    if n<2 or n&(n-1): raise ValueError('power-of-two cell count required')
    h=Decimal(2)/n; steps=offsets(data); terms=[]
    y0,y2=arb(data['y0']),arb(data['y2'])
    if Decimal(data['y2']):
        kind='t2' if Decimal(data['y2'])<0 else '-t2'
        terms.append(reference.Term(kind,None,-y2 if Decimal(data['y2'])<0 else y2,arb(0)))
    L=y0+y2*arb(2)/3
    if data['schema']=='periodic-triangle-dual-v1':
        L+=2*sum((arb(v) for v in data['high']),arb(0)); circle_rows=data['low']+data['high']
    else:
        circle_rows=[]
        for family in data['families']:
            coefficients,bound=family_coefficients(family)
            L+=bound*sum((arb(v) for v in family['z']),arb(0)); circle_rows+=family['z']
    for row in data['cos']:
        if Decimal(row['z'])>0 or Decimal(row['xi'])==0: raise ValueError('invalid cosine row')
        z,xi=arb(row['z']),arb(row['xi'])
        terms.append(reference.Term('cos',row['xi'],-z,arb(0)))
        L+=z*(xi.sin()/xi)**2
    M4=fourth_derivative_bound(terms)
    M2=2*y2.abs_upper()+sum((t.lam.abs_upper()*t.xi.abs_upper()**2 for t in terms if t.kind=='cos'),arb(0))
    total=arb(0); nodes=amb=pos=neg=0; cell_width=Decimal(width)
    for i,step in enumerate(steps):
        # Half-open cell endpoints have measure zero. No interval crosses a jump.
        shift=y0-1+arb(step.numerator)/step.denominator; stack=[(h*i,h*(i+1))]
        while stack:
            aD,bD=stack.pop(); a,b=arb(str(aD)),arb(str(bD)); c,r=(a+b)/2,(b-a)/2
            q,q1,q2,q3=q_jet(terms,c); q+=shift
            if order==4:
                radius=q1.abs_upper()*r+q2.abs_upper()*r*r/2+q3.abs_upper()*r**3/6+M4*r**4/24
            else: radius=q1.abs_upper()*r+M2*r*r/2
            nodes+=1
            if nodes>10000000: raise RuntimeError('node limit')
            lo,hi=q-radius,q+radius
            if hi<=0: neg+=1; continue
            if lo>=0:
                total+=(reference.Q(terms,b)-reference.Q(terms,a)+shift*(b-a)).upper(); pos+=1
            elif bD-aD<=cell_width:
                total+=(b-a)*reference.pos_upper(hi); amb+=1
            else:
                mid=(aD+bD)/2; stack.extend(((aD,mid),(mid,bD)))
    return (2*total).upper(),L,{'nodes':nodes,'ambiguous':amb,'positive':pos,'negative':neg,
                               'cosine_rows':len(data['cos']),'nonzero_circle_rows':sum(Decimal(v)!=0 for v in circle_rows)}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('certificate',type=Path)
    ap.add_argument('--extract',type=Path); ap.add_argument('--cutoff',type=float,default=1e-12)
    ap.add_argument('--mean-max',default='0'); ap.add_argument('--target',default='0')
    ap.add_argument('--width',default='0.0000001'); ap.add_argument('--prec',type=int,default=200)
    ap.add_argument('--order',type=int,choices=[2,4],default=4); ap.add_argument('--report',type=Path)
    args=ap.parse_args(); getcontext().prec=120; ctx.prec=args.prec; start=time.time()
    if args.extract: extract(args.extract,args.certificate,args.cutoff)
    data=json.loads(args.certificate.read_text()); D,L,info=verify(data,args.width,args.order)
    m=Decimal(args.mean_max)
    if m<0: raise ValueError('negative mean maximum')
    if Decimal(data['y2'])<0: L+=arb(data['y2'])*arb(str(m*m))/2
    bound=L/D; passed=bool(L>0 and D>0 and bound>arb(args.target))
    out={'passed':passed,'mean_abs_max':str(m),'target':args.target,'lower_bound_ball':bound.str(70),
         'numerator_ball':L.str(70),'positive_integral_upper_ball':D.str(70),
         'precision_bits':ctx.prec,'width':args.width,'order':args.order,'elapsed':time.time()-start,
         'certificate_sha256':hashlib.sha256(args.certificate.read_bytes()).hexdigest(),
         'scope':'continuous lower bound for |mean| <= mean_abs_max; not a full mean cover by itself',**info}
    if args.report: args.report.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps(out,indent=2),flush=True)
    if not passed: raise SystemExit(1)
if __name__=='__main__': main()
