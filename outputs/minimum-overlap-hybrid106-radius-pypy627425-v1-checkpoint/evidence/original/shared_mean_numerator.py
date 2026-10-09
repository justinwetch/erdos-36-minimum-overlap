"""Exact common-mean return for an already integrated blend kernel.

The polynomial is conditional on the existing hybrid normalization and
universal Fourier/Gram premises. It does not perform continuum integration.
"""
from fractions import Fraction as F

def coefficients(d):
    assert d['schema']=='hybrid-outer-blend-v1'
    h,o=d['hybrid'],d['outer'];theta=F(d['theta_outer']);ell=F(d['hybrid_numerator_lower'])
    assert 0<=theta<=1 and ell>0
    lo,hi=F(o['lo']),F(o['hi']);assert -1<=lo<=hi<=1
    r=max(abs(lo),abs(hi));max2=r*r;min2=F(0) if lo<=0<=hi else min(lo*lo,hi*hi)
    C=F(h['y2'])/2
    for row in h['functional_rows']:
        mu=F(row['multiplier']);cert=row['certificate'];assert mu>=0
        assert cert['schema']=='phase-gram-functional-v2'
        C-=mu*F(cert['mean_multiplier'])*F(cert['cells']**2,4)
    hs=(1-theta)/ell
    a=F(1)-hs*min(F(0),C)*max2;b=F(0);c=hs*C
    for row in o['active']:
        w=theta*F(row['lambda']);assert w>=0;k=row['kind']
        if k=='t':a+=w*hi;b-=w
        elif k=='-t':a-=w*lo;b+=w
        elif k=='t2':a+=w*max2/2;c-=w/2
        elif k=='-t2':a-=w*min2/2;c+=w/2
        else:assert k in {'cos','-cos','sin','-sin','cos+asin'}
    return (a,b,c),{'hybrid_mean_square_coefficient':str(C),'normalization_premise':str(ell),'original_mean_bin':[str(lo),str(hi)]}

def value(p,x):a,b,c=p;return a+b*x+c*x*x

def minimum(p,lo,hi):
    lo,hi=F(lo),F(hi);assert lo<=hi
    candidates=[lo,hi];a,b,c=p
    if c>0 and lo<=-b/(2*c)<=hi:candidates.append(-b/(2*c))
    x=min(candidates,key=lambda x:value(p,x));return value(p,x),x

def controls():
    # Exact minimum, including a convex interior vertex and concave endpoints.
    cases=[((F(1),F(-2),F(1)),F(0),F(2),F(0)),
           ((F(1),F(0),F(-1)),F(-2),F(1),F(-3)),
           ((F(1),F(3),F(0)),F(-1),F(2),F(-2))]
    for p,lo,hi,want in cases:
        got,x=minimum(p,lo,hi);assert got==want and lo<=x<=hi
        assert all(value(p,lo+(hi-lo)*F(j,100))>=got for j in range(101))
    count=0
    for lo,hi in [(F(1,10),F(1,5)),(F(-1,5),F(1,10)),(F(-1,5),F(-1,10))]:
        for C in [F(-3,2),F(0),F(2,3)]:
            d={'schema':'hybrid-outer-blend-v1','theta_outer':'1/3','hybrid_numerator_lower':'4/5',
               'hybrid':{'y2':str(2*C),'functional_rows':[]},
               'outer':{'lo':str(lo),'hi':str(hi),'active':[{'kind':k,'lambda':'2/7'} for k in ['t','-t','t2','-t2']]}}
            p,_=coefficients(d);r=max(abs(lo),abs(hi));min2=0 if lo<=0<=hi else min(lo*lo,hi*hi)
            for j in range(11):
                m=lo+(hi-lo)*F(j,10)
                direct=1+F(5,6)*(C*m*m-min(0,C)*r*r)
                direct+=F(2,21)*((hi-m)+(m-lo)+(r*r-m*m)/2+(m*m-min2)/2)
                assert value(p,m)==direct and direct>=1;count+=1
    return {'status':'PASS','exact_minimum_fixtures':len(cases),'exact_shared_mean_fixtures':count,
            'scope':'rational polynomial identities only; original normalized kernel integration and premises still required'}
