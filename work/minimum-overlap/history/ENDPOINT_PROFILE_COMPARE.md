# Endpoint geometry discriminator

Status: derived necessary inequalities; paired numerical fit executed.
Existing trusted checkers and certificate schemas are unchanged.

For phase u uniform on[0,1], endpoint cell averages satisfy |x|<=u and
|z|<=1-u, while an interior average satisfies |y|<=1. Thus
E|xy|<=1/2 and E|xz|<=1/6. Each of the four triangle sign patterns with
product -1 has pointwise bound1-u+u^2, hence expectation at most5/6.

To prove the triangle bound it suffices to check cube vertices because
the expression is multilinear in the three rescaled variables. Sign
flips reduce to maximizing xy+yz-xz. Equal endpoint signs give
1-u(1-u); opposite signs give |2u-1|+u(1-u), which is no larger:
their difference is2u^2 for u<=1/2 and2(1-u)^2 for u>=1/2.
Integrating gives5/6. These statements require no step-density assumption.

Earlier endpoint-five tests included these sharper endpoint premises in
both arms, so their zero pentagon increment did not isolate the value of
endpoint geometry itself. A new paired test on the calibrated continuous
profile uses identical generic PSD, mean and retained triangle premises,
then adds only endpoint pair/cross/triangle bounds. It reports numerical
constraint defects and preserves both matrices. A meaningful increment
would warrant designing a separate exact certificate extension; otherwise
defer it. Numerical objective or solver status is not a proof or an
infeasibility certificate. No endpoint row is accepted by existing checkers.

The order43 calibrated-profile comparison completed in169.7635 seconds,
with602 retained triangles and3232 exact vertex checks. Generic-box
mismatch was .0005428045550343666 (optimal_inaccurate, maximum numerical
defect4.00e-10); endpoint-box mismatch was .0005428035388810315 (optimal,
defect3.34e-11). The -1.016e-9 increment is numerical noise, not a genuine
decrease under stronger constraints. The generic matrix already passed
all added endpoint bounds to its numerical accuracy; the tightest cross
bound had slack7.39e-10. No useful separation gain was observed.

Defer an exact verifier extension for this route. This does not prove
the endpoint inequalities redundant in every possible instance. Reports,
both matrices and the executed implementation are preserved in
`runs/endpoint43-calibrated50-pair/`. Frozen proof checkers are unchanged.
