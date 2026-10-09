"""Exact adversarial controls for coefficient packing and upper-score mapping."""
import argparse,hashlib,json,random
from pathlib import Path
from exact_packed_correlations import convolve,verify
from exact_verify import verify as direct_verify

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);args=ap.parse_args();rng=random.Random(540813);count=0
    for n in (1,2,3,7,16,31):
        for m in (1,2,5,19):
            for bits in (0,1,8,64,130):
                a=[rng.getrandbits(bits) for _ in range(n)];b=[rng.getrandbits(bits) for _ in range(m)]
                expected=[sum(a[i]*b[k-i] for i in range(n) if 0<=k-i<m) for k in range(n+m-1)]
                assert convolve(a,b)==expected;count+=len(expected)
    for n in (2,4,8,16,32):
        for D in (1,7,10**17+3):
            half=[rng.randrange(D+1) for _ in range(n//2)];a=half+[D-v for v in half];rng.shuffle(a)
            data={'numerators':a,'denominator':D};fast=verify(data);slow=direct_verify(data)
            assert fast['score_fraction']==slow['score_fraction'] and fast['argmax_lags']==slow['argmax_lags'];count+=2*n-1
    for a,b in (([],[1]),([1],[]),([-1],[1]),([1],[.5])):
        try:convolve(a,b)
        except ValueError:count+=1
        else:raise AssertionError('invalid coefficient accepted')
    result={'status':'PASS','fixtures':count,'scope':'exact coefficient controls across sizes and bit lengths; balanced witnesses compared with unchanged direct checker',
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'implementation_hashes':{name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in ('exact_packed_correlations.py','exact_verify.py')}}
    args.out.write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
