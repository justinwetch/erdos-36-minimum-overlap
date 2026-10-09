"""Exact embedded Gram premises and their piecewise affine kernels."""
import hashlib,json
from fractions import Fraction as F
from verify_phase_gram import compile_dual,restricted,positive_definite

def validate(data,mean):
    if data['schema']!='periodic-gram-functional-v5' or data['base_schema']!='periodic-hypermetric-dual-v2':raise ValueError('hybrid schema')
    if not 0<=mean<=1:raise ValueError('mean radius')
    functions=[];reports=[]
    for row in data['functional_rows']:
        mu=F(row['multiplier'])
        if mu<0:raise ValueError('negative functional multiplier')
        cert=dict(row['certificate']);cert['mean_abs_max']='0'
        if cert['schema']!='phase-gram-functional-v2':raise ValueError('signed functional required')
        G,L0=compile_dual(cert);passed,stats=positive_definite(restricted(G))
        if not passed:raise ValueError('embedded Gram PSD failure')
        N=cert['cells'];a=F(2,N);eta=F(cert['mean_multiplier']);gamma=list(map(F,cert['functional_weights']))
        functions.append({'mu':mu,'N':N,'a':a,'gamma':gamma,'L0':L0,'mean_coefficient':-eta/a**2})
        reports.append({'passed':True,'canonical_certificate_sha256':hashlib.sha256(json.dumps(row['certificate'],sort_keys=True,separators=(',',':')).encode()).hexdigest(),
            'mean_abs_max':str(mean),'functional_lower_exact':str(L0-eta*(mean/a)**2),'restricted_psd_check':stats})
    return functions,reports

def knots(functions):
    return {F(2*j,f['N']) for f in functions for j in range(f['N']+1)}|{F(0),F(2)}

def affine(functions,t):
    intercept=slope=F(0)
    for f in functions:
        a=f['a'];j=min(f['N']-1,int(t//a));gamma=f['gamma']
        left=gamma[j]/a if j==0 else gamma[j]/(2*a);right=gamma[j+1]/(2*a)
        s=(right-left)/a;intercept+=f['mu']*(left-s*j*a);slope+=f['mu']*s
    return intercept,slope
