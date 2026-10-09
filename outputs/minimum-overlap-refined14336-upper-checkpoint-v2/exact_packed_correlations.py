"""Exact nonnegative convolution through carry-free integer polynomial packing."""
import argparse,hashlib,json,time
from fractions import Fraction as F
from pathlib import Path

def convolve(a,b):
    if not a or not b or any(type(v)!=int or v<0 for v in a+b):raise ValueError('nonnegative integer coefficient lists required')
    bound=min(len(a),len(b))*max(a)*max(b);width=max(1,(bound.bit_length()+7)//8)
    left=int.from_bytes(b''.join(v.to_bytes(width,'little') for v in a),'little')
    right=int.from_bytes(b''.join(v.to_bytes(width,'little') for v in b),'little')
    raw=(left*right).to_bytes((len(a)+len(b)-1)*width,'little')
    return [int.from_bytes(raw[i:i+width],'little') for i in range(0,len(raw),width)]

def verify(data):
    start=time.time();a=data['numerators'];D=data['denominator'];n=len(a)
    if type(D)!=int or D<=0 or not n or any(type(v)!=int or not 0<=v<=D for v in a) or 2*sum(a)!=n*D:raise ValueError('mass or box')
    counts=convolve([D-v for v in a],a[::-1]);peak=max(counts);q=F(2*peak,n*D*D);scale=10**25;lo=q.numerator*scale//q.denominator
    return {'status':'PASS','scope':'exact uniform-step continuum supremum via nonnegative polynomial coefficients; no optimization claim',
        'cells':n,'shifts_checked':2*n-1,'mass':'1','box':'exact','score_fraction':str(q),
        'decimal_upper_strict':f'{(lo+1)//scale}.{(lo+1)%scale:025d}',
        'argmax_lags':[i-n+1 for i,v in enumerate(counts) if v==peak],'elapsed':time.time()-start}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('witness',type=Path);ap.add_argument('--out',type=Path,required=True);args=ap.parse_args()
    result=verify(json.loads(args.witness.read_text()));result['witness_sha256']=hashlib.sha256(args.witness.read_bytes()).hexdigest()
    result['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest();args.out.write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
