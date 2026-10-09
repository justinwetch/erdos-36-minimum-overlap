"""Nonuniform step correlation and exact certification, with distinct checks."""
from collections import defaultdict
from fractions import Fraction
import json

import numpy as np

def score_float(values, edges, return_pair=False):
    f = np.asarray(values)
    x = np.asarray(edges)
    n = len(f)
    if len(x) != n+1 or np.any(np.diff(x)<=0):
        raise ValueError('invalid grid')
    da = np.diff(np.r_[0.,f,0.])
    db = np.diff(np.r_[0.,1-f,0.])
    locations = (x[None,:]-x[:,None]).ravel()
    weights = (-da[:,None]*db[None,:]).ravel()
    order = np.argsort(locations, kind='stable')
    loc = locations[order]
    w = weights[order]
    # Use long double for discovery to reduce cancellation. Exact arithmetic
    # below supplies the certificate independently of these floating values.
    slope = np.cumsum(w, dtype=np.longdouble)
    val = np.r_[np.longdouble(0),np.cumsum(slope[:-1]*np.diff(loc),dtype=np.longdouble)]
    k = int(np.argmax(val))
    if return_pair:
        original = int(order[k]); i,j = divmod(original,n+1)
        return float(val[k]), (i,j), float(loc[k])
    return float(val[k])

def peaks_float(values, edges, margin=1e-6, max_peaks=500):
    f=np.asarray(values); x=np.asarray(edges); n=len(f)
    da=np.diff(np.r_[0.,f,0.]); db=np.diff(np.r_[0.,1-f,0.])
    loc0=(x[None,:]-x[:,None]).ravel()
    w0=(-da[:,None]*db[None,:]).ravel()
    relevant=np.flatnonzero(w0!=0)
    order0=np.argsort(loc0[relevant],kind='stable'); order=relevant[order0]
    loc=loc0[order]; w=w0[order]
    slope=np.cumsum(w,dtype=np.longdouble)
    val=np.r_[np.longdouble(0),np.cumsum(slope[:-1]*np.diff(loc),dtype=np.longdouble)]
    peak=float(val.max())
    candidates=np.flatnonzero((np.r_[0.,slope[:-1]]>=0)&(slope<=0)&(val>=peak-margin))
    if not len(candidates): candidates=np.array([int(np.argmax(val))])
    candidates=candidates[np.argsort(val[candidates])[::-1]][:max_peaks]
    pairs=[divmod(int(order[k]),n+1) for k in candidates]
    return peak,pairs

def value_gradient_at_pair(values,edges,pair):
    f=np.asarray(values); x=np.asarray(edges); n=len(f)
    da=np.diff(np.r_[0.,f,0.]); db=np.diff(np.r_[0.,1-f,0.])
    i,j=pair; s=x[j]-x[i]
    r=s-(x[None,:]-x[:,None]); mask=r>0
    r=np.maximum(r,0)
    # The selected knot's positive-part argument is identically zero, so its
    # derivative contributes zero even though its location moves.
    r[i,j]=0.; mask[i,j]=False
    v=-(r@db)+(da@r)
    grad_f=v[:-1]-v[1:]
    w=-da[:,None]*db[None,:]*mask
    grad_x=w.sum(axis=1)-w.sum(axis=0)
    slope=w.sum()
    grad_x[i]-=slope; grad_x[j]+=slope
    value=float(np.sum((-da[:,None]*db[None,:])*r,dtype=np.longdouble))
    return value,grad_f,grad_x

def exact_certificate(values, edges, denom=10**13):
    n = len(values)
    p = [round(float(x)*denom) for x in edges]
    p[0],p[-1] = 0, 2*denom
    if not all(p[i]<p[i+1] for i in range(n)):
        raise ValueError('rounded grid not increasing')
    a = [max(0,min(denom,round(float(v)*denom))) for v in values]
    widths = [p[i+1]-p[i] for i in range(n)]
    deficit = denom*denom-sum(v*w for v,w in zip(a,widths))
    # One exact rational height change; all heights then share one denominator.
    idx = max(range(n), key=lambda i: min(a[i],denom-a[i])*widths[i])
    w = widths[idx]
    a = [v*w for v in a]
    a[idx] += deficit
    height_denom = denom*w
    if not all(0<=v<=height_denom for v in a):
        raise ValueError('repair left box')
    return {'height_denominator':height_denom,'numerators':a,
            'edge_denominator':denom,'edges':p,
            'mass_repair':{'cell':idx,'added_height':str(Fraction(deficit,denom*w))}}

def verify_nonuniform(obj):
    a = obj['numerators']; A = obj['height_denominator']
    p = obj['edges']; B = obj['edge_denominator']; n = len(a)
    def need(c,msg):
        if not c: raise ValueError(msg)
    need(type(A)is int and A>0 and type(B)is int and B>0,'denominators')
    need(len(p)==n+1 and n>0,'length')
    need(all(type(v)is int and 0<=v<=A for v in a),'box')
    need(all(type(v)is int for v in p) and p[0]==0 and p[-1]==2*B,'support')
    need(all(p[i]<p[i+1] for i in range(n)),'grid')
    need(sum(a[i]*(p[i+1]-p[i]) for i in range(n))==A*B,'mass')
    da = [a[0]]+[a[i]-a[i-1] for i in range(1,n)]+[-a[-1]]
    g = [A-v for v in a]
    db = [g[0]]+[g[i]-g[i-1] for i in range(1,n)]+[-g[-1]]
    events = defaultdict(int)
    for i in range(n+1):
        for j in range(n+1):
            events[p[j]-p[i]] -= da[i]*db[j]
    # Independently obtain the second derivative by summing trapezoids for
    # literal interval-pair intersections; no jump arrays used in this check.
    second = defaultdict(int)
    for i in range(n):
        for j in range(n):
            c = a[i]*(A-a[j])
            second[p[j]-p[i+1]] += c
            second[p[j]-p[i]] -= c
            second[p[j+1]-p[i+1]] -= c
            second[p[j+1]-p[i]] += c
    need(dict(events)==dict(second),'independent event maps disagree')
    slope=0; value=0; previous=-2*B; peak=0; argmax=previous
    for location in sorted(events):
        value += slope*(location-previous)
        if value>peak:
            peak=value; argmax=location
        slope += events[location]
        previous=location
    need(slope==0 and value==0,'outside-support closure')
    # Direct interval integration at the maximizing translate.
    direct = 0
    for i in range(n):
        for j in range(n):
            length = min(p[i+1],p[j+1]-argmax)-max(p[i],p[j]-argmax)
            if length>0: direct += a[i]*(A-a[j])*length
    need(direct==peak,'direct integral disagrees at peak')
    q=Fraction(peak,A*A*B)
    scale=10**25; lower=q.numerator*scale//q.denominator
    return {'status':'PASS','n':n,'distinct_shift_knots_checked':len(events),
            'independent_event_map':'PASS','direct_peak_integral':'PASS',
            'mass':'1','box':'exact','score_fraction':str(q),'score_float':float(q),
            'decimal_lower':f'{lower//scale}.{lower%scale:025d}',
            'decimal_upper_strict':f'{(lower+1)//scale}.{(lower+1)%scale:025d}',
            'argmax_shift':str(Fraction(argmax,B)),
            'scope':'exact continuum supremum of this nonuniform step function'}

if __name__=='__main__':
    import argparse
    from pathlib import Path
    ap=argparse.ArgumentParser(); ap.add_argument('input'); ap.add_argument('--out')
    args=ap.parse_args()
    result=verify_nonuniform(json.loads(Path(args.input).read_text()))
    if args.out: Path(args.out).write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))
