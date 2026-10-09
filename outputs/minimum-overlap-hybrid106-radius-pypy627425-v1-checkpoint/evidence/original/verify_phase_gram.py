"""Standard-library rational dual and PSD checker for phase-averaged Grams."""
import argparse, hashlib, json, math, time
from fractions import Fraction as F
from pathlib import Path

def need(ok,message):
    if not ok:raise ValueError(message)

def pi_lower():
    def bounds(x):
        total=sum(((-1)**j*x**(2*j+1)/(2*j+1) for j in range(12)),F(0))
        return total,total+x**25/25
    a,b=bounds(F(1,5));c,d=bounds(F(1,239))
    # Machin's identity: pi=16*atan(1/5)-4*atan(1/239).
    return 16*a-4*d

def compile_dual(data):
    functional=data['schema']=='phase-gram-functional-v2'
    need(functional or data['schema']=='phase-gram-dual-v1','schema')
    N=data['cells'];need(type(N)==int and 2<=N<=512,'cell count')
    n=N+1;a=F(2,N);G=[[F(0) for _ in range(n)] for _ in range(n)];lower=F(0)
    def weight(x):
        value=F(x);need(value>=0,'negative multiplier');return value
    def entry(i,j,value):
        if i==j:G[i][i]+=value
        else:G[i][j]+=value/2;G[j][i]+=value/2
    def diagonal(k,value):
        for i in range(n-k):entry(i,i+k,value)
    bases=[F(1,2)-a/12]+[(2-k*a)/4 for k in range(1,N)]+[a/24]
    for i,z in enumerate(data['diagonal']):
        w=weight(z);entry(i,i,w);lower-=w*(F(1,3) if i in (0,N) else 1)
    need(len(data['diagonal'])==n,'dimensions')
    if functional:
        caps=list(map(F,data['functional_weights']));need(len(caps)==n and any(caps),'functional dimensions')
    else:
        need(len(data['caps'])==n,'cap dimensions')
        caps=list(map(weight,data['caps']));need(sum(caps)==1,'exact cap normalization')
    for k,w in enumerate(caps):diagonal(k,-a*w/4);lower+=w*bases[k]
    nonnegative=data.get('nonnegative',[]);need(len(nonnegative) in (0,n),'nonnegative dimensions')
    for k,z in enumerate(nonnegative):
        w=weight(z);diagonal(k,a*w/4);lower-=w*bases[k]
    eta=weight(data.get('mean_multiplier','0'))
    if eta:
        m=F(data['mean_abs_max']);error=F(data['mean_error_upper'])
        need(0<=m<=1 and error>=F(1,12),'sharp periodic Lipschitz mean error constant')
        for i in range(n):
            for j in range(n):G[i][j]+=eta*i*j*a*a
        lower-=eta*(error+(m/a)**2)
    def qweights(k):
        k%=N;out=[F(0)]*n
        if k==0:out[0]=1;out[N]=2
        else:out[k]+=1;out[N-k]+=1
        return out
    def wide(k,d):
        out=[F(0)]*n
        for j in range(1-d,d):
            w=F(d-abs(j),d*d)
            for i,z in enumerate(qweights(d*k+j)):out[i]+=w*z
        return out
    for row in data.get('circle_rows',[]):
        k,d=row['k'],row['distance'];need(type(k)==type(d)==int and 0<=k<N and 2<=d<=100,'circle indices')
        w=weight(row['multiplier']);last,first,second=wide(k,d),wide(k,1),wide(k,d-1)
        if row['kind']=='lower':coeff=[z-x-y for z,x,y in zip(last,first,second)];rhs=F(0)
        elif row['kind']=='perimeter':coeff=[z+x+y for z,x,y in zip(last,first,second)];rhs=F(2)
        else:raise ValueError('circle kind')
        for i,z in enumerate(coeff):diagonal(i,-a*w*z/4)
        lower-=w*(rhs-sum((z*b for z,b in zip(coeff,bases)),F(0)))
    signs_allowed={(1,1,-1),(1,-1,1),(-1,1,1),(-1,-1,-1)}
    for row in data.get('triangle_rows',[]):
        positions=row['positions'];signs=tuple(row['signs'])
        need(len(positions)==3 and all(type(i)==int for i in positions) and 0<=positions[0]<positions[1]<positions[2]<n,'triangle positions')
        need(signs in signs_allowed,'triangle signs');i,j,k=positions;w=weight(row['multiplier'])
        entry(i,j,w*signs[0]);entry(j,k,w*signs[1]);entry(i,k,w*signs[2]);lower-=w
    return G,lower

def restricted(G):
    n=len(G);return [[G[i][j]-G[i][-1]-G[-1][j]+G[-1][-1] for j in range(n-1)] for i in range(n-1)]

def positive_definite(matrix):
    n=len(matrix);den=math.lcm(*(x.denominator for row in matrix for x in row))
    A=[[x.numerator*(den//x.denominator) for x in row] for row in matrix]
    previous=1;pivot_bits=[]
    for k in range(n):
        pivot=A[k][k]
        if pivot<=0:return False,{'first_nonpositive_leading_minor':k+1,'dimension':n}
        pivot_bits.append(pivot.bit_length())
        if k==n-1:break
        for i in range(k+1,n):
            for j in range(i,n):
                numerator=A[i][j]*pivot-A[i][k]*A[k][j]
                value,remainder=divmod(numerator,previous)
                if remainder:raise ArithmeticError('Bareiss division not exact')
                A[i][j]=A[j][i]=value
        previous=pivot
    return True,{'dimension':n,'positive_leading_principal_minors':n,'maximum_minor_bits':max(pivot_bits),
                 'method':'integer Bareiss elimination and Sylvester criterion; no floating eigenvalues'}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('certificate',type=Path);ap.add_argument('--target',required=True)
    ap.add_argument('--out',type=Path,required=True);args=ap.parse_args();start=time.time()
    data=json.loads(args.certificate.read_text(encoding='utf-8'));G,lower=compile_dual(data)
    pd,stats=positive_definite(restricted(G));target=F(args.target)
    functional=data['schema']=='phase-gram-functional-v2'
    result={'passed':pd and lower>target,'scope':('conditional linear overlap functional inequality; NOT a bound on mu' if functional else 'central mean interval only; analytic phase-average/box premises in PHASE_GRAM_PROOF.md'),
        'mean_abs_max':data['mean_abs_max'],'target':args.target,'lower_bound_exact':str(lower),
        'lower_bound_float_display':float(lower),'restricted_psd_check':stats,'elapsed':time.time()-start,
        'certificate_sha256':hashlib.sha256(args.certificate.read_bytes()).hexdigest(),
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    if functional:
        result['functional_lower_bound_exact']=result.pop('lower_bound_exact')
        result['functional_lower_float_display']=result.pop('lower_bound_float_display')
        result['functional_weights']=data['functional_weights']
    args.out.write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result,indent=2),flush=True)
    if not result['passed']:raise SystemExit(1)
if __name__=='__main__':main()
