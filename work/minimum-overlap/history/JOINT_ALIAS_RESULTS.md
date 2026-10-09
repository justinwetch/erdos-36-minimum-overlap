# Joint alias/interior-trace continuation status

The analytic derivation is in JOINT_ALIAS_TRACE.md. The new row is separate
from the selected production checkpoint; no global bound has been promoted
using it. No novelty, optimality or causal skill-efficacy claim is made.

Twenty-four exact physical fixtures passed. Three exact matrix/scalar
reconstruction fixtures and six malformed-input rejections passed for the
standalone checker. Six zero-mean physical densities attain the old1/12
constant, so the new gain requires the common interior-trace information.

The previous SCS matrix has joint-row left side0.17675212005338548 against
2/19=0.10526315789473684. Its negative eigenvalue is retained; it is not
treated as PSD or realizable. Matched baseline and added-row fits used the
same profile,127cells, initial177triangle rows and solver budgets. Final
actual mismatches were 0.014858581589269323 and
0.014866090093800854. Both were optimal_inaccurate,
with different subsequent cut choices and PSD defects. Their small final
score difference does not prove the row's effect on an optimum.

## Exactly checked signed functional

The new certificate is certificates/hybrid97-joint-alias-functional-v1.json,
SHA-256 e393d52d64a9dc1ce3a0f78efae68ed57d75412974d91a8718b5f17e60e097f1. Its signed hat weights obey the scalar
functional lower bound

    L = -1176054977768635829720567732488054265733/24130000000000000000000000000000000000000.

Its decimal value -0.048738291660531945 is NOT a bound on mu.
Relative to the weaker old-schema surrogate for this same dual matrix,
the new analytic premise supplies the exact positive scalar correction

    11317190099656291627/5791200000000000000000000.

Diagonal PSD repairs were paid explicitly. The unchanged integer Bareiss
implementation checked the127-dimensional restricted matrix. Original and
fresh standalone executions both passed, with all frozen source/input
hashes unchanged. The actual raw proposal was rejected by the old verifier,
and the completed new certificate was rejected by the production hybrid
parser, as intended. The fresh receipt and root review are
runs/hybrid97-joint-alias-functional-replay.json and
runs/hybrid97-joint-alias-functional-root-review.json.

A portable standalone replay from this research directory is:

```powershell
python verify_joint_alias_functional.py certificates/hybrid97-joint-alias-functional-v1.json --target=-1 --out runs/continued-joint-functional-check.json
```

The conservative target-1 is just an acceptance gate; the checker computes
and reports the exact L above. This replay uses the unchanged PSD checker
and the hash-bound manually reviewed analytic lemma, not a proof assistant.

## Remaining bridge

A bounded numerical kernel probe uses the fresh-checked functional. Its
exports have an explicitly unsupported diagnostic schema. Before any
production use, implement a separately versioned continuous-kernel return,
check all-mean coefficients and positive integrals independently, cover
every mean and execute a full fresh global replay. Standalone functional
acceptance does not discharge these obligations. The incumbent global
bound remains whatever the independently reviewed production checkpoint
records.

## Current-kernel discriminator: no gain

The independently fresh-checked new functional was appended at zero weight
to the frozen H97 kernel in a separate numerical oracle. Its added-coordinate
gradient was 0.0024913475817811559, so the bounded test selected
coefficient zero and returned no gain. The initial and final numerical
mean-zero scores were both 0.38062742560603202. Source hashes
were unchanged. The result is runs/hybrid97-joint-alias-kernel-probe-v1/summary.json.

This is a local numerical directional test at one fixed seed, not an
optimality certificate or a ceiling on other duals using the lemma. It
does not justify a new production proof pipeline for this particular
candidate before the deadline. Retain the derived common-energy inequality
and exact signed-functional witness, preserve the failed direction, and
seek a discriminator tied to the remaining actual kernel/profile obstruction
before investing in a new end-to-end return. The production grammar and
selected global bound remain unchanged by this route.
# Exact virtual-profile separation

**Interpretation correction:** the literal step profile's discontinuities
already force uniform distance at least 0.19035359916369549 from every
continuous overlap. That dominates the smaller functional distances
below, so those literal uniform exclusions are redundant. Their useful
replacement compares the smoothed hat-average vector and first moment;
the exact exclusions and the circular-row outcome are recorded in
[CIRCULAR_ALIAS_RESULTS.md](CIRCULAR_ALIAS_RESULTS.md). No profile exclusion
is a new bound on mu.

The numerical no-gain observation for this functional has since gained an
outward arithmetic check on the fixed added-coefficient line. See
[FIXED_LINE_DIRECTION.md](FIXED_LINE_DIRECTION.md). Its derivative has a
strictly positive lower endpoint, so convexity proves that line cannot
improve the fixed kernel. This says nothing about reoptimizing the other
coefficients. The stronger circular endpoint premise is separately
derived in [CIRCULAR_ALIAS_TRACE.md](CIRCULAR_ALIAS_TRACE.md); its numerical
test and standalone compilation have their own evidence and do not alter
the frozen original functional.

The standalone functional also quantitatively excludes one literal trial
profile. `evaluate_joint_alias_profile.py` rationalizes the 65536 values in
`runs/hybrid92-inactive-profile-v1/primal.json` and normalizes their exact
mass to one. The original mass is
163840000000000002111203/163840000000000000000000, so this adjustment is
explicit and negligible in size. The profile remains a virtual even step
profile, not an admissible overlap construction.

Exact integration against the signed affine kernel gives a positive gap
between the certified functional lower bound and this profile's value.
Dividing that gap by the exactly integrated kernel L1 norm proves that
every admissible overlap with mean zero has uniform distance at least
0.01095756057165429 (display rounded; the exact rational is in
`runs/hybrid97-joint-alias-profile-separation.json`) from this normalized
profile. Equivalently, the open uniform ball of that exact radius contains
no such overlap. Seven exact integration and kernel-norm checks pass.

The separation extends to arbitrary means. Write the exact all-mean
functional as `integral p K >= L0-beta*m^2`, with beta nonnegative.
The even normalized trial profile p0 has first moment zero. If
`epsilon=||p-p0||infinity`, support in [-2,2] gives
`|m|<=epsilon*integral |t|dt=4*epsilon`. Consequently
`L0-integral p0 K <= ||K||1*epsilon+16*beta*epsilon^2`.
Exact rational bisection of this monotone scalar polynomial proves
that every admissible overlap, with arbitrary mean, is at uniform
distance strictly greater than **10776750361/1000000000000**
(0.010776750361) from this normalized profile. The scalar root lies
between that rational and the rational one trillionth larger; the upper
endpoint is not an upper bound on any realizable profile's distance.
An additional exact quadratic-root fixture passes.

This is a separation of one profile, not a new bound on mu, and does not
show that the joint row is necessary to refute that profile. Its smaller
predecessor functional already had a positive separation gap. The proof
is the signed-functional inequality followed by
`|integral (p-p0) K| <= ||p-p0||infinity * ||K||1`.

Replay from the research directory:

```powershell
python evaluate_joint_alias_profile.py --profile runs/hybrid92-inactive-profile-v1/primal.json --certificate certificates/hybrid97-joint-alias-functional-v1.json --receipt runs/hybrid97-joint-alias-functional-replay.json --out runs/continued-joint-profile-separation.json
```

