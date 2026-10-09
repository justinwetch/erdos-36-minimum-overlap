# Continuous Fourier, circle and phase-Gram functional certificate

This proof supplements PROOF.md, CIRCLE_PROOF.md and PHASE_GRAM_PROOF.md.
It applies to every measurable h:[0,2]->[0,1] of integral 1, with g=1-h
on that interval, both zero outside, and p(t)=integral h(x)g(x+t)dx.
Write m=integral t*p(t)dt. The finite-to-continuous bridge is in PROOF.md.
The certificate has schema periodic-gram-functional-v5, containing a
schema-v2 periodic/Fourier certificate and finitely many embedded signed
phase-Gram certificates with nonnegative rational multipliers mu_j.

## Exact functional return map

For functional j, a_j=2/N_j and gamma_j,k are its signed hat weights.
The phase argument proves sum_k gamma_j,k*y_j,k >= L_j(0)-eta_j*m^2/a_j^2.
Its PSD matrix does not depend on m. The sharper alias estimate 1/12 is
already included in L_j(0); any larger certificate error constant is valid.
The checker recomputes the matrix and this constant from the embedded
coefficients. It requires the restricted matrix to be positive definite
by exact integer Bareiss elimination and Sylvester's criterion. Numerical
solver output and stored functional RHS values are not premises.

Let T_a(t)=max(0,1-|t|/a). Extend the following K_j evenly from t>=0:

    K_j(t)=gamma_j,0*T_a(t)/a_j
           +sum_(k=1)^N_j gamma_j,k*T_a(t-k*a_j)/(2*a_j).

Because the even part of p is e(t)=(p(t)+p(-t))/2, the whole-line integral
of p*K_j equals sum gamma_j,k*y_j,k. For k=0 the two half-lines share
one centered hat. For k>=1 the positive hat's support stays nonnegative,
and the reflected negative hat contributes the other half. The endpoint
hat at t=2 is integrated only over the support of p. There is no assumption
that p is piecewise constant or that its odd part vanishes.

On [0,2], K_j is exactly piecewise affine, with knot values gamma_j,0/a_j
at zero and gamma_j,k/(2*a_j) at k*a_j, k>=1. These are the kernels
implemented in hybrid_functionals.py. The independent hat-integral fixtures
cover their normalization, support corners, signed weights and primitives.

## Hybrid lower inequality and mean dependence

Let Q_base be the even test function of the schema-v2 certificate. Its
universal Fourier, moment and periodic hypermetric inequalities give

    integral p*Q_base >= L_base(0)+(y2/2)*m^2.

For Q=Q_base+sum mu_j*K_j, nonnegative mu_j therefore give

    integral p*Q >= L0+c*m^2,
    L0=L_base(0)+sum mu_j*L_j(0),
    c=y2/2-sum mu_j*eta_j/a_j^2.

For |m|<=delta, the valid uniform numerator is

    L(delta)=L0+min(0,c)*delta^2.

The mean coefficient is combined before taking this minimum. This also
covers positive y2 and does not separately discard a helpful term.
For M=||p||_infinity, nonnegativity of p gives
integral p*Q <= M*integral max(Q,0). Thus a certified upper D on the last
integral and positive L(delta),D imply M>=L(delta)/D. Signed functional
lower values may be negative; their individual values are not bounds on M.

## Complete continuous integration

Split [0,2] at the union of all exact periodic step discontinuities and
all rational hat knots. On each resulting piece, the added functional
kernel is u+v*t. No integration interval crosses a jump or a kink.
The exact affine contribution to the jet is u+v*c at the center and v
in the first derivative; its second and higher derivatives vanish.
Its primitive increment is u*(b-a)+v*(b^2-a^2)/2.

Each piece is covered by rational intervals obtained by exact bisection.
The Arb implementation encloses the value by either the first-order jet
with global second-derivative remainder, or the third-order jet with
global fourth-derivative remainder. Entirely negative pieces contribute
zero; entirely positive pieces use an outward primitive difference;
ambiguous pieces use width times the nonnegative outward upper range.
All pieces are included even when a numerical root finder missed a zero.
The final positive-axis sum is doubled because Q is even.

verify_integer_hybrid.py independently compiles the periodic families and
uses standard-library integer dyadic enclosures for trigonometric values,
jets and primitives. It shares the exact hat helper and rational Gram
checker with the Arb path; this shared dependency is explicit in hashes.
Agreement is an implementation check, not a formal proof-assistant result.

## Global obligation

A central replay covers only |m|<=delta. The global lower claim also needs
executed Fourier outer certificates covering every remaining m in [-1,1]
at the same target. Their finite interval union, endpoints, report inputs
and checker hashes must be audited. A previously passed weaker target
cannot substitute for a fresh stronger replay. Until that union passes,
this construction remains a central-case result.
