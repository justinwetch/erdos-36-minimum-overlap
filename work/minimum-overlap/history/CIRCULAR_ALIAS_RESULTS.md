# Circular-row outcome and observable separation

The analytic strengthening is in the immutable
[CIRCULAR_ALIAS_TRACE.md](CIRCULAR_ALIAS_TRACE.md). Its opening status was
written before compilation. Subsequent evidence below establishes a
standalone signed functional, with no production grammar or global bound.

The numerical 127-cell fit used the same initial 177 triangle rows and
300-second solver budgets as the earlier joint-row experiment. Its final
actual mismatch was 0.014939202873420918, with PSD defect approximately
-3.04339e-6. Later triangle selections and solver inaccuracies differ;
these runs do not establish exact SDP optima or a causal row comparison.

The proposed dual was repaired with paid rational diagonal costs. The
separate circular checker reconstructs the old joint matrix plus the
exact endpoint rank-one term, then checks restricted positive definiteness
by the unchanged integer Bareiss implementation. The scalar lower bound
is -720653607708495019831165252922801606537 /
14478000000000000000000000000000000000000. This is a signed-functional
value, not a lower bound on mu. Original and fresh-copy checks pass, with
127 positive leading principal minors. Root review is recorded in
`runs/hybrid97-joint-circular-alias-functional-root-review.json`.
Both the raw proposal and completed circular certificate are rejected by
the old production grammar, as required.

The current-kernel numerical probe chose added multiplier zero, with no
gain and initial derivative 0.0022560064026038162. Its separate outward
derivative enclosure is approximately
[0.00221187026173990,0.00229984640346147]. The strictly positive exact
lower endpoint and the convexity argument in
[FIXED_LINE_DIRECTION.md](FIXED_LINE_DIRECTION.md) reject this fixed line
for every positive coefficient. Joint reoptimization remains open.

## Correct interpretation of profile separation

The earlier literal uniform-profile exclusions were mathematically valid
but redundant: the trial step function has jumps. Continuity of every
actual overlap already gives uniform distance at least approximately
0.19035359916369549, larger than either functional's literal uniform
distance result. Those receipts are preserved as a checked dead end.

The useful finite-observable version compares **smoothed hat averages**.
Let y be the overlap's vector of the 128 normalized hat integrals at
scale n=127, and let y0 be that vector for the exactly mass-normalized
virtual profile. For a signed functional with weights gamma and the
all-mean return L0-beta*m^2, put gap=L0-gamma.dot(y0)>0. At mean zero,

    ||y-y0||infinity >= gap / sum|gamma|.

For arbitrary means, use the explicitly defined joint-observable distance
rho=max(||y-y0||infinity,|m|). The same inequality implies

    gap <= (sum|gamma|)*rho + beta*rho^2.

Exact rational root bracketing gives the following exclusions:

| Separately compiled functional | Mean-zero hat-vector distance, display | Arbitrary-mean joint-observable distance, strict rational lower bound |
|---|---:|---:|
| Original joint alias/interior trace | 0.01075546667298901 | 10744440867/1000000000000 |
| Circular merged endpoint | 0.010846165033107268 | 2700935801/250000000000 |

These are two constructed separators of one common vector, not optimal
distances and not a causal measurement of the extra row. The hat-vector
code integrates each observable independently, checks that its exact dot
product equals the independently organized affine-kernel integral, and
checks constant-profile and refinement fixtures. This formulation avoids
using the literal trial profile's discontinuities as the exclusion.

Receipts are `runs/hybrid97-joint-alias-hat-separation.json` and
`runs/hybrid97-joint-circular-alias-hat-separation.json`. For example:

```powershell
python evaluate_hat_profile_separation.py --profile runs/hybrid92-inactive-profile-v1/primal.json --certificate certificates/hybrid97-joint-circular-alias-functional-v1.json --receipt runs/hybrid97-joint-circular-alias-functional-replay.json --out runs/continued-circular-hat-separation.json
```

The production lower-bound frontier is unchanged by these experiments.
A more useful new functional, or joint optimization with a different
kernel, still needs a separately reviewed continuous return and complete
global/fresh proof before it can improve the bound on mu.
