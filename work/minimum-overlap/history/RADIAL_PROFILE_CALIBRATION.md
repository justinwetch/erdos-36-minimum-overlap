# Calibration before another phase separator

Status: implemented and executed as a numerical discriminator. Independent
32/64 geometry and the unchanged outward mean-zero checker passed. This
does not establish overlap feasibility or complete root isolation.

`calibrate_hybrid_profile.py` passed smooth, kink and unbracketed controls
and four exact moment fixtures. A kink-control failure and an initial
JSON serialization failure are preserved. The fresh successful run is
`runs/hybrid50-profile-calibration-v2`: three cycles, 46.5074 seconds,
sampled mass 1.000000002158017 and moment .666666668006941. The 32/64
geometry agrees to 4.9e-15 in D and 1.04e-10 in the gradient. The unchanged
Arb4 mean-zero bound is .3806111055934610371394712; this alone is not global.

A 65536-cell export with a 32-subdivision oracle has mass one and moment
.6666666668365571. The older 32768-cell export exceeded the unchanged
1e-8 moment-error gate and remains a failed diagnostic. The new profile
is virtual, not an actual h. A fitted order43 functional passed exact
positive-definiteness checks and a compact sparse pilot reached numerical
mean-zero .38061111572744283. Its independent outward check is recorded
separately; no global promotion follows from these experiments.

The deep48 optimizer improved D but left v dot gradient D = +.00397568;
the full50 pilot reduced this only to +.00155281. Its positive-set density
cannot simultaneously use cap 1/D and have exact mass one. Normalizing by
the positive-set volume hides that mismatch by changing the cap. A phase
separator fitted to this uncalibrated profile may target a defect already
charged by the existing scalar/second-moment constraints.

With normalized numerator one, write Q_v(t)=1+v dot Phi(t), and
D(v)=2 integral_0^2 Q_v(t)^+ dt. Away from a zero set of positive measure,
differentiation gives

    v dot gradient D = D - V,   V=2 measure{Q_v>0}.

Along a radial line this derivative identifies the mass error of
p(t)=1_{Q_v>0}/D: its full symmetric mass is V/D. The y2 coordinate a
uses Phi_0(t)=2/3-t^2, so

    gradient_a D = 2 integral_{Q_v>0} (2/3-t^2) dt.

If both gradient_a D=0 and v dot gradient D=0, this virtual p has mass one,
cap 1/D and second moment 2/3. It need not satisfy any other overlap or
phase constraints. It is never an actual construction or upper bound.
For current a>0 and finite cosine/affine pieces, Q is nonconstant analytic
inside each piece; its zero set has measure zero. Boundary jumps have
measure zero. New parameters reaching a=0 require rechecking this condition
or using subgradients and fractional values on a zero interval.

A two-variable calibration fixes w=(all coordinates except a) and varies
(b,s) in v'=(b,s*w), b>0,s>0. D is convex in these two variables. Interior
stationarity in both variables implies the two identities above. One
possible cheap discriminator is alternating bounded derivative bisection
on b and s, preserving the best actual numerical objective and recording
the calibrated proposal separately. Check monotonic derivatives, sampled
32/64 geometry, mass/moment residuals, and unchanged outward score. Do not
declare calibration from objective agreement alone or loosen existing
derivative gates. If it fails or costs too much, keep the valid certificate
and the explicitly uncalibrated profile; no feasibility inference follows.

Only if calibration succeeds with negligible outward score loss should a
new phase fit target that continuous positive-set profile. This changes
the adversary from the earlier grid-relaxation profile while keeping the
same exact supported functional grammar and final global proof obligations.
The numerical cap gains from59/61 grids are larger than their observed
continuous effect, so this is a deciding alternative to more prime grids.
