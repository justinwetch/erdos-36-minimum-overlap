"""Compare the packed affine score with independent literal nonuniform checks."""
import argparse,hashlib,json,random
from fractions import Fraction as F
from pathlib import Path
from exact_fractional_rotation import anchors,score,candidate
from nonuniform import verify_nonuniform

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);args=ap.parse_args();rng=random.Random(194065);count=0
    for n in (2,4,6,8):
        for D in (1,7,13,10**17+3):
            half=[rng.randrange(D+1) for _ in range(n//2)];a=half+[D-v for v in half];rng.shuffle(a)
            for integer in (-1,0,1):
                k=integer%n;shifted=a[k:]+a[:k];prepared=anchors(shifted,D)
                for v in (F(0),F(1,8),F(1,2),F(7,8),F(1),F(1,10**23)):
                    expected=verify_nonuniform(candidate(a,D,integer,v));actual=score(shifted,D,v,prepared)
                    assert actual==F(expected['score_fraction']);count+=1
    result={'status':'PASS','fixtures':count,'scope':'exact fractional-cut scores, mass and all shift knots compared with unchanged nonuniform checker across sizes, bit lengths and endpoint/tiny cuts',
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'implementation_hashes':{name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in ('exact_fractional_rotation.py','exact_packed_correlations.py','nonuniform.py')}}
    args.out.write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
