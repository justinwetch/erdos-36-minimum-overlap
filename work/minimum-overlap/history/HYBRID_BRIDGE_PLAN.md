LATEST October 08, 2026, 07:38 UTC: global .380588792, hybrid21-checkpoint40files, ALL8freshpackagedchecksPASS. Later research is in NEXT.md. Older status paragraphs below are historical.

LATEST October8 07:06UTC: global .380583137, spectral-checkpoint37files,
ALL8freshpackagedchecksPASS. The rest of this plan is historical. Read
NEXT.md and HYBRID_PROOF.md for current status and decisive dependencies.

# Historical bridge plan: continuous Fourier/circle/Gram-functional certificate

UPDATE October8 06:21UTC: the continuous return and global mean coverage
below have now been implemented and checked. Strongest GLOBAL target is
.380575919, with 24/48-cell signed functionals. Both Arb orders, stdlib
integer central, both174-binouterimplementations, fullcoveraudit and all7
freshpackagedreplaycommandsPASS. Read HYBRID_PROOF.md and current NEXT.md.
Published35files outputs/minimum-overlap-hybrid17-checkpoint. Next deciding
test is N96profilecompatibility; one bounded fit is running. The original
proposal-stage wording below is retained as historical reasoning, not the
current verification status.

This is an implementation plan for a **proposed** improvement, not a proof
of that improvement. Global verified bounds remain
.380565779 < mu < .3808585738368000599384507.

## Executed input

Six signed Gram functionals have exact rational PSD certificates, all on
|mean|<=.002042269461. Their source files, in LP-row order, are:

1. certificates/phase-gram-functional24-frozen.json
2. certificates/phase-cuts24b-iter2.json
3. certificates/phase-cuts24b-iter3.json
4. certificates/phase-cuts24b-iter4.json
5. certificates/phase-cuts24b-iter5.json
6. certificates/phase-cuts24b-iter6.json

Reports are runs/phase-gram-functional24-integer-replay.json and
runs/phase-cuts24b-iter{2,...,6}-integer.json. The checker is
verify_phase_gram.py, standard library only. All 24 leading principal minors
are positive after exact diagonal repairs. check_phase_gram.py passed 6,996
exact mapping/sharpness fixtures; check_phase_gram_dual.py passed 137 independent
aggregation and Bareiss fixtures. PHASE_GRAM_PROOF.md derives the universal
phase return, signed functional implication, and sharp 1/12 alias bound.

The first exact row excluded the literal relaxed profile by .0026882544 in
its signed functional. Subsequent numerical LP escapes, each with an exact
new row, raised the relaxed cap from .3805671919792061 to .38057008158572897.
Those are discovery caps, not upper bounds on the original problem. The
campaign summary is runs/phase-cuts24b-summary.json. Six rows are in
runs/phase-cuts24b-iter6-allcuts.json; float coefficients are discovery only.

extract_hybrid_seed.py matched every rational LP row coefficient to its
exact proof functional and exported certificates/hybrid6-grid-proposal.json.
Only three functionals, 78 cosine rows and five periodic families have nonzero
LP dual multipliers. This is an untrusted continuous proposal. A midpoint
diagnostic gives mean-zero .3805677007 and, at the old mean cut, .3805669995.
The loss from the grid relaxation is real; no outward replay has run yet.
See runs/hybrid6-grid-proposal-diagnostic.json. The numerical numerator L(0)
is .3805711036576 and the coefficient of mean-radius squared is -.1681313917.

## Exact new certificate meaning

The schema-v5 proposal contains the original schema-v2 Fourier/circle fields
and embedded, independently checkable signed functional certificates with
nonnegative multipliers mu_j. On t>=0, functional j has the piecewise affine
kernel with knots t=k*a_j, a_j=2/N_j, and knot values

    K_j(0)=gamma_j,0/a_j,
    K_j(k*a_j)=gamma_j,k/(2*a_j), 1<=k<=N_j.

