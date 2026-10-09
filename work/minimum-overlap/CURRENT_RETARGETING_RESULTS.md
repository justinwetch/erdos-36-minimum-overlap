# Retargeting the signed functional to the current kernel

The older joint and circular functionals separated the old H92 virtual
profile. Their outward derivatives against the current H97 kernel were
positive. Those checked fixed-line failures did not rule out fitting a
different functional to the current kernel. This was the deciding
difference for the final discriminator.

The new sampled positive-set profile has mass close to one, but its
second-moment residual is approximately -0.000850579151. It is a discovery
target, not an admissible overlap or a feasible full-relaxation witness.
Its sampled root list is not a certificate of complete root isolation.

The 127-cell circular fit was compiled as a separate signed functional.
Original and fresh-copy exact checks passed, including 127 positive
restricted Bareiss minors. Root review is in
`runs/hybrid97-joint-current-circular-functional-root-review.json`.
The stronger schema remains rejected by the frozen production grammar.

## A useful direction, with limited scope

The numerical current-kernel search reports a gain of approximately
1.01902e-9 in its mean-zero discovery score. More decisively, the
unchanged outward derivative checker gives the interval

    [-0.0119639710831730, -0.0119206645262808].

These displayed endpoints abbreviate the exact rationals in
`runs/hybrid97-joint-current-circular-direction-enclosure.json`.
For the fixed line Q_rho=Q+rho*(K-L), rho>=0, the strictly negative
right derivative proves that some sufficiently small positive coefficient
decreases the positive-part denominator. The mean-zero numerator is
preserved, so the fixed mean-zero kernel ratio strictly improves.
This does not specify a globally certified target or cover other means.

The weaker surrogate already accepted by the production grammar also has
a negative direction. Its scalar lower bound differs by the exact positive
delta recorded in `runs/hybrid97-joint-current-circular-direction-review.json`.
Changing the affine direction by this constant increases the right
derivative by a number between zero and 4*delta, because the support has
length four and the positive-part map is monotone and 1-Lipschitz.
The resulting derivative interval remains strictly negative:

    [-0.0119639710831730, -0.0119169358881853].

Thus the extra circular premise is not required for this local improvement.
The numerical proposal was also exported with that weaker, accepted
surrogate for central-only tests under the unchanged `hybrid_certificate.py`.
Both original fourth-order outward tests passed: the mean-zero target
0.380627426 and the target 0.380627425 for |m|<=0.00007. The latter
enclosure is approximately 0.3806274252809042949175884667.
The separate second-order Taylor enclosure also passed the same central
target, at approximately 0.3806274252809042395291104857. Both use Arb;
agreement between Taylor orders is not an independent integer proof.
Consult `runs/hybrid97-joint-current-weaker-return-v1/` for actual test
reports. Passing those tests does not supply an independent
integer enclosure, a complete mean cover or a full fresh global replay.

To replay the direction and its exact surrogate interpretation from this
research directory, use fresh output names:

```powershell
python enclose_added_functional_direction.py runs/hybrid97-newrow-capacity627424-v1/central-frozen.json certificates/hybrid97-joint-current-circular-functional-v1.json runs/hybrid97-joint-current-circular-functional-replay.json --out runs/continued-current-direction.json
python review_current_direction.py --out runs/continued-current-direction-review.json
```

The review command reads the retained original enclosure and verifies its
source identities. Packet validation separately executes the enclosure
again and compares its exact endpoints before replaying the interpretation.

## Prerequisite failures retained

Current-profile mass/moment calibration stopped at its cycle limit with
its acceptance gate false. Two finite primal LP attempts, with 65536 and
8192 cells and 299 necessary rows, hit the solver time limit. A different
19-row formulation aggregated the Fourier inequalities using their current
nonnegative weights and also hit the time limit. No accepted primal
profile was serialized by these attempts; all dependent SDP workflows
stopped at their prerequisite gates.

The solver's time-limit messages are not proofs of infeasibility or
optimality. The aggregate Fourier formulation preserves that weighted
necessary inequality but relaxes the individual Fourier constraints. Even
a successful finite LP would not prove full circle feasibility or original
overlap realizability. Do not repeat the same failed numerical formulation
without identifying and testing a different obstruction.

A fourth attempt changed the aggregate LP algorithm from interior point
to dual simplex, retaining the relaxation, tolerances and ninety-second
solver budget. It also stopped at the time limit without an accepted
profile. The total observed wall time was about 150 seconds, including
assembly and solver overhead. Its dependent SDP route stopped at the
same prerequisite gate. No further LP retry was started.

The strongest fully promoted global checkpoint is identified by the packet
README and proof receipts. The results on this page are continuation
evidence and do not supersede that checkpoint.
