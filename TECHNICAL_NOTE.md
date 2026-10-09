# Technical note: a certified interval for minimum overlap

This packet's selected checkpoints establish

    .380627425 < mu < 0.3808585738345707361812673.

The claim is a computer-assisted bound. The two endpoints do not meet.
The arithmetic checks are reproducible; the analytic arguments below and
in the linked proof documents have been reviewed but are not formalized
in a proof assistant. No global priority or causal skill-efficacy claim
is made. This note explains the mathematical interfaces; execution
receipts and immutable manifests supply the separate finite evidence.

## Contract and return to the discrete problem

Partition {1,...,2N} into equal parts A and B. Minimize the maximum,
over all integer k, of the number of pairs with a-b=k, and divide by N.
The limit mu equals the continuous infimum of the peak of

    p(t) = integral h(x)g(x+t) dx,

where h is any measurable function on [0,2], 0<=h<=1, integral h=1,
and g=1-h on [0,2]. Both functions are zero outside that interval.
In particular g is not the global complement of the zero extension.

The equivalence has two directions. A balanced binary partition embeds
as a step density. Its overlap is affine between integer lag knots, so
its continuous peak equals the normalized discrete peak. Conversely,
fix a finite step density first, and independently assign the 2N indices
using its midpoint probabilities. For every nonzero shift the two
membership indices differ, so the expectation factors. Bounded
differences controls all shifts simultaneously; balancing the random
cardinality costs at most twice the number of changed memberships per
shift. For a fixed n-cell density of peak Q the resulting estimate is

    M(N) <= N Q + 4n+4 + 3 sqrt(12N log(4N)).

Zero-shift overlap is identically zero for an actual partition. Dividing
by N and taking N to infinity with n fixed proves the return. Cell
averages approximate every admissible measurable h in L1, preserve its
mass and box constraints, and change all correlations by at most
2 times the L1 error. Letting n grow only after the discrete limit closes
the equivalence. See [PROOF.md](outputs/minimum-overlap-refined14336-upper-checkpoint-v2/PROOF.md).

## Universal kernel premises

A lower certificate combines necessary inequalities obeyed by every
admissible density. Its frozen even kernel Q has two checked properties:

    integral Q(t)p(t) dt >= L(m),
    integral max(Q(t),0) dt <= D,

where L is a rational quadratic in the same first moment
m=integral t p(t) dt, and D is positive. Fourier positivity, periodic
box inequalities and phase-averaged Gram inequalities supply the first
property. Their exact coefficients, signs and source certificates are
part of the frozen kernel, not fitted assumptions about an extremizer.

For the Gram premise put r=2h-1 on [0,2], zero elsewhere, and average r
on a grid of cell width a=2/n with a uniformly random origin. Its n+1
cell averages sum to zero for every phase. The matrix X of their averaged
outer products is positive semidefinite and annihilates the all-ones
vector. Interior diagonal bounds are 1; the two endpoint bounds are
1/3. Averaging the grid origin identifies sums along the matrix diagonals
with triangular-hat averages of the autocorrelation of r. This identity
holds for every measurable admissible h, without assuming h is a step
function. It includes the diagonal k=0 case and the support endpoints.

The phase-centering error is periodic, has zero mean and Lipschitz
constant at most 2. A periodic L-Lipschitz function of period a has
variance at most L^2 a^2/48: integrate along the two arcs joining its
minimum and maximum, and use that its range width is at most La/2.
Thus the centering-error variance is at most a^2/12. For c_i=i*a and
|m|<=delta this gives the rational alias constraint

    c^T X c <= 1/12 + (delta/a)^2.

Rational dual coefficients are reconstructed from these formulas.
The restricted dual matrix is checked by integer Bareiss elimination
on the orthogonal complement of the all-ones vector. Diagonal repairs
are paid using the exact diagonal bounds. A floating SDP status or a
positive numerical eigenvalue is never a proof premise. A signed Gram
functional proves only its scalar functional inequality until the
continuous kernel return combines it into a peak bound. Details are in
[PHASE_GRAM_PROOF.md](work/minimum-overlap/history/PHASE_GRAM_PROOF.md).

The constant 1/12 remains sharp even at mean zero: an explicit symmetric
binary density attains it while having a large overlap peak. Thus mean
zero alone cannot strengthen this constant. A tighter restriction would
need further common-density information, such as a small peak cap. See
[the exact counterexample](work/minimum-overlap/history/ALIAS_SHARPNESS_AT_ZERO_MEAN.md).

## Keeping the common physical odd profile

Let H(t)=integral_0^t h. Autocorrelation cancellation gives

    d(t)=p(t)-p(-t)=H(t)+H(2-t)-1.

On [0,1], d is 1-Lipschitz, d(0)=0, |d|<=M for overlap peak M,
d(2-t)=d(t), and 2 integral_0^1 d=m. All these restrictions concern one
common function. They retain information lost by using independent
worst-case odd profiles for separate constraints.

Write A(t)=Q(t), B(t)=Q(2-t), c(t)=|A(t)|+|B(t)|. The pair sums at t
and 2-t each lie between |d(t)| and 2M-|d(t)|. Maximizing their weighted
contributions, with either sign of A and B, and integrating gives

    integral Qp <= M D - integral_0^1 c(t)|d(t)| dt.

Partition [0,1] into cells of lengths h_i, including every kernel jump
and its reflected breakpoint as boundaries. Write z_i for cell averages
of d and C_i=|integral_cell A|+|integral_cell B|. Then

    |z_i|<=M, |z_0|<=h_0/2,
    |z_(i+1)-z_i|<=(h_i+h_(i+1))/2,  2 sum h_i z_i=m.

