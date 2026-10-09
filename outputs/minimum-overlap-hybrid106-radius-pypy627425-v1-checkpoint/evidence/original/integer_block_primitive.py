"""Outward interval primitives through short exact trigonometric recurrences.

This is an isolated arithmetic helper. Existing proof campaigns continue
to use their unchanged direct evaluator. Addition identities plus outward
interval operations enclose each value; blocks reset from direct sincos.
"""
import argparse,hashlib,json,time
from fractions import Fraction as F
from pathlib import Path
from verify_integer_circle import I,SCALE,sincos
class BlockPrimitive:
    def __init__(self,checker,grid,block=64):
        assert type(grid)==int and grid>0 and type(block)==int and 1<=block<=256
        self.checker=checker;self.grid=grid;self.block=block;self.cache={};self.steps=[sincos(t[0]*I(F(1,grid))) for t in checker.terms];self.blocks=0;self.fallback=0;self.maximum_width=0
    def __call__(self,x):
        x=F(x)
        if x in self.cache:return self.cache[x]
        k=x*self.grid
        if k.denominator!=1 or not 0<=k<=2*self.grid:
            self.fallback+=1;v=self.checker.primitive(x);self.cache[x]=v;return v
        k=int(k);start=k//self.block*self.block;stop=min(2*self.grid+1,start+self.block);xs=[F(j,self.grid) for j in range(start,stop)];values=[]
        for t in map(I,xs):values.append(self.checker.constant*t+I(self.checker.linear)*t*t/2+I(self.checker.quadratic)*t*t*t/3)
        for term,(sd,cd) in zip(self.checker.terms,self.steps):
            xi,*_=term;adiv,bdiv=term[-2:];s,c=sincos(xi*I(xs[0]))
            for j in range(len(xs)):
                values[j]+=adiv*s-bdiv*c
                s,c=s*cd+c*sd,c*cd-s*sd
        for t,v in zip(xs,values):
            self.maximum_width=max(self.maximum_width,v.hi-v.lo);assert v.hi-v.lo<SCALE//10**30,'recurrence interval too wide';self.cache[t]=v
        self.blocks+=1;return self.cache[x]
def controls():
    class Fixture:
        def __init__(self,trig=True):
            from verify_integer_hybrid_outer_blend import compiled_terms
            self.constant=I(F(2,7));self.linear=F(-3,11);self.quadratic=F(5,13)
            self.terms=compiled_terms({F(1,3):(F(2,5),F(-3,7)),F(999,7):(F(-1,11),F(1,17))})[0] if trig else []
        def primitive(self,x):
            t=I(x);v=self.constant*t+I(self.linear)*t*t/2+I(self.quadratic)*t*t*t/3
            for term in self.terms:
                s,c=sincos(term[0]*t);v+=term[-2]*s-term[-1]*c
            return v
    exact=0;overlap=0
    for block in [1,7,64]:
        f=Fixture(False);b=BlockPrimitive(f,128,block)
        for k in range(257):
            x=F(k,128);want=F(2,7)*x+F(-3,22)*x*x+F(5,39)*x*x*x;v=b(x);assert F(v.lo,SCALE)<=want<=F(v.hi,SCALE);exact+=1
        f=Fixture();b=BlockPrimitive(f,128,block)
        for k in range(257):
            x=F(k,128);a=b(x);v=f.primitive(x);assert a.lo<=v.hi and v.lo<=a.hi;overlap+=1
        x=F(5,19);v=b(x);w=f.primitive(x);assert v.lo==w.lo and v.hi==w.hi and b.fallback==1
    return {'status':'PASS','exact_polynomial_values':exact,'direct_trigonometric_overlap_values':overlap,'nonuniform_fallback_fixtures':3,'scope':'exact polynomial containment and independent direct-evaluator consistency; recurrence containment follows from addition identities and outward arithmetic'}
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();r=controls();r['implementation_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest();a.out.write_text(json.dumps(r,indent=2),encoding='utf-8');print(json.dumps(r))
if __name__=='__main__':main()
