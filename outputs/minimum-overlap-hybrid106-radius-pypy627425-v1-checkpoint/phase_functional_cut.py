"""Convert an exactly checked Gram functional into a discovery LP row."""
import argparse,hashlib,json
from fractions import Fraction as F
from pathlib import Path

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def hat_integral(lo,hi,c,a):
    points=sorted({lo,hi,max(lo,min(hi,c))})
    height=lambda t:max(F(0),1-abs(t-c)/a)
    # Include the support corners if the LP cell straddles them.
    points=sorted(set(points)|{t for t in (c-a,c+a) if lo<t<hi})
    return sum(((r-l)*(height(l)+height(r))/2 for l,r in zip(points,points[1:])),F(0))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('certificate',type=Path);ap.add_argument('report',type=Path)
    ap.add_argument('profile',type=Path);ap.add_argument('--out',type=Path,required=True);args=ap.parse_args()
    data=json.loads(args.certificate.read_text(encoding='utf-8'));report=json.loads(args.report.read_text(encoding='utf-8'))
    if not report['passed'] or report['certificate_sha256']!=sha(args.certificate):raise ValueError('missing executed functional check')
    if report['checker_sha256']!=sha(Path(__file__).with_name('verify_phase_gram.py')):raise ValueError('checker changed')
    if data['schema']!='phase-gram-functional-v2':raise ValueError('signed functional required')
    lower=F(report['functional_lower_bound_exact']);gamma=list(map(F,data['functional_weights']));N=data['cells'];a=F(2,N)
    profile=json.loads(args.profile.read_text(encoding='utf-8'),parse_float=str);p=list(map(F,profile['values']));n=len(p)
    coefficients=[]
    for i in range(n):
        lo,hi=F(2*i,n),F(2*(i+1),n)
        first=max(0,int(lo/a)-1);last=min(N,int(hi/a)+1)
        value=sum((gamma[k]*(2 if k==0 else 1)/a*hat_integral(lo,hi,k*a,a) for k in range(first,last+1)),F(0))
        coefficients.append(value)
    actual=sum((c*x for c,x in zip(coefficients,p)),F(0));gap=lower-actual;scale=max(map(abs,coefficients))
    result={'status':'EXACT_FUNCTIONAL_ROW','scope':'exact mean-conditional linear row and literal-profile comparison; float LP row is discovery only',
        'certificate_sha256':sha(args.certificate),'report_sha256':sha(args.report),'profile_sha256':sha(args.profile),
        'mean_abs_max':data['mean_abs_max'],'functional_lower_exact':str(lower),'profile_functional_exact':str(actual),
        'profile_separation_gap_exact':str(gap),'profile_separation_gap_float_display':float(gap),
        'hat_average_infinity_exclusion_radius_exact':str(max(F(0),gap)/sum(map(abs,gamma))),
        'rows':[{'values':[-float(c/scale) for c in coefficients],'rhs':-float(lower/scale),
                 'rational_values':[str(-c/scale) for c in coefficients],'rational_rhs':str(-lower/scale)}]}
    args.out.write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
if __name__=='__main__':main()
