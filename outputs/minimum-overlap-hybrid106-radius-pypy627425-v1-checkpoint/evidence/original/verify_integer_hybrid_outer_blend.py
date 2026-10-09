"""Independent blend parser and full-line dyadic integration, standard library."""
import argparse,hashlib,json,math,time
from pathlib import Path
from fractions import Fraction as F
from verify_integer_hybrid import HybridChecker
from verify_integer_circle import I,SCALE,sincos


def sqrt_nonnegative(x):
    if x.hi<0:raise ValueError('negative square-root interval')
    lo=math.isqrt(max(0,x.lo)*SCALE);v=max(0,x.hi)*SCALE;hi=math.isqrt(v)
    if hi*hi<v:hi+=1
    return I.raw(lo,hi)


def outer_rhs(row,lo,hi):
    k,p=row['kind'],row.get('param');max2=max(lo*lo,hi*hi);min2=0 if lo<=0<=hi else min(lo*lo,hi*hi)
    if k=='t':return I(hi)
    if k=='-t':return I(-lo)
    if k=='t2':return I(F(2,3)+max2/2)
    if k=='-t2':return I(-F(2,3)-min2/2)
    if k not in {'cos','-cos','sin','-sin','cos+asin'}:raise ValueError('outer kind')
    xi=F(p[0] if k=='cos+asin' else p)
    if not xi:raise ValueError('zero frequency')
    s,_=sincos(I(xi));s=s/I(xi);s2=s*s
    if k=='cos':return s2
    if k=='-cos':return 1-2*s2
    if k=='cos+asin':return I(1+F(p[1])**2)*s2
    return 2*I.raw(0,s.abs_upper())*sqrt_nonnegative(1-s2)


def compiled_terms(rows):
    terms=[];M4=F(0)
    for xi,(a,b) in sorted(rows.items()):
        if not a and not b:continue
        terms.append(tuple(map(I,(xi,a,b,a*xi,b*xi,a*xi**2,b*xi**2,a*xi**3,b*xi**3,a/xi,b/xi))))
        M4+=(abs(a)+abs(b))*xi**4
    return terms,I(M4)


