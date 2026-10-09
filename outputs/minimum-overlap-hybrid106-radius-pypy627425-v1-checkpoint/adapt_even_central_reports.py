"""Return checked central denominators to a theta-zero normalized wrapper."""
import argparse,hashlib,json
from fractions import Fraction as F
from pathlib import Path
from hybrid_functionals import validate
from shared_mean_numerator import coefficients
from verify_shared_mean_return import ball_interval
R=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def adapt(wrapper,central,reports):
    d=json.loads(wrapper.read_text());h=json.loads(central.read_text());assert F(d['theta_outer'])==0 and d['outer']['active']==[] and d['hybrid']==h
    ell=F(d['hybrid_numerator_lower']);poly,premise=coefficients(d);C=F(premise['hybrid_mean_square_coefficient']);radius=max(abs(F(d['outer']['lo'])),abs(F(d['outer']['hi'])))
    bindings={str(wrapper):sha(wrapper),str(central):sha(central)};rows=[];expected=None;oldmean=None
    for mode,p in reports:
        r=json.loads(p.read_text());assert r['passed'] and r['certificate_sha256']==sha(central)
        checker='verify_integer_hybrid.py' if mode=='integer' else 'hybrid_certificate.py';assert r['checker_sha256']==sha(R/checker);bindings[str(R/checker)]=sha(R/checker)
        for n,v in r['implementation_hashes'].items():assert sha(R/n)==v;bindings[str(R/n)]=v
        mean=F(r['mean_abs_max']);assert F(r['mean_square_coefficient_exact'])==C
        if oldmean is None:oldmean=mean;_,expected=validate(h,mean)
        assert mean==oldmean and r['functional_premises']==expected
        if mode=='integer':D=F(r['positive_integral_upper_exact']);L0=F(r['numerator_interval'][0])-min(0,C)*mean*mean
        else:
            assert r['order']==int(mode[-1]);D=ball_interval(r['positive_integral_upper_ball'])[1];L0=ball_interval(r['mean0_numerator_ball'])[0]
        assert D>0 and L0+min(0,C)*radius*radius>=ell
        rows.append({'mode':mode,'report':str(p),'original_positive_integral_upper_exact':str(D),'wrapped_positive_integral_upper_exact':str(D/ell),'verified_mean0_numerator_lower_exact':str(L0)});bindings[str(p)]=sha(p)
    assert [m for m,_ in reports]==['arb2','arb4','integer']
    for n in ['adapt_even_central_reports.py','hybrid_functionals.py','verify_phase_gram.py','shared_mean_numerator.py','verify_shared_mean_return.py']:bindings[str(R/n)]=sha(R/n)
    return {'status':'PASS','scope':'three executed fixed-central-kernel denominator bounds scaled by the exact positive normalization; no global mu bound by itself','wrapper_sha256':sha(wrapper),'central_sha256':sha(central),'polynomial_exact':list(map(str,poly)),'rows':rows,'maximum_wrapped_denominator_exact':str(max(F(r['wrapped_positive_integral_upper_exact']) for r in rows)),'bindings':bindings,'implementation_sha256':sha(Path(__file__))}
def main():
    ap=argparse.ArgumentParser();ap.add_argument('wrapper',type=Path);ap.add_argument('--central',type=Path,required=True);ap.add_argument('--arb2',type=Path,required=True);ap.add_argument('--arb4',type=Path,required=True);ap.add_argument('--integer',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();r=adapt(a.wrapper,a.central,[('arb2',a.arb2),('arb4',a.arb4),('integer',a.integer)]);a.out.write_text(json.dumps(r,indent=2),encoding='utf-8');print(json.dumps({'status':r['status'],'maximum_wrapped_denominator_exact':r['maximum_wrapped_denominator_exact']}))
if __name__=='__main__':main()
