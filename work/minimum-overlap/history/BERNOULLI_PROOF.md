# Periodic quadratic overlap tests

Put B2(u)=u^2-u+1/6 on [0,1] and extend it periodically. For every
positive integer N and a=2/N, every admissible overlap density p obeys

    integral_[-2,2] p(t)*B2(t/a)dt <= 0.

This is a universal inequality, not an assertion that a relaxed primal
profile is an admissible overlap. The function B2 is continuous and even
on the circle, and is quadratic between its integer knots.

## Direct covariance proof

Let eps_s(x)=a*({(s-x)/a}-1/2), with s uniform on one period of length a.
Its values at discontinuity points do not affect any integral. The exact
covariance identity is

    E_s eps_s(x)*eps_s(y)=(a^2/2)*B2((x-y)/a).

To verify it, use periodicity to set x=0, y/a=v in [0,1], then integrate
the product of the two affine sawtooths on [0,v] and [v,1]. This gives
(a^2/2)*(v^2-v+1/6). Both sawtooths have zero mean.

For r=2h-1 on [0,2], zero outside, let E_s=integral r(x)*eps_s(x)dx.
Boundedness and compact support justify Fubini, and therefore

    Var_s(E_s)=(a^2/2)*integral R(t)*B2(t/a)dt >=0,
    R(t)=integral r(x)*r(x+t)dx.

The even part e of the overlap is (2-|t|)_+/4-R(t)/4. Moreover
integral (2-|t|)_+*B2(t/a)dt=0: write the triangular kernel as the
autocorrelation of 1_[0,2], and for each fixed x integrate y over exactly
N periods of the zero-mean function B2((y-x)/a). Consequently

    integral p(t)*B2(t/a)dt
      = integral e(t)*B2(t/a)dt
      = -Var_s(E_s)/(2*a^2) <=0.

No differentiability of h, step-density assumption, Fourier truncation,
or overlap-mean restriction is required. The density box constraint is
stronger than needed for the boundedness used in this proof.

## Exact cell integrals and discovery scope

A periodic primitive is J(u)=u^3/3-u^2/2+u/6 on [0,1], since J(0)=J(1)=0.
Thus the exact integral over any cell [l,r] is a*(J({r/a})-J({l/a})).
For a literal even step profile on n positive-axis cells, scan_bernoulli.py
uses integer residues (N*i) mod n and rational polynomial arithmetic to
evaluate every selected functional exactly. The factor 2 includes the
negative half-axis. A positive value excludes that literal profile, but
is not a bound on the original optimum.

Equivalently B2(u)=pi^-2 sum_(k>=1) cos(2*pi*k*u)/k^2. The absolute
uniform convergence allows integration term by term. This explains the
connection to infinitely many Fourier constraints. The covariance proof
above does not depend on that series. Finite spectral separation can use
the already supported Fourier rows instead, with every resulting decimal
frequency treated as an exact rational and its analytic RHS recomputed.

The bounded discovery probe with twelve quadratic rows gave only a small
numerical gain. Before adding a new continuous certificate schema, the
campaign tests finite Fourier separation of the resulting relaxed profile.
Any new bound still requires complete continuous and mean-cover replays.
