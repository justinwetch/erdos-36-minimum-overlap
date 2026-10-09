# Joint moment and Fourier route — proposed, not certified

Motivation: direct frequency/phase optimization and another 100 high-frequency
cosine rows gave only small numerical gains beyond the verified 0.38055650.
The current mean-zero numerical dual reaches about 0.380556589830248; this is
a point-bin discovery estimate, not a global bound. We now test structure of
the underlying complementary density that the separate Fourier rows discard.

## Variables and identities

Center the support at [-1,1]. Put r=h-g=2h-1. Then |r|<=1, integral r=0.
Define a=integral u h(u)=-m/2, b=integral u^2 h(u), c=integral u^3 h(u),
and beta=b-1/3. Thus integral r u^2=2 beta. Bathtub bounds give
1/12<=b<=7/12, so |beta|<=1/4. Also |c|<=1/4. For overlap density p,

    E_p t^4 = 16/15 - 6 beta^2 - 4 m c.

Consequently, for mean-bin maximum absolute mean M,

    16/15 - 6 beta^2 - M <= E_p t^4
       <= 16/15 - 6 beta^2 + M.

This follows by expanding E(Y-X)^4 and using h+g=1. It needs a final independent
algebra review before admission into a new trusted verifier. A simpler
unconditional fourth-moment test was not violated by the numerical primal
candidate and is recorded as a failed route in beta-diagnostic.json.

## Fourier anchor inequality

Choose real v0,v_i and nonzero frequencies xi_i. Let

    R(u)=u^2-v0-sum_i v_i cos(xi_i u),
    kappa=integral_0^1 |R(u)| du.

Writing D_i=integral_-1^1 r(u) exp(i xi_i u) du and using |r|<=1 yields

    |beta| <= kappa + sum_i |v_i| |Re D_i|/2
           <= kappa + sum_i |v_i| sqrt(sigma_i^2-C_i),

where sigma_i=sin(xi_i)/xi_i and C_i=E_p cos(xi_i t). The second inequality
uses the exact source identity sigma_i^2-C_i=|D_i|^2/4. This is a joint
constraint; every term is evaluated on the same underlying h.

For arbitrary positive tau_i, sqrt(V)<=V/(2 tau_i)+tau_i/2 gives

    |beta| <= kappa + sum_i w_i (sigma_i^2-C_i) + K,
    w_i=|v_i|/(2 tau_i), K=sum_i |v_i| tau_i/2.

On a branch |beta|>=l this becomes a linear cosine inequality with a
potentially smaller RHS:

    sum_i w_i C_i <= sum_i w_i sigma_i^2 + kappa + K - l.

On a branch |beta|<=u, the fourth-moment lower bound supplies
E_p t^4>=16/15-6u^2-M. One can cover |beta| in [0,1/4] and combine the two
constraints, or first test a two-branch split near the limiting beta.

For an interval |beta| in [l,u], l+u>0, the chord inequality
|beta| >= (beta^2+l*u)/(l+u) also gives the valid composite row

    sum_i w_i C_i - E_p t^4/[6(l+u)]
      <= sum_i w_i sigma_i^2 + kappa + K
         - (16/15-M)/[6(l+u)] - l*u/(l+u).

These are proposed analytic bridges. No new bound has been claimed from them.
Continuous kappa must be rigorously recomputed; a sampled LP residual is not
an integral certificate. A new composite term would require an explicitly
reviewed verifier extension and complete mean/beta coverage. The original
mathematical objective and support, mass and box constraints remain fixed.

## Executed deciding tests

anchor_diagnostic.py solves sampled r LPs with selected Fourier anchors fixed
to zero, maximizing beta. With 1,2,4,8,16,32 anchors, the numerical maxima are
approximately .23484,.19353,.17357,.16915,.16866,.16292. The implied beta from
the current dual's positive-set candidate is about .16776. Thus 32 joint
anchors potentially separate it, while individual anchors do not.

The 32-anchor dual contains large coefficients, so nonzero anchor slacks may
erase the apparent separation. This is the deciding uncertainty. Evaluate
the bound using an actually feasible primal relaxation, not an inaccurate
indicator from a nearly flat dual q. Choose tau_i from the primal slacks and
allow a numerical floor before forming any weights.

primal_relaxation.py is currently solving a 4096-cell even-p LP with source
cosine inequalities, mass and second moment. It does not construct h and
its cap is NOT an upper bound for the original problem. Its role is to test
separation and diagnose limits of the present relaxation. If the 240-second
solve times out, a smaller primal diagnostic is appropriate; do not infer
infeasibility or stationarity from a timeout.

Update around 02:28 UTC: the 4096-cell primal solve completed in 72.82 seconds,
cap 0.3805566599469782, fourth moment 0.8950467511233176, implying
|beta| about 0.16912516 at mean zero. Its maximum floating constraint
violation was 2.12e-10; it is a numerical diagnostic, not a certificate.
anchor_separation.py reoptimized the anchor dual allowing nonzero Fourier
slacks, with a conservative numerical slack floor 1e-9. The 32-anchor explicit
bound is about 0.16505588317, leaving separation about 0.00406928. Its sum
of absolute v coefficients is about 10.98824, much smaller than the first
zero-anchor dual. The 16-anchor row also separates, but only by about .000417.

verify_anchor.py has now executed the complete continuous auxiliary integral
for the 32-anchor soft dual, at Arb 200 bits and cell width 1e-6:

    kappa <= 0.16445409357730963473786888783921200566602027530851...

Record: runs/anchor-kappa-32.json, 2399 nodes, 80 ambiguous cells. A floating
bracket failed because two summation orders disagreed near zero; that proposal
was skipped, and the remaining full interval was still covered by Arb. Three
polynomial special cases with known absolute integrals also passed. This
checks only kappa. It is not a new global minimum-overlap bound.

Before implementing a large new verifier, test the two beta branches numerically
on the primal LP, with a threshold near .166-.169 and the outward kappa upper
bound. Quantify the actual cap gain. A large beta separation may still buy only
a tiny bound gain because high-frequency deficits are cheap: for positive
weights lambda_i, Cauchy-Schwarz gives

    sum_i lambda_i (sigma_i^2-C_i)
       >= (|beta|-kappa)^2 / sum_i(v_i^2/lambda_i)

when |beta|>kappa. Large coefficient norms or small existing multipliers can
make this improvement negligible. This is a deciding cost check, not grounds
to announce a major gain. If numerical conditional caps do not improve usefully,
retain the auxiliary inequality and change approach rather than building a
large unproductive extension.

## Continuous kappa certificate plan

For R, compute Arb jets through order three, with
M4=sum_i |v_i| |xi_i|^4. The primitive is
u^3/3-v0*u-sum_i v_i sin(xi_i*u)/xi_i. On [0,1], use the same fourth-order
Taylor enclosure as the existing verifier: integrate R where its sign is
certified, -R where negative, and bound ambiguous cells by width times a
certified absolute maximum. Every final interval must be covered. Floating
roots may seed subdivisions only. This yields an outward kappa upper bound.
Recompute it once per anchor list inside any extended verifier rather than
trusting a serialized float. Then derive each branch RHS outward using that
bound, the exact listed v_i,tau_i, and mean/beta endpoints.
