"""Exact narrower-mean conclusion from an executed fixed-kernel enclosure."""
from fractions import Fraction as F
from verify_shared_mean_return import ball_interval

def retarget(report, mode, mean):
    assert report['passed'] and mode in ['arb2','arb4','integer']
    old=F(report['mean_abs_max']);mean=F(mean)
    assert 0<=mean<=old<=1,'new central radius must not exceed executed radius'
    c=F(report['mean_square_coefficient_exact']);negative=min(F(0),c)
    if mode=='integer':
        D=F(report['positive_integral_upper_exact']);oldnum=F(report['numerator_interval'][0])
        assert D>0 and F(report['lower_bound_exact'])==oldnum/D,'inconsistent executed integer return'
        L0=oldnum-negative*old*old
    else:
        assert report['order']==int(mode[-1])
        D=ball_interval(report['positive_integral_upper_ball'])[1]
        L0=ball_interval(report['mean0_numerator_ball'])[0]
        assert D>0,'nonpositive executed denominator'
    numerator=L0+negative*mean*mean
    assert numerator>0
    return {'mode':mode,'executed_mean_abs_max':str(old),'returned_mean_abs_max':str(mean),'mean0_numerator_lower_exact':str(L0),'mean_square_coefficient_exact':str(c),'positive_integral_upper_exact':str(D),'numerator_lower_exact':str(numerator),'lower_bound_exact':str(numerator/D)}

def controls():
    cases=0
    for c in [F(-3),F(0),F(2)]:
        old=F(1,5);new=F(1,10);L0=F(2);D=F(5)
        r={'passed':True,'mean_abs_max':str(old),'mean_square_coefficient_exact':str(c),'positive_integral_upper_exact':str(D),'numerator_interval':[str(L0+min(F(0),c)*old*old)],'lower_bound_exact':str((L0+min(F(0),c)*old*old)/D)}
        got=retarget(r,'integer',new)
        assert F(got['lower_bound_exact'])==(L0+min(F(0),c)*new*new)/D;cases+=1
        try:retarget(r,'integer',F(1,4))
        except AssertionError:pass
        else:raise AssertionError('enlarged radius accepted')
    return {'status':'PASS','exact_positive_zero_negative_coefficient_cases':cases,'enlarged_radii_rejected':cases}

if __name__=='__main__':
    import json
    print(json.dumps(controls()))
