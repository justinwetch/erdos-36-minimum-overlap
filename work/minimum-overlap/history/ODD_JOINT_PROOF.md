# Cap-dependent odd moments: a conditional result, then a cheap escape

Status, October 8, 2026, approximately 04:35 UTC: a continuous conditional case
exclusion is established computationally in this work. It is not a new global
bound. Reoptimization found a cheap escape, so a large global verifier extension
is not currently justified. This supersedes ODD_MOMENT_ROUTE.md's finite model.

## Exact identities

Let p be the original overlap, e(t)=(p(t)+p(-t))/2, and A(t)=p(t)-p(-t).
For 0<=t<=2, cancellation of the autocorrelation terms gives

    A(t)=integral_0^t h(x)dx-integral_(2-t)^2 h(x)dx,
    A(2-t)=A(t), A'(t)=h(t)-h(2-t) almost everywhere.

Center h on [-1,1], put r=2h-1, and v(u)=(r(u)-r(-u))/2 for 0<=u<=1.
Then |v|<=1, and A(t)=-integral_(1-t)^1 v(u)du for 0<=t<=1.
For M>=||p||_infinity, |A(t)|<=2(M-e(t)); reflection also bounds A(t)
using e(2-t). Define a_k=(1/2) integral_-1^1 r(u)u^k du.
For odd k, a_k=integral_0^1 v(u)u^k du, and a_1=-mean(p)/2.
The odd overlap moments satisfy

    E_p t^(2n+1)=-2 sum_(odd k<=2n+1) binom(2n+1,k)*a_k/(2n+2-k).

In particular p3=-2a1-2a3 and p5=-2a1-(20/3)a3-2a5.
check_odd_mapping.py passed 108 exact rational fixtures. General even moment
identities and the symmetric-subclass caveat are in MOMENT_ROUTE.md.

## Corrected model and paired fits

The relaxed 4096-cell profile supplies cell averages, not endpoint values.
The earlier endpoint test was too restrictive for comparison with the
relaxation. No verified global result depended on it. odd_cap_diagnostic.py
now defaults to exact cell-average A constraints on a nested finite odd grid;
--endpoint-model retains the stronger toy model.

For runs/circle-interior-original4096/primal.json, a 256-cell odd v model gave
numerical capacities approximately .0001341713, .0002207435, .0003050695,
.0003871955 and .0004671670 for a3,a5,a7,a9,a11 respectively. These are finite
diagnostics, not continuous bounds (odd-cap-averaged-circle1/summary.json).

A general r fit uses 512 cells, because the odd grid covers only [0,1]. On that
same grid, unconstrained moments through p degree12 fit with maximum scaled
residual 1.21e-9. Adding separate numerical odd capacities left residual
3.49e-6. Optimizer failure is not an infeasibility proof. Records:
moment-fit-unrestricted512 and moment-fit-odd-averaged1.

## Separate capacities lose dependence

moment_separator.py found an even polynomial P of degree10 with reconstructed
functional F approximately 1. Exact rational interval integration proves
integral_0^1 |P| <= .9996309844366295 (display value). Naive propagation and
polynomial expansion both failed to exclude the case using separate odd
capacities: expanded F lower was .99781824. Failed reports are retained.

The expanded functional's odd quadratic part has two negative eigenmodes.
Numerical joint LP bounds on these combinations were much tighter than the
componentwise boxes, motivating continuous support-function certificates.

## Continuous support certificate

For half-grid t cells I_i=[i/N,(i+1)/N], define

    K_i(u)=-length(I_i intersect [1-u,1])/length(I_i).

Then average_(I_i) A=integral_0^1 K_i(u)v(u)du. If full-grid averages of e
are bounded below by p_i, the cap and reflection imply

    |integral K_i*v| <= E_i=2(M-max(p_i,p_(2N-1-i))).

For an odd polynomial w and real gamma,z_i, mean zero gives

    |integral w*v| <= sum |z_i| E_i
                     + integral_0^1 |w-gamma*u-sum z_i*K_i| du.

This covers arbitrary measurable |v|<=1. The K_i sum is piecewise affine;
its polynomial residual can be integrated outward with exact rational
arithmetic. LP optimality and finite-grid feasibility are not proof premises.

odd_dual_discovery.py exports candidate multipliers; verify_odd_duals.py checks
the continuous residual. Coarse 256-cell multipliers had large residuals
(aliasing). With 2048 discovery cells, exact checked support bounds for
a3,a5,a7,a9 are approximately .0002373910, .0004773508, .0007738312,
.0011199332. The two harmful combinations are bounded by .00001202783 and
.0001856423. All are conditional on the listed profile, cap and zero mean.
Record: runs/odd-dual2048-circle1/continuous-check.json.

## Conditional exclusion actually checked

verify_joint_obstruction.py uses that same profile/cap case, mean zero, and
overlap moments p4,p6,p8,p10,p12 within 1e-8 of the literal centers in
runs/moment-reconstruction-circle1/summary.json. These are additional explicit
hypotheses, not consequences of cell-average closeness alone.

Complementation preserves the case and permits a2>=0. The p4 identity bounds
a2. Polynomial expansion reconstructs a4,...,a10 while retaining cancellations.
The odd quadratic part is bounded below by two negative squares; the residual
matrix is positive definite by exact rational LDL and an exact reconstruction
check. Higher-order terms and coefficient errors are bounded outward. The F
lower is .9999157633295429, exceeding the checked integral |P| upper by more
than .00028477889. Since |r_even|<=1 requires F<=integral |P|, no density
satisfies this entire explicit case.

Executed report: runs/odd-dual2048-circle1/joint-obstruction.json, PASS.
check_moment_polynomial.py passed 2000 exact rational fixtures;
check_continuous_odd_duals.py passed 91 independent kernel-integration and LDL
fixtures. This is a computational proof with stated analytic premises, not
proof-assistant verification or a global minimum-overlap lower bound.

## Deciding experiment and remaining obligation

A heuristic tangent cut to the obstruction was added to the same 4096-cell
circle/Fourier LP. This diagnostic cut is not asserted valid outside the case
above. The paired control cap was .3805669504398015; the cut run moved to
.3805669905169041, only about 4.01e-8 higher. Both source IPM exits were Unknown
with usable interior proposals; neither is an optimality certificate. The
revised moments are numerically feasible in the symmetric subclass through
degree12; its best degree10 sampled separator has negative separation margin.
Records: moment-cut-control4096, moment-cut-test4096,
moment-reconstruction-cut1, moment-separator-cut1.

The original relaxed profile is incompatible with a concrete continuous case,
but nearby objective values escape this low-order mechanism. The global bound
is unchanged. Further investment requires materially stronger reoptimized
gain, coverage beyond mean zero, and elimination or coverage of the profile
and moment hypotheses. Repeating the fixed-profile exclusion would not do so.