class BlendChecker:
    def __init__(self,data):
        if data['schema']!='hybrid-outer-blend-v1':raise ValueError('schema')
        theta,ell=F(data['theta_outer']),F(data['hybrid_numerator_lower'])
        if not 0<=theta<=1 or ell<=0:raise ValueError('blend weights')
        h,o=data['hybrid'],data['outer'];lo,hi=F(o['lo']),F(o['hi'])
        if not -1<=lo<=hi<=1:raise ValueError('mean bin')
        old=HybridChecker(h,max(abs(lo),abs(hi)))
        if old.L.lo<I(ell).hi:raise ValueError('unproved hybrid normalization')
        hs=(1-theta)/ell;self.constant=I(hs*F(h['y0'])+theta);self.linear=F(0);self.quadratic=hs*F(h['y2'])
        rows={}
        def add(xi,a,b):
            previous=rows.get(xi,(F(0),F(0)));rows[xi]=(previous[0]+a,previous[1]+b)
        for row in h['cos']:add(F(row['xi']),hs*F(row['z']),F(0))
        for row in o['active']:
            lam=F(row['lambda'])
            if lam<0:raise ValueError('negative outer multiplier')
            k,p=row['kind'],row.get('param');weight=theta*lam;B=outer_rhs(row,lo,hi)
            self.constant+=I(weight)*B
            if k=='t':self.linear-=weight
            elif k=='-t':self.linear+=weight
            elif k=='t2':self.quadratic-=weight
            elif k=='-t2':self.quadratic+=weight
            elif k in {'cos','-cos','sin','-sin'}:
                xi=F(p);a=-weight if k=='cos' else weight if k=='-cos' else F(0)
                b=-weight if k=='sin' else weight if k=='-sin' else F(0);add(xi,a,b)
            elif k=='cos+asin':add(F(p[0]),-weight,-weight*F(p[1]))
            else:raise ValueError('outer kind')
        self.terms,self.M4=compiled_terms(rows);self.parts=[]
        for left,right,constant,slope in old.parts:
            self.parts.extend([(left,right,hs*constant,hs*slope),(-right,-left,hs*constant,-hs*slope)])
        self.parts.sort()
        assert self.parts[0][0]==-2 and self.parts[-1][1]==2 and all(a[1]==b[0] for a,b in zip(self.parts,self.parts[1:]))
        self.premises=old.premises;self.numerator=old.L;self.bin=(lo,hi);self.cache={}

    def jet(self,x):
        t=I(x);q=self.constant+I(self.linear)*t+I(self.quadratic)*t*t
        q1=I(self.linear)+2*I(self.quadratic)*t;q2=2*I(self.quadratic);q3=I(0)
        for xi,a,b,a1,b1,a2,b2,a3,b3,_,_ in self.terms:
            s,c=sincos(xi*t);q+=a*c+b*s;q1+=-a1*s+b1*c;q2+=-a2*c-b2*s;q3+=a3*s-b3*c
        return q,q1,q2,q3

    def primitive(self,x):
        if x in self.cache:return self.cache[x]
        t=I(x);v=self.constant*t+I(self.linear)*t*t/2+I(self.quadratic)*t*t*t/3
        for xi,_,_,_,_,_,_,_,_,adiv,bdiv in self.terms:
            s,c=sincos(xi*t);v+=adiv*s-bdiv*c
        self.cache[x]=v;return v

    def verify(self,width,target,limit=2000000):
        start=time.time();total=nodes=pos=neg=amb=0
        for index,(left,right,constant,slope) in enumerate(self.parts):
            shift,sl=I(constant),I(slope);stack=[(left,right)]
            while stack:
                a,b=stack.pop();c=(a+b)/2;r=I((b-a)/2);q,q1,q2,q3=self.jet(c)
                q+=shift+sl*I(c);q1+=sl
                radius=I.raw(q1.abs_upper(),q1.abs_upper())*r+I.raw(q2.abs_upper(),q2.abs_upper())*r*r/2
                radius+=I.raw(q3.abs_upper(),q3.abs_upper())*r*r*r/6+self.M4*r*r*r*r/24
                hi=q.hi+radius.hi;lo=q.lo-radius.hi;nodes+=1
                if nodes>limit:raise RuntimeError('node budget')
                if hi<=0:neg+=1;continue
                if lo>=0:
                    v=self.primitive(b)-self.primitive(a)+shift*I(b-a)+sl*I((b*b-a*a)/2)
                    if v.hi<0:raise ArithmeticError('negative positive-piece integral')
                    total+=max(0,v.hi);pos+=1
                elif b-a<=width:
                    total+=(I(b-a)*I.raw(max(0,hi),max(0,hi))).hi;amb+=1
                else:stack.extend(((a,c),(c,b)))
            if index%100==0:print(json.dumps({'piece':index,'pieces':len(self.parts),'nodes':nodes,'elapsed':time.time()-start}),flush=True)
        D=F(total,SCALE);lower=1/D if D>0 else None
        return {'passed':lower is not None and lower>target,'scope':'single mean bin only, independent standard-library blend compiler and dyadic integration',
                'mean_bin':list(map(str,self.bin)),'target':str(target),'positive_integral_upper_exact':str(D),
                'lower_bound_exact':str(lower),'lower_bound_float_display':float(lower) if lower else None,
                'hybrid_numerator_interval':self.numerator.as_strings(),'functional_premises':self.premises,
                'nodes':nodes,'positive':pos,'negative':neg,'ambiguous':amb,'pieces':len(self.parts),'elapsed':time.time()-start}


def controls():
    for x in [0,1,2,4,F(1,9),F(7,13)]:
        v=sqrt_nonnegative(I(x));assert v.lo**2<=I(x).hi*SCALE and v.hi**2>=I(x).lo*SCALE
    count=0
    for x in map(F,['-.9','0','.7']):
        o=object.__new__(BlendChecker);o.constant=I(F(2,3));o.linear=F(-3,5);o.quadratic=F(7,9);o.terms=[];o.cache={}
        j=o.jet(x);exact=(F(2,3)-F(3,5)*x+F(7,9)*x*x,-F(3,5)+F(14,9)*x,F(14,9),F(0))
        assert all(a.lo<=I(b).lo<=I(b).hi<=a.hi for a,b in zip(j,exact));count+=1
    return {'status':'PASS','rational_polynomial_jets':count,'sqrt_enclosure_fixtures':6,
            'scope':'independent polynomial and square-root arithmetic fixtures; sine/cosine arithmetic shared with existing integer checker'}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('certificate',type=Path);ap.add_argument('--target',required=True)
    ap.add_argument('--width',default='1e-7');ap.add_argument('--out',type=Path,required=True);args=ap.parse_args();start=time.time()
    target,width=F(args.target),F(args.width)
    if target<=0 or width<=0:raise ValueError('parameters')
    checked=controls();data=json.loads(args.certificate.read_text());result=BlendChecker(data).verify(width,target)
    result.update({'controls':checked,'total_elapsed':time.time()-start,'certificate_sha256':hashlib.sha256(args.certificate.read_bytes()).hexdigest(),
                   'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'width':args.width})
    result['implementation_hashes']={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
        for name in ['verify_integer_hybrid.py','verify_integer_hypermetric.py','verify_integer_circle.py','hybrid_functionals.py','verify_phase_gram.py']}
    args.out.write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in result.items() if k!='functional_premises'}),flush=True)
    if not result['passed']:raise SystemExit(1)

if __name__=='__main__':main()