Its exact lower value L_j(delta) comes from compile_dual after replacing that
embedded certificate's mean_abs_max by the desired radius delta. This is
valid: its PSD matrix does not depend on delta, only the analytic mean RHS
does. In particular

    L_j(delta)=L_j(0)-eta_j*(delta/a_j)^2.

Do not trust any stored float RHS. Recompile and check each embedded matrix.
The hybrid test function and numerator are

    Q(t)=y0+y2*t^2+sum z_xi*cos(xi*t)+periodic_steps(t)+sum mu_j*K_j(t),
    L(delta)=L_base(0)+y2*delta^2/2+sum mu_j*L_j(delta)

for y2<0. A nonnegative y2 instead uses its minimum mean-square contribution
on the mean interval. Thus integral p*Q>=L(delta), and a certified upper
D>=integral max(Q,0) gives mu>=L(delta)/D on this central interval. Negative
L_j values are legitimate functional lower values, not bounds on mu.

## Verification to implement first

Create new checker files; keep the previously published checkers unchanged.
An Arb verifier can reuse the original term/jet/antiderivative mathematics,
but it must split at the union of every exact periodic step boundary and
every rational hat knot. Intervals have rational endpoints: use Fraction
bisectors and arb(numerator)/denominator, avoiding decimal-rounded gaps.
On each piece the additional kernel sum is exactly u+v*t. Add u+v*c to q(c),
v to q'(c), and u*(b-a)+v*(b^2-a^2)/2 to its integral. The second/fourth
derivative remainder bounds are unchanged. Run both Taylor orders.

The independent integer checker can inherit GeneralChecker's smooth jet,
primitive and dyadic arithmetic, while independently compiling the periodic
families. Its new per-piece integral and derivative use the exact rational
affine coefficients. Replay every embedded Gram PSD certificate. Give the
new checker and its dependencies hashes in the result. Verify assembly against
exact fixtures before relying on it. A tiny-multiplier or zero-functional
reduction to the known schema-v2 certificate is a useful control.

## Continuous discovery after a first correct replay

Extend the continuous Oracle in a new file. It currently handles uniform step
cells. Use the union of step boundaries and functional knots, about 4,120
pieces rather than their 12,288-cell common refinement. Retain a mapping from
each new piece to its old circle cell when accumulating gradient lengths.
Functional primitives are exactly piecewise quadratic; evaluate them at
proposed roots for the gradient. Missed roots remain possible in discovery;
the complete interval verifier decides the proof.

In the old normalization E Q>=1, add nonnegative coefficients times
K_j-L_j(0). The exported constant therefore subtracts sum mu_j*L_j(0),
while the actual polynomial/cosine/circle coefficients retain their meanings.
The numerator at mean zero is then 1. Check gradients on independent fixtures
and retain best whole-file proposals. Finite LP seed multipliers are not
optimizer guarantees or proof premises.

## Join and global obligation

Only after the central replay passes, adjust the outer mean join. The effective
coefficient for a circle_join-style formula is

    y2_effective = y2 - 2*sum mu_j*eta_j/a_j^2.

Use L(0), the rigorously bounded D, and this coefficient when searching for
a cut in source bin 103 [.0015625,.00234375], trimming its mirror bin 86.
At a target around .380567-.380569, ordinary coarse outer bin 112 is still
above target (~.380584), but execute every required outer bin at the actual
new target. Both fourth-order and unchanged public second-order replays are
required. The original checker may need cell width .00001.

audit_circle.py assumes two Arb central reports; build an explicit hybrid
audit that also binds the embedded PSD checks, independent integer replay,
checker hashes and exact full mean cover. Do not modify old passed reports
to pretend they executed a stronger target. Publish a new distinct output
checkpoint only after all obligations pass, with a copied-checker replay and
manifest validation. Then update the progress report and strongest-bound
records. The final ZIP is still due at the campaign deadline, with a fenced
ready-to-copy continuation prompt and companion text file.
