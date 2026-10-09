# Retaining the same mean in every numerator inequality

Let m=integral t p(t)dt, with integral p=1. The partition identity gives
integral t^2 p(t)dt=2/3+m^2/2. An embedded hybrid kernel H has the checked
lower expectation L0+C m^2. The old normalization premise at radius r is
L0+min(0,C)r^2>=ell. Therefore, for every admissible mean m,

    integral H p >= ell+C m^2-min(0,C)r^2.

The blend Q=hs H+theta(1+sum lambda(B_bin-phi)), hs=(1-theta)/ell,
has the following lower expectation polynomial:

    L(m)=1+hs[C m^2-min(0,C)r^2]
       +theta sum lambda[B_bin-B_actual(m)].

For t, -t, t^2 and -t^2, B_actual(m) is exactly m, -m,
2/3+m^2/2 and -2/3-m^2/2. For the accepted trigonometric coordinates,
the same universal upper RHS is used, so their additional lower slack is
zero. This is a lower bound even if those inequalities are not sharp.
All original multipliers and Fourier/Gram premises remain unchanged.

The previous return replaced each mean-dependent term by its separate
worst case on the bin. These worst cases need not occur at the same m.
Retaining their sum gives an exact rational quadratic L. Its minimum on
an interval occurs at an endpoint or at its interior vertex when convex.
For a checked D>=integral Q_+, and p<=M, we obtain

    M >= min_m L(m)/D,

provided that minimum is positive. The same fixed kernel can be used on
an interval different from its original one: the original bin supplies
its normalization premise and fixed coefficients, while the displayed
polynomial gives its expectation for the actual m. Reflection supplies
the negative-mean return exactly as in PROOF.md.

This is a derived return, not a new global bound. The first exact rational
diagnostic found minimum numerator slack 1.0681e-6 for the broad low20-26
kernel, suggesting a quadrature bound 0.3806260845 instead of 0.3806256780.
The denominator in that diagnostic was numerical. The separate
verify_shared_mean_return.py requires all three checked integrations,
their input/dependency hashes and identical embedded premises. It parses
outward ball endpoints as rationals and uses the integer denominator
directly. Complete mean coverage, independent return review and fresh
replay are still required before any global claim is promoted.


Executed checks now include a three-mode conditional return above
0.3806255776217937 on [0.0024,0.0025], exact independent assembly from
the checked hybrid numerator, four exact density moment fixtures, and an
intentional rejected target of 0.4. The separate polynomial global auditor
passed a full regression on the original verified 0.380624000 cover.
The proposed two-kernel cover uses a central radius 0.0008, coverage
[0.0008,0.00244] from the original [0.0018,0.0022] kernel and
[0.00244,0.003515625] from the original [0.0030,0.0034] kernel. Exact
fourth-order returns exceed 0.38062620283 and 0.38062620101 respectively.
The original integer integrations and complete fresh replay are pending.
No new global bound has been promoted on this basis.

The v9 numerical search minimizes the positive-part integral divided by
the minimum common-mean numerator. Its gradient differentiates the active
endpoint or interior quadratic vertex by the envelope theorem. The search
records raw 1/D separately from the numerator-adjusted numerical score.
Both remain discovery scores until a rounded kernel passes the separate
exact numerator and continuum integration checks. No optimizer optimality
or causal skill-efficacy claim follows from these experiments.
