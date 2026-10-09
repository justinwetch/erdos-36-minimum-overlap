"""Retarget a fully checked fixed kernel through its exact mean polynomial.

All three existing integration reports are required. No quadrature score
or floating display is used; this is a conditional interval return only.
"""
import argparse,hashlib,json,re
from fractions import Fraction as F
from pathlib import Path
from shared_mean_numerator import coefficients,minimum,controls as polynomial_controls
R=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
NUMBER=r'[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?'
def ball_interval(s):
    m=re.fullmatch(r'\[('+NUMBER+r') \+/- ('+NUMBER+r')\]',s)
    if m:
        center,radius=map(F,m.groups());assert radius>=0;return center-radius,center+radius
    assert re.fullmatch(NUMBER,s),('unsupported ball',s)
    v=F(s);return v,v
def moment_slack(outer,m):
    lo,hi=F(outer['lo']),F(outer['hi']);total=F(0)
    kinds={'t':(1,1),'-t':(-1,1),'t2':(1,2),'-t2':(-1,2)}
    for row in outer['active']:
        if row['kind'] not in kinds:continue
        sign,power=kinds[row['kind']]
        expectation=lambda x:sign*(x if power==1 else F(2,3)+x*x/2)
        points=[lo,hi]+([F(0)] if lo<=0<=hi else [])
        rhs=max(map(expectation,points));total+=F(row['lambda'])*(rhs-expectation(m))
    return total
def controls():
    assert ball_interval('[1.25 +/- 2.5e-2]')==(F(49,40),F(51,40))
    assert ball_interval('2e-3')==(F(1,500),F(1,500))
    rejected=0
    for s in ['nan','inf','[1 +/- -1]','[1 +/- nan]','1 trailing']:
        try:ball_interval(s)
        except (AssertionError,ValueError):rejected+=1
    assert rejected==5
    density_fixtures=0
    for h in [[0,0,1,1],[F(1,5),F(3,5),F(4,5),F(2,5)],[F(1,2)]*4,[1,0,0,1]]:
        assert sum(map(F,h),F(0))/2==1
        hx=gx=hxx=gxx=F(0)
        for i,v in enumerate(map(F,h)):
            l,r=F(i,2),F(i+1,2);hx+=v*(r*r-l*l)/2;gx+=(1-v)*(r*r-l*l)/2
            hxx+=v*(r**3-l**3)/3;gxx+=(1-v)*(r**3-l**3)/3
        mean=gx-hx;assert hxx+gxx-2*hx*gx==F(2,3)+mean*mean/2;density_fixtures+=1
    return {'status':'PASS','ball_parse_fixtures':2,'malformed_ball_rejections':rejected,'exact_density_moment_fixtures':density_fixtures,'polynomial_controls':polynomial_controls()}
def verify(certificate,reports,lo,hi,target):
    data=json.loads(certificate.read_text());p,premise=coefficients(data);L,x=minimum(p,lo,hi)
    assert -1<=lo<=hi<=1 and L>0 and target>0
    oldbin=list(map(F,premise['original_mean_bin']));inputhash=sha(certificate);hashes={str(certificate):inputhash};rows=[];premises=[]
    for mode,rp in reports:
        r=json.loads(rp.read_text());assert r['passed'] and r['certificate_sha256']==inputhash and r['controls']['status']=='PASS'
        checker='verify_integer_hybrid_outer_blend.py' if mode=='integer' else 'verify_hybrid_outer_blend.py'
        assert r['checker_sha256']==sha(R/checker);hashes[str(R/checker)]=sha(R/checker)
        for n,h in r['implementation_hashes'].items():assert sha(R/n)==h;hashes[str(R/n)]=h
        if mode=='integer':
            assert list(map(F,r['mean_bin']))==oldbin
            D=F(r['positive_integral_upper_exact']);premises.append(r['functional_premises'])
            # A second assembly uses the checked hybrid numerator and exact
            # moment expectations, independently of the coefficient helper.
            old_lower=F(r['hybrid_numerator_interval'][0]);ell=F(data['hybrid_numerator_lower']);assert old_lower>=ell
            C=F(premise['hybrid_mean_square_coefficient']);theta=F(data['theta_outer']);hs=(1-theta)/ell;radius=max(map(abs,oldbin))
            from shared_mean_numerator import value
            differences=[]
            for m in map(F,[-1,0,1]):
                direct=hs*(old_lower+C*m*m-min(0,C)*radius*radius)+theta*(1+moment_slack(data['outer'],m))
                differences.append(direct-value(p,m))
            assert differences==[hs*(old_lower-ell)]*3 and differences[0]>=0
        else:
            assert r['order']==int(mode[-1]) and list(map(F,r['premises']['mean_bin']))==oldbin
            assert F(r['premises']['hybrid_numerator_lower_exact'])==F(data['hybrid_numerator_lower'])
            assert r['premises']['mean_square_coefficient_exact']==premise['hybrid_mean_square_coefficient']
            ref=R/'sources/lower-bound/certificate/prove_erdos_0380554275_arb.py';assert r['reference_sha256']==sha(ref);hashes[str(ref)]=sha(ref)
            D=ball_interval(r['positive_integral_upper_ball'])[1];premises.append(r['premises']['functional_premises'])
        assert D>0
        hashes[str(rp)]=sha(rp);bound=L/D
        rows.append({'mode':mode,'report':str(rp),'positive_integral_upper_exact':str(D),'lower_bound_exact':str(bound),'lower_bound_float_display':float(bound),'passed':bound>target})
    assert [mode for mode,_ in reports]==['arb2','arb4','integer'] and premises[0]==premises[1]==premises[2]
    return {'passed':all(r['passed'] for r in rows),'scope':'conditional exact common-mean polynomial return; complete global coverage and fresh replay are separate obligations',
            'mean_bin':[str(lo),str(hi)],'target':str(target),'polynomial_exact':list(map(str,p)),
            'minimum_numerator_exact':str(L),'minimizer_exact':str(x),'normalization_premise':premise,
            'integration_returns':rows,'independent_moment_assembly_checks':3,'hashes':hashes,'checker_sha256':sha(Path(__file__)),'polynomial_helper_sha256':sha(R/'shared_mean_numerator.py')}
def main():
    ap=argparse.ArgumentParser();ap.add_argument('certificate',type=Path);ap.add_argument('--arb2',type=Path,required=True);ap.add_argument('--arb4',type=Path,required=True);ap.add_argument('--integer',type=Path,required=True);ap.add_argument('--lo',required=True);ap.add_argument('--hi',required=True);ap.add_argument('--target',required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args()
    checked=controls();r=verify(a.certificate,[('arb2',a.arb2),('arb4',a.arb4),('integer',a.integer)],F(a.lo),F(a.hi),F(a.target));r['controls']=checked
    a.out.write_text(json.dumps(r,indent=2),encoding='utf-8');print(json.dumps({'passed':r['passed'],'mean_bin':r['mean_bin'],'bounds':[v['lower_bound_float_display'] for v in r['integration_returns']]}))
    if not r['passed']:raise SystemExit(1)
if __name__=='__main__':main()
