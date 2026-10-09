# Continuous Fourier phase proposal on a fixed mean bin

Status: derived under the same Fourier inequalities already checked by the
public outer grammar. No new lower bound is claimed by this note.

This completing-square perspective was already explored in the earlier
CONDITIONAL_PHASE_TILT.md experiment. That 76-row numerical run started
symmetrically and produced no certified improvement. The current route
revives the same inequality with asymmetric starting kernels, a larger
compatible active menu, and an executed return through the existing blend
grammar. The algebraic idea is not claimed as a new theorem, and these
uncontrolled changes do not identify a causal source of the improvement.

For frequency xi, write B=(sin(xi)/xi)^2. The accepted inequality is
E[cos(xi t)+alpha sin(xi t)] <= (1+alpha^2) B for every real alpha.
For a>0 and arbitrary b, multiply it by a and set alpha=b/a. The resulting
nonnegative-expectation coordinate is

    a(B-cos(xi t)) - b sin(xi t) + B b^2/a.

This retains the even cosine coefficient a while allowing its phase to be
chosen continuously. Its extra constant is a convex quadratic perspective.
Combined with the normalized nonnegative hybrid and outer coordinates in
ASYMMETRIC_BIN_PROOF.md, Q has E[Q]>=1 on the fixed mean bin. Positive-part
integration would then give mu>=1/integral(Q_+).

The discovery optimizer uses Gauss quadrature and optionally a smooth upper
approximation to positive part. For epsilon>0, this approximation equals zero
below -epsilon, q above epsilon, and (q+epsilon)^2/(4epsilon) between. Its
pointwise excess is at most epsilon/4, hence its continuous integration excess
on [-2,2] is at most epsilon. Quadrature error is a separate unresolved
discovery error. No quadrature objective is a certificate.

The return uses the existing hybrid-outer-blend-v1 grammar: remove the selected
cosine multipliers from the hybrid block and add outer cos+asin terms with
lambda=2a and alpha=b/a, using theta=1/2. Normalize the remaining hybrid block
exactly as in ASYMMETRIC_BIN_PROOF.md. Rounded decimals define a fresh candidate;
the unchanged Arb and integer compilers recompute every RHS and normalization.
This avoids a new trusted proof grammar. Full mean coverage and fresh replay
are still required for a global claim. Numerical convergence proves no
optimality and the source status of the open problem is unchanged.

Several rotated coordinates at one frequency can be merged before a warm
start. For a_i>=0, alpha_i real, a=sum a_i and b=sum a_i alpha_i, Cauchy's
inequality gives b^2/a <= sum a_i alpha_i^2 when a>0. Thus merging preserves
the oscillatory coefficients and reduces the constant by a nonnegative
weighted variance times B. An unrotated cosine is included with alpha=0.
The discovery code checks the floating difference with a stated tolerance;
the rounded returned kernel is checked afresh, so that tolerance is never
used as a proof premise. Canonical active-menu unions retain coordinates
that prior numerical exports assigned zero weight.

Executed local test on [0.00285,0.00290]: the first continuous-phase return
passed both unchanged outward Taylor orders at target 0.380625100. Their
lower enclosures exceed 0.38062515038365564. A bounded warm polish passed
the fourth-order checker above 0.38062516517479665. The wider interval
[0.00290,0.00300] passed above 0.38062502931248838. These are conditional
results. Independent integer replay of the first phase candidate passed in
1294.914 seconds, with exact lower bound displayed as 0.3806251503827875.
Its compiler consistency controls also passed, checking all 3512 affine-piece
pairs as well as jets, primitives and malformed input rejection.
The next wider interval [0.00300,0.00310] missed the
numerical 0.380625000 gate, so no full phase cover was produced by that run.
All failures and numerical limitations are retained. Restarting from the
older larger-mean kernel tests whether the stalled warm continuation is
an optimizer limitation; neither failure proves a mathematical barrier.

Signed sine coordinates give a further valid extension. For a decimal
frequency xi, let B_s be the public sine RHS
2 abs(sin(xi)/xi) sqrt(max(0,1-(sin(xi)/xi)^2)). Both signs obey this
bound. Thus any real c gives the valid nonnegative-expectation coordinate
abs(c) B_s-c sin(xi t). At an exact nonzero integer multiple of pi,
B_s=0, consistently with the exact odd reflection identity. Decimal
frequencies retain their small nonzero RHS in every proof replay.

The v5 search added 64, then 128, free signed near-integer-pi coordinates.
The return uses existing sin or -sin terms with theta=1/2 and lambda=2abs(c).
No proof grammar or checker changed. The 64-sine wide29 candidate passed
both outward orders above 0.38062519178858211. The 128-sine warm polish
passed the fourth-order checker above 0.38062566814896135. These statements
cover only [0.0029,0.0030], with independent integer and global replay
obligations recorded separately. No new global bound follows from them.

The v6 warm start merges terms only when their rational decimal frequencies
are exactly equal. For coefficients c_i, replacing their separate costs
B_s sum abs(c_i) by B_s abs(sum c_i) preserves the oscillatory coefficient
and reduces the constant by the nonnegative triangle-inequality difference.
Exact rational coefficient sums precede floating discovery. Nine exact
aggregation fixtures supplement the existing gradient and export controls.
All rounded returned kernels still require fresh outward checks.


The v7 discovery partition removes a base-cell boundary only when every
active step coordinate has identical values on both sides, and retains
every exact functional knot. It checks all original open pieces against
the compressed partition, including the affine functional coordinates.
This preserves the entire active search family, rather than only the
current weighted kernel. Smooth cosine/sine/quadratic terms need no step
boundary. The quadrature nodes change, so numerical integration errors
remain unresolved until the unchanged continuum checkers accept a return.
The first pilot compressed 4734 positive pieces to 900 and checked all 240
active rows, with 1535 discovery calls completed in 56.897 seconds. This
is a performance observation under changing machine load, not a causal
comparison or a continuum certificate.
