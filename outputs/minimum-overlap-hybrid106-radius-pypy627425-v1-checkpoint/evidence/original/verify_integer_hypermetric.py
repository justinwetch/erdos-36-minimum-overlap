"""Independent rational compiler and integer enclosure for schema-v2.

Shares only the standard-library dyadic arithmetic and analytic integration
engine with verify_integer_circle.py. No Arb or numerical package is used.
"""
import argparse,hashlib,json,time
from fractions import Fraction as F
from pathlib import Path
from verify_integer_circle import Checker,I,sincos

def compile_families(data):
    if data['schema']!='periodic-hypermetric-dual-v2':raise ValueError('schema v2 required')
    n=data['cells']
    if type(n)!=int or n<2 or n&(n-1):raise ValueError('power-of-two cells required')
    h=F(2,n);direct=[F(0)]*n;B=F(0)
    for family in data['families']:
        positions,weights=family['positions'],family['b']
        if len(positions)!=len(weights) or not positions or len(set(positions))!=len(positions):raise ValueError('family dimensions')
        if any(type(v)!=int for v in positions+weights) or min(positions)<0:raise ValueError('integer positions and weights required')
        z=list(map(F,family['z']))
        if len(z)!=n or any(v>0 for v in z):raise ValueError('family multipliers')
        bound=sum(weights)**2//4;B+=bound*sum(z)
        pairs={}
        for i in range(len(positions)):
            for j in range(i+1,len(positions)):
                distance=abs(positions[i]-positions[j])
                pairs[distance]=pairs.get(distance,0)+weights[i]*weights[j]
        for cell,value in enumerate(z):
            if not value:continue
            for distance,coefficient in pairs.items():
                if not coefficient:continue
                amount=value*coefficient/(distance*h)
                for offset in range(distance):direct[(distance*cell+offset)%n]+=amount
    steps=[(direct[i]+direct[n-1-i])/2 for i in range(n)];parts=[]
    for i,value in enumerate(steps):
        if parts and parts[-1][2]==value:parts[-1]=(parts[-1][0],h*(i+1),value)
        else:parts.append((h*i,h*(i+1),value))
    return parts,B

class GeneralChecker(Checker):
    def __init__(self,data):
        self.parts,B=compile_families(data)
        self.y0=I(data['y0']);self.y2=I(data['y2']);self.y2F=F(data['y2'])
        self.terms=[];self.L=self.y0+self.y2*I(F(2,3))+I(B);M4=F(0)
        for row in data['cos']:
            z,xi=F(row['z']),F(row['xi'])
            if z>0 or not xi:raise ValueError('cosine row')
            zz,xx=I(z),I(xi);ss,_=sincos(xx);ratio=ss/xx
            self.L=self.L+zz*ratio*ratio
            self.terms.append((zz,xx,zz*xx,zz*xx*xx,zz*xx*xx*xx,zz/xx));M4+=abs(z)*xi**4
        self.M4=I(M4);self.cache={}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('certificate',type=Path);ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--mean',default='.002038866657');ap.add_argument('--target',default='.38056559')
    ap.add_argument('--width',default='1e-7');ap.add_argument('--node-limit',type=int,default=1000000)
    args=ap.parse_args();data=json.loads(args.certificate.read_text(encoding='utf-8'))
    width,mean,target=map(F,(args.width,args.mean,args.target))
    if width<=0 or mean<0 or mean>1 or target<=0:raise ValueError('invalid target parameters')
    result=GeneralChecker(data).verify(width,mean,target,args.out,args.node_limit)
    result['certificate_sha256']=hashlib.sha256(args.certificate.read_bytes()).hexdigest()
    result['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result['arithmetic_sha256']=hashlib.sha256((Path(__file__).parent/'verify_integer_circle.py').read_bytes()).hexdigest()
    args.out.write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result),flush=True)
    if not result['passed']:raise SystemExit(1)

if __name__=='__main__':main()
