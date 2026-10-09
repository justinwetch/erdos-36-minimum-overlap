"""Exact fractional-cut scores from packed anchors and affine knot formulas."""
import argparse,hashlib,json,time
from fractions import Fraction as F
from pathlib import Path
from exact_packed_correlations import convolve,verify as uniform_verify

def anchors(a,D):
    n=len(a)
    def correlation(values):
        c=convolve([D-v for v in values],values[::-1]);m=len(values)-1
        return c[m:]+[0],c[m::-1]+[0]
    p0,m0=correlation(a);half=[a[0]]+[v for value in a[1:] for v in (value,value)]+[a[0]]
    ph,mh=correlation(half);p1,m1=correlation(a[1:]+a[:1])
    def assemble(p,m,which):
        if which==0:part=lambda q:q+q[:-1]+q[1:]
        elif which==1:part=lambda q:q[::2]+q[1::2]+q[1::2]
        else:part=lambda q:q+q[1:]+q[:-1]
        scale=1 if which==1 else 2
        return [scale*v for v in part(p)+part(m)]
    return [assemble(p0,m0,0),assemble(ph,mh,1),assemble(p1,m1,2)]

def score(a,D,v,prepared=None):
    if not 0<=v<=1:raise ValueError('one-cell fraction')
    values=anchors(a,D) if prepared is None else prepared;half=0 if v<F(1,2) else 1;theta=2*v-half
    p,q=theta.numerator,theta.denominator
    peak=max((q-p)*x+p*y for x,y in zip(values[half],values[half+1]))
    return F(peak,len(a)*D*D*q)

def candidate(a,D,integer,v):
    n=len(a);k=integer%n;a=a[k:]+a[:k];B=n*v.denominator
    edges=[F(0)]+[F(2*i,n)-2*v/n for i in range(1,n+1)]+[F(2)]
    values=[a[0]]+a[1:]+[a[0]];heights=[];ends=[0]
    for i,height in enumerate(values):
        if edges[i+1]>edges[i]:heights.append(height);ends.append(int(edges[i+1]*B))
    return {'numerators':heights,'height_denominator':D,'edges':ends,'edge_denominator':B,
        'integer_cut':integer,'fractional_cell_cut':str(v)}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('witness',type=Path);ap.add_argument('discovery',type=Path);ap.add_argument('--name',required=True)
    args=ap.parse_args();start=time.time();data=json.loads(args.witness.read_text());discovery=json.loads(args.discovery.read_text())
    if discovery['witness_sha256']!=hashlib.sha256(args.witness.read_bytes()).hexdigest():raise ValueError('discovery input changed')
    baseline=F(uniform_verify(data)['score_fraction']);a=data['numerators'];D=data['denominator'];records=[];best=(baseline,0,F(0));cache={}
    for row in discovery['records']:
        integer=row['integer_cut'];v=F(row['fraction']);k=integer%len(a);shifted=a[k:]+a[:k]
        if k not in cache:cache[k]=anchors(shifted,D)
        value=score(shifted,D,v,cache[k]);records.append({'integer_cut':integer,'fraction':str(v),'score_exact':str(value),'gain_exact':str(baseline-value)})
        if value<best[0]:best=(value,integer,v)
    root=Path(__file__).resolve().parent;run=root/'runs'/args.name;run.mkdir(parents=True,exist_ok=True)
    witness=candidate(a,D,best[1],best[2]);witness['source_sha256']=hashlib.sha256(args.witness.read_bytes()).hexdigest()
    (run/'best.json').write_text(json.dumps(witness,indent=2),encoding='utf-8');q=best[0];scale=10**25;lo=q.numerator*scale//q.denominator
    result={'status':'PASS','scope':'exact continuous scores of listed fractional cuts via finite knot families and positive polynomial packing; independent nonuniform replay still required',
        'baseline_exact':str(baseline),'score_exact':str(q),'gain_exact':str(baseline-q),'gain_float_display':float(baseline-q),
        'decimal_upper_strict':f'{(lo+1)//scale}.{(lo+1)%scale:025d}','integer_cut':best[1],'fraction':str(best[2]),
        'knot_families_checked':2*(3*len(a)+1),'records':records,'elapsed':time.time()-start,
        'witness_sha256':hashlib.sha256(args.witness.read_bytes()).hexdigest(),'discovery_sha256':hashlib.sha256(args.discovery.read_bytes()).hexdigest(),
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'packed_checker_sha256':hashlib.sha256(Path(__file__).with_name('exact_packed_correlations.py').read_bytes()).hexdigest()}
    (run/'verification.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