Jensen gives C_i<=integral_cell c. Within each smooth cell the covariance
of c and |d| is bounded by h_i^(5/2)||c'||_2/sqrt(120). This follows
from the Green kernel min(s,t)-st/h_i and Cauchy-Schwarz. Summing the
cell errors gives

    E <= h_max^2 sqrt(E_Q/120),

where E_Q is the full piecewise derivative energy of Q. A jump is a cell
boundary, not a zero-cost global Sobolev derivative. An exact fixture
shows that ignoring this distinction would invalidate the bound.

For rational k_i in [-1,1], arbitrary edge flows v_i, and rational
tau,kappa, define the divergence as (-v_0,v_0-v_1,...,v_last), and put

    R_i=-k_i C_i-2 tau h_i-div(v)_i-kappa*1_(i=0),
    T=sum |v_i|(h_i+h_(i+1))/2+|kappa|h_0/2.

Finite summation by parts and the cell constraints give the return

    M >= [L(m)-tau*m-T-E] / [D+sum |R_i|].

Every coefficient residual is charged. Consequently the numerical LP
need be neither optimal nor feasible to propose usable rational flows.
The checker verifies |k_i|<=1 and computes all penalties outward.
See [EVEN_ODD_CAPACITY_RETURN.md](work/minimum-overlap/history/EVEN_ODD_CAPACITY_RETURN.md)
for the proof, normalization and discontinuity obligations.

## Finite arithmetic to a universal claim

The selected checkpoint uses an explicit radius return. Its three fresh
central integral checks actually execute target .380627424
and radius .00007. Their execution reports keep
those parameters. The positive-part denominator does not depend on the
mean radius. The separate exact deduction therefore reuses its outward
bound and recomputes L(0)+min(0,c)*r^2 at the narrower returned radius
.00004, to pass the global target .380627425. Both outer
implementations execute the global target. The fresh replay repeats the
integral checks before this deduction; enlarged radii and mismatched
execution parameters are rejected. See
[CENTRAL_RADIUS_RETURN.md](outputs/minimum-overlap-hybrid106-radius-pypy627425-v1-checkpoint/CENTRAL_RADIUS_RETURN.md).


Each returned rational interval uses the exact minimum of the numerator
quadratic and a positive denominator. The central interval, reflected
capacity intervals and Fourier outer intervals must cover every mean in
[-1,1]. Each bound must strictly exceed the selected target. The finite
minimum then gives a uniform strict margin, allowing the infimum over
all admissible densities. Isolated mean scores do not suffice.

The [lower checkpoint](outputs/minimum-overlap-hybrid106-radius-pypy627425-v1-checkpoint/README.md) contains the
frozen inputs and full replay entry point. Arb and standard-library
rational/dyadic arithmetic independently enclose the needed integrals.
The block primitive, where selected, uses outward integer sine/cosine
recurrences, resets from direct enclosures and falls back on the direct
evaluator at nonuniform points. Actual global audit, control suites and
fresh-copy executions are required after discovery and repair. Their
shared analytic premises remain visible in
[ANALYTIC_INTERFACE_AUDIT.md](work/minimum-overlap/ANALYTIC_INTERFACE_AUDIT.md).

## The upper witness and the remaining obstruction

The [upper checkpoint](outputs/minimum-overlap-refined14336-upper-checkpoint-v2/README.md) supplies a single
admissible rational nonuniform step density with 14337 cells. Cell-pair
overlap lengths are piecewise affine in the shift, with all knots among
differences of cell endpoints. Two exact arithmetic methods check the
mass, box constraints and all 86017 shift knots; affinity covers the
intervening shifts. Its exact peak is

    Q = 10919977028984812147789295189227209/28672000000000000000000000000000000.

The discrete return above proves mu<=Q. The displayed decimal upper
endpoint is rounded strictly outward. This gives an upper bound on mu,
without an optimality claim about the density.

The remaining obstruction is the gap between necessary realizability
conditions and an admissible density attaining the relaxed profile.
Virtual LP profiles are not upper witnesses. A two-sided integral bound
for one fixed kernel limits that kernel's return, not mu or other
kernels. Further progress needs a stronger universal kernel, a new
valid common-profile restriction, or a better explicit construction,
followed by the same original and fresh certification obligations.

A late, separately derived
[alias/interior-trace coupling](work/minimum-overlap/JOINT_ALIAS_TRACE.md)
retains a common energy budget that the independent alias and diagonal
bounds lose. Its physical fixtures and standalone signed-functional
checker are research evidence. This additional row is not used in the
selected production checkpoint and has not promoted a global bound.

The [current-kernel retargeting experiment](work/minimum-overlap/CURRENT_RETARGETING_RESULTS.md)
separately checks a strictly negative fixed-line derivative. The weaker
surrogate accepted by the production grammar retains that negative sign
after paying its scalar correction. Thus some local mean-zero improvement
exists, without an explicit globally certified target from this argument.
The central-only candidate and failed numerical prerequisites are retained
with their actual scope; they do not supersede the selected global proof.

The separate [dyadic subadditivity return](work/minimum-overlap/SUBADDITIVITY_RETURN.md)
uses the pointwise triangle inequality for a+b-2ab to derive
F(s+t)<=F(s)+F(t), where F(t)=p(t)+p(-t). Nonnegative hat weights
give signed affine kernel rows with zero scalar and mean penalties.
Its exact virtual-profile exclusion and outward fixed-line test are
research evidence; this row is not part of the selected global proof.
