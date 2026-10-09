"""Independent integer certificate for uniform step densities; stdlib only."""
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path

def require(condition, message):
    if not condition:
        raise ValueError(message)

def certificate(values, denominator=10**15):
    """Round to a fixed denominator and restore mass within the box exactly."""
    n = len(values)
    require(n > 0 and n % 2 == 0, 'positive even vector length required')
    a = [max(0, min(denominator, round(float(x) * denominator))) for x in values]
    discrepancy = n * denominator // 2 - sum(a)
    # Change interior cells first; this avoids perturbing saturated plateaux.
    order = sorted(range(n), key=lambda i: min(a[i], denominator-a[i]), reverse=True)
    repairs = []
    for i in order:
        if discrepancy == 0:
            break
        delta = min(discrepancy, denominator-a[i]) if discrepancy > 0 else max(discrepancy, -a[i])
        a[i] += delta
        discrepancy -= delta
        if delta:
            repairs.append([i, delta])
    require(discrepancy == 0, 'mass repair failed')
    return {'denominator': denominator, 'numerators': a, 'repair': repairs}

def verify(obj):
    a = obj['numerators']
    d = obj['denominator']
    n = len(a)
    require(type(d) is int and d > 0, 'bad denominator')
    require(n > 0 and n % 2 == 0, 'bad length')
    require(all(type(x) is int and 0 <= x <= d for x in a), 'box violation')
    require(2*sum(a) == n*d, 'mass violation')
    # Direct ordered cell-pair accumulation, independently of optimizer slices.
    sums = [0] * (2*n-1)
    for i, ai in enumerate(a):
        for j, aj in enumerate(a):
            sums[j-i+n-1] += ai * (d-aj)
    peak = max(sums)
    argmax = [i-n+1 for i,s in enumerate(sums) if s == peak]
    q = Fraction(2*peak, n*d*d)
    scale = 10**25
    low = q.numerator*scale // q.denominator
    high = low+1
    result = {'status': 'PASS', 'n': n, 'shifts_checked': 2*n-1,
              'mass': '1', 'box': 'exact', 'argmax_lags': argmax,
              'score_fraction': str(q), 'score_float': float(q),
              'decimal_lower': f'{low//scale}.{low%scale:025d}',
              'decimal_upper_strict': f'{high//scale}.{high%scale:025d}',
              'scope': 'exact continuum supremum of this uniform step function; no global optimality claim'}
    # An independent second arithmetic organization checks every lag.
    for m in range(-(n-1), n):
        total = sum(a[i]*(d-a[i+m]) for i in range(max(0,-m), min(n,n-m)))
        require(total == sums[m+n-1], 'independent lag mismatch')
    return result

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=Path)
    parser.add_argument('--out', type=Path)
    args = parser.parse_args()
    data = args.input.read_bytes()
    obj = json.loads(data)
    result = verify(obj)
    result['input_sha256'] = hashlib.sha256(data).hexdigest()
    if args.out:
        args.out.write_text(json.dumps(result, indent=2), encoding='utf-8')
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()
