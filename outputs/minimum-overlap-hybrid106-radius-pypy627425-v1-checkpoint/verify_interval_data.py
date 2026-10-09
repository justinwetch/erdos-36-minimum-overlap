"""Outward integration for exact rational periodic interval test functions."""
from decimal import Decimal
from fractions import Fraction as F
from flint import arb
from verify_fourth_order import q_jet,fourth_derivative_bound,reference
from circle_intervals import compile_intervals

def A(f):
    return arb(f.numerator)/f.denominator

def verify(data,width,order):
    parts,B,nonzero=compile_intervals(data); terms=[]
    y0,y2=arb(data['y0']),arb(data['y2']); y2D=Decimal(data['y2'])
    if not Decimal(data['y0']).is_finite() or not y2D.is_finite(): raise ValueError('nonfinite polynomial coefficient')
    if y2D:
        terms.append(reference.Term('t2' if y2D<0 else '-t2',None,-y2 if y2D<0 else y2,arb(0)))
    L=y0+y2*arb(2)/3+A(B)
    for row in data['cos']:
        zD,xiD=Decimal(row['z']),Decimal(row['xi'])
        if not zD.is_finite() or zD>0 or not xiD.is_finite() or xiD==0: raise ValueError('invalid cosine')
        z,xi=arb(row['z']),arb(row['xi']); terms.append(reference.Term('cos',row['xi'],-z,arb(0)))
        L+=z*(xi.sin()/xi)**2
    M4=fourth_derivative_bound(terms)
    M2=2*y2.abs_upper()+sum((t.lam.abs_upper()*t.xi.abs_upper()**2 for t in terms if t.kind=='cos'),arb(0))
    widthF=F(width)
    if widthF<=0: raise ValueError('positive width required')
    total=arb(0); nodes=amb=pos=neg=0
    for aF,bF,step in parts:
        shift=y0-1+A(step); stack=[(aF,bF)]
        while stack:
            aa,bb=stack.pop(); a,b=A(aa),A(bb); c,r=(a+b)/2,(b-a)/2
            q,q1,q2,q3=q_jet(terms,c); q+=shift
            if order==4:
                radius=q1.abs_upper()*r+q2.abs_upper()*r*r/2+q3.abs_upper()*r**3/6+M4*r**4/24
            elif order==2: radius=q1.abs_upper()*r+M2*r*r/2
            else: raise ValueError('Taylor order')
            nodes+=1
            if nodes>10000000: raise RuntimeError('node limit')
            lo,hi=q-radius,q+radius
            if hi<=0: neg+=1; continue
            if lo>=0:
                total+=(reference.Q(terms,b)-reference.Q(terms,a)+shift*(b-a)).upper(); pos+=1
            elif bb-aa<=widthF:
                total+=(b-a)*reference.pos_upper(hi); amb+=1
            else:
                middle=(aa+bb)/2; stack.extend(((aa,middle),(middle,bb)))
    return (2*total).upper(),L,{'nodes':nodes,'ambiguous':amb,'positive':pos,'negative':neg,
                               'cosine_rows':len(data['cos']),'nonzero_circle_rows':nonzero,'compiled_pieces':len(parts)}
