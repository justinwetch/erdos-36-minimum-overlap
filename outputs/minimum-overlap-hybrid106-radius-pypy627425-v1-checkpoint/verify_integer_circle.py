"""Independent integer-only enclosure of a schema-v1 central certificate.

Uses Python integers/Fraction, Taylor sine/cosine with halving and doubling,
and a separately implemented exact periodic-step compiler. No NumPy, Arb,
source parser, floating root finder, or optimization package is imported.
The analytic universal inequalities remain mathematical premises.
"""
import argparse, hashlib, json, math, time
from fractions import Fraction as F
from pathlib import Path

BITS=192
SCALE=1<<BITS

def ceildiv(a,b):
    assert b>0
    return -((-a)//b)

class I:
    __slots__=('lo','hi')
    def __init__(self,x=0,hi=None,raw=False):
        if raw:
            self.lo=x; self.hi=hi
        elif isinstance(x,I):
            self.lo=x.lo; self.hi=x.hi
        else:
            x=F(x); self.lo=(x.numerator*SCALE)//x.denominator
            self.hi=ceildiv(x.numerator*SCALE,x.denominator)
    @staticmethod
    def raw(lo,hi):
        assert lo<=hi
        return I(lo,hi,True)
    def __add__(a,b):
        if not isinstance(b,I): b=I(b)
        return I.raw(a.lo+b.lo,a.hi+b.hi)
    __radd__=__add__
    def __neg__(a): return I.raw(-a.hi,-a.lo)
    def __sub__(a,b): return a+-I(b)
    def __rsub__(a,b): return I(b)+-a
    def __mul__(a,b):
        if not isinstance(b,I): b=I(b)
        v=(a.lo*b.lo,a.lo*b.hi,a.hi*b.lo,a.hi*b.hi)
        return I.raw(min(v)//SCALE,ceildiv(max(v),SCALE))
    __rmul__=__mul__
    def __truediv__(a,b):
        if isinstance(b,int) and b>0:
            return I.raw(a.lo//b,ceildiv(a.hi,b))
        if not isinstance(b,I): b=I(b)
        if b.lo<=0<=b.hi: raise ValueError('zero in divisor')
        if b.hi<0: return (-a)/(-b)
        return a*I.raw((SCALE*SCALE)//b.hi,ceildiv(SCALE*SCALE,b.lo))
    def abs_upper(a): return max(abs(a.lo),abs(a.hi))
    def as_strings(a):
        return [str(F(a.lo,SCALE)),str(F(a.hi,SCALE))]

def sincos(x):
    x=I(x); k=0
    while x.abs_upper()>SCALE//8:
        x=x/2; k+=1
    x2=x*x; c=I(1); s=I(x); ct=I(1); st=I(x)
    for j in range(1,25):
        ct=-(ct*x2)/((2*j-1)*(2*j)); c=c+ct
        st=-(st*x2)/((2*j)*(2*j+1)); s=s+st
    # Lagrange remainders: |x|<=1/8, and all real sin/cos derivatives <=1.
    ec=I(F(1,8**50*math.factorial(50))).hi
    es=I(F(1,8**51*math.factorial(51))).hi
    c=I.raw(c.lo-ec,c.hi+ec); s=I.raw(s.lo-es,s.hi+es)
    for _ in range(k):
        s,c=2*s*c,c*c-s*s
    return s,c

def compile_steps(data):
    if data['schema']!='periodic-triangle-dual-v1': raise ValueError('schema v1 required')
    n=data['cells']
    if type(n)!=int or n<2 or n&(n-1): raise ValueError('power-of-two cells required')
    low=list(map(F,data['low'])); high=list(map(F,data['high']))
    if len(low)!=n or len(high)!=n or any(v>0 for v in low+high): raise ValueError('circle rows')
    h=F(2,n); direct=[F(0)]*n
    for i in range(n):
        direct[i]+=(-2*low[i]+2*high[i])/h
        for j in (2*i%n,(2*i+1)%n): direct[j]+=(low[i]+high[i])/(2*h)
    steps=[(direct[i]+direct[n-1-i])/2 for i in range(n)]
    parts=[]
    for i,v in enumerate(steps):
        if parts and parts[-1][2]==v: parts[-1]=(parts[-1][0],h*(i+1),v)
        else: parts.append((h*i,h*(i+1),v))
    return parts,2*sum(high)

class Checker:
    def __init__(self,data):
        self.parts,B=compile_steps(data)
        self.y0=I(data['y0']); self.y2=I(data['y2']); self.y2F=F(data['y2'])
        self.terms=[]; self.L=self.y0+self.y2*I(F(2,3))+I(B)
        M4=F(0)
        for row in data['cos']:
            z,xi=F(row['z']),F(row['xi'])
            if z>0 or not xi: raise ValueError('cosine row')
            zz,xx=I(z),I(xi); ss,_=sincos(xx); ratio=ss/xx
            self.L=self.L+zz*ratio*ratio
            self.terms.append((zz,xx,zz*xx,zz*xx*xx,zz*xx*xx*xx,zz/xx))
            M4+=abs(z)*xi**4
        self.M4=I(M4); self.cache={}
    def jet(self,c):
        c=I(c); q=self.y0+self.y2*c*c; q1=2*self.y2*c
        q2=2*self.y2; q3=I(0)
        for z,xi,z1,z2,z3,_ in self.terms:
            s,co=sincos(xi*c)
            q=q+z*co; q1=q1-z1*s; q2=q2-z2*co; q3=q3+z3*s
        return q,q1,q2,q3
    def primitive(self,x):
        if x in self.cache: return self.cache[x]
        t=I(x); value=self.y0*t+self.y2*t*t*t/3
        for _,xi,_,_,_,zdiv in self.terms:
            s,_=sincos(xi*t); value=value+zdiv*s
        self.cache[x]=value
        return value
    def verify(self,width,mean,target,out,limit):
        started=time.time(); total=0; nodes=pos=neg=amb=0
        for index,(a,b,step) in enumerate(self.parts):
            shift=I(step); stack=[(a,b)]
            while stack:
                a,b=stack.pop(); c=(a+b)/2; r=I((b-a)/2)
                q,q1,q2,q3=self.jet(c); q=q+shift
                radius=I.raw(q1.abs_upper(),q1.abs_upper())*r
                radius=radius+I.raw(q2.abs_upper(),q2.abs_upper())*r*r/2
                radius=radius+I.raw(q3.abs_upper(),q3.abs_upper())*r*r*r/6
                radius=radius+self.M4*r*r*r*r/24
                lo=q.lo-radius.hi; hi=q.hi+radius.hi; nodes+=1
                if nodes>limit: raise RuntimeError('node budget exceeded')
                if hi<=0: neg+=1; continue
                if lo>=0:
                    integral=self.primitive(b)-self.primitive(a)+shift*I(b-a)
                    if integral.hi<0: raise ArithmeticError('negative positive-piece integral')
                    total+=max(0,integral.hi); pos+=1
                elif b-a<=width:
                    total+=(I(b-a)*I.raw(max(0,hi),max(0,hi))).hi; amb+=1
                else:
                    stack.extend(((a,c),(c,b)))
            if index%25==0:
                print(json.dumps({'piece':index,'pieces':len(self.parts),'nodes':nodes,'elapsed':time.time()-started}),flush=True)
        D=F(2*total,SCALE)
        L=self.L+self.y2*I(mean*mean/2) if self.y2F<0 else self.L
        lower=F(L.lo,SCALE)/D if D>0 else None
        result={'passed':lower is not None and L.lo>0 and lower>target,'scope':'central mean case only; universal analytic inequalities are premises',
                'implementation':'Python integer dyadic intervals; no external math packages',
                'precision_bits':BITS,'mean_abs_max':str(mean),'target':str(target),
                'numerator_interval':L.as_strings(),'positive_integral_upper_exact':str(D),
                'lower_bound_exact':str(lower) if lower is not None else None,'lower_bound_float_display':float(lower) if lower is not None else None,
                'nodes':nodes,'positive':pos,'negative':neg,'ambiguous':amb,'pieces':len(self.parts),
                'width':str(width),'elapsed':time.time()-started}
        out.write_text(json.dumps(result,indent=2),encoding='utf-8'); return result

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('certificate',type=Path); ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--mean',default='.002038866657'); ap.add_argument('--target',default='.38056559')
    ap.add_argument('--width',default='1e-7'); ap.add_argument('--node-limit',type=int,default=1000000)
    args=ap.parse_args(); data=json.loads(args.certificate.read_text(encoding='utf-8'))
    width,mean,target=map(F,(args.width,args.mean,args.target))
    if width<=0 or mean<0 or mean>1 or target<=0: raise ValueError('invalid target parameters')
    checker=Checker(data); result=checker.verify(width,mean,target,args.out,args.node_limit)
    result['certificate_sha256']=hashlib.sha256(args.certificate.read_bytes()).hexdigest()
    result['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    args.out.write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result),flush=True)
    if not result['passed']: raise SystemExit(1)

if __name__=='__main__': main()
