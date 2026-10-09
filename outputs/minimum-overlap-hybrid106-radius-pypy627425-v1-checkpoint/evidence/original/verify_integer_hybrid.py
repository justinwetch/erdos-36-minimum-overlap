"""Integer-only continuous verification of the hybrid schema-v5 dual."""
import argparse,hashlib,json,time
from fractions import Fraction as F
from pathlib import Path
from verify_integer_hypermetric import GeneralChecker
from verify_integer_circle import I,SCALE
from hybrid_functionals import validate,knots,affine

class HybridChecker(GeneralChecker):
    def __init__(self,data,mean):
        super().__init__(dict(data,schema=data['base_schema']))
        functions,self.premises=validate(data,mean);baseparts=self.parts
        coefficient=self.y2F/2
        for f in functions:
            self.L+=I(f['mu']*f['L0']);coefficient+=f['mu']*f['mean_coefficient']
        self.L+=I(min(F(0),coefficient)*mean*mean);self.coefficient=coefficient
        boundaries=sorted(knots(functions)|{v for left,right,_ in baseparts for v in (left,right)})
        parts=[];index=0
        for left,right in zip(boundaries,boundaries[1:]):
            center=(left+right)/2
            while baseparts[index][1]<=center:index+=1
            assert baseparts[index][0]<=center<baseparts[index][1]
            u,v=affine(functions,center);parts.append((left,right,baseparts[index][2]+u,v))
        self.parts=parts

    def verify_hybrid(self,width,mean,target,limit):
        start=time.time();total=0;nodes=pos=neg=amb=0
        for index,(left,right,constant,slope) in enumerate(self.parts):
            shift,sl=I(constant),I(slope);stack=[(left,right)]
            while stack:
                a,b=stack.pop();c=(a+b)/2;r=I((b-a)/2)
                q,q1,q2,q3=self.jet(c);q+=shift+sl*I(c);q1+=sl
                radius=I.raw(q1.abs_upper(),q1.abs_upper())*r
                radius+=I.raw(q2.abs_upper(),q2.abs_upper())*r*r/2
                radius+=I.raw(q3.abs_upper(),q3.abs_upper())*r*r*r/6+self.M4*r*r*r*r/24
                hi=q.hi+radius.hi;lo=q.lo-radius.hi;nodes+=1
                if nodes>limit:raise RuntimeError('node budget')
                if hi<=0:neg+=1;continue
                if lo>=0:
                    integral=self.primitive(b)-self.primitive(a)+shift*I(b-a)+sl*I((b*b-a*a)/2)
                    if integral.hi<0:raise ArithmeticError('negative positive-piece integral')
                    total+=max(0,integral.hi);pos+=1
                elif b-a<=width:
                    total+=(I(b-a)*I.raw(max(0,hi),max(0,hi))).hi;amb+=1
                else:stack.extend(((a,c),(c,b)))
            if index%25==0:print(json.dumps({'piece':index,'pieces':len(self.parts),'nodes':nodes,'elapsed':time.time()-start}),flush=True)
        D=F(2*total,SCALE);lower=F(self.L.lo,SCALE)/D if D>0 else None
        return {'passed':lower is not None and self.L.lo>0 and lower>target,'scope':'central interval only; no global mean cover',
            'implementation':'standard-library rational PSD and dyadic trigonometric arithmetic',
            'mean_abs_max':str(mean),'target':str(target),'lower_bound_exact':str(lower),'lower_bound_float_display':float(lower) if lower else None,
            'numerator_interval':self.L.as_strings(),'positive_integral_upper_exact':str(D),
            'mean_square_coefficient_exact':str(self.coefficient),'nodes':nodes,'positive':pos,'negative':neg,'ambiguous':amb,
            'pieces':len(self.parts),'width':str(width),'elapsed':time.time()-start,'functional_premises':self.premises}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('certificate',type=Path);ap.add_argument('--mean',default='0');ap.add_argument('--target',required=True)
    ap.add_argument('--width',default='1e-7');ap.add_argument('--node-limit',type=int,default=1000000);ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();width,mean,target=map(F,(args.width,args.mean,args.target))
    if width<=0 or target<=0 or not 0<=mean<=1:raise ValueError('parameters')
    data=json.loads(args.certificate.read_text(encoding='utf-8'));result=HybridChecker(data,mean).verify_hybrid(width,mean,target,args.node_limit)
    result['certificate_sha256']=hashlib.sha256(args.certificate.read_bytes()).hexdigest()
    result['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result['implementation_hashes']={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
        for name in ('hybrid_functionals.py','verify_phase_gram.py','verify_integer_hypermetric.py','verify_integer_circle.py')}
    args.out.write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result),flush=True)
    if not result['passed']:raise SystemExit(1)
if __name__=='__main__':main()
