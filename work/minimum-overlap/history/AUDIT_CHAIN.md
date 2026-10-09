# Review chain for the minimum-overlap certificates

This is a review guide, not an additional proof premise or a formal proof.
The decisive derivations are in PROOF.md, LOWER_PROOF.md, CIRCLE_PROOF.md,
PHASE_GRAM_PROOF.md and HYBRID_PROOF.md. Executed reports must match their
certificate and implementation hashes. Discovery solver output is not trusted.

1. The continuous class consists of real measurable h on [0,2], with 0<=h<=1
   and integral h=1. Put g=1-h on this interval and extend both by zero.
   The overlap p(t)=integral h(x)g(x+t)dx is nonnegative, supported on [-2,2],
   has integral1, and is continuous. The target is inf_h ||p||_infinity.

2. A balanced finite partition embeds as a binary density on2N equal cells
   of width1/N. Its overlap is affine between grid translates and its peak
   equals the normalized difference count. Conversely, cell-average any h,
   round the cells independently, control all nonzero shifts by bounded
   differences, and balance the random cardinality with o(N) flips. The
   zero shift of the binary rounding is0. The overlap perturbation obeys
   ||p_h-p_f||_infinity<=2||h-f||_1, so the rounding and balancing losses
   vanish uniformly in the shift. This gives the original finite limit.

3. For mean m=integral t p(t)dt, mass and box constraints imply |m|<=1.
   The second moment is exactly2/3+m^2/2. Completing a complex square gives
   integral p(t)cos(xi*t)dt <= (sin(xi)/xi)^2 for every real nonzero xi.
   Each retained decimal xi denotes an exact rational number in the checker.

4. Periodically extend h with period2. Its wrapped overlap q is even and
   q(s)=p(s)+p(s-2). Integer signed hypermetric inequalities follow by taking
   independent Bernoulli variables with the indicated h values: the signed
   cut sum is S(B-S)<=floor(B^2/4). Integrating in x and then over the stated
   phase cell gives the exact periodic kernel and its right side. This proof
   remains valid at coincident arguments; no binary assumption on h is used.

5. For r=2h-1 and a=2/N, average cell means over one translated grid phase.
   Their Gram matrix X is PSD, X*1=0, with endpoint diagonals<=1/3 and other
   diagonals<=1. The averaged diagonal sums are exactly triangular-kernel
   integrals of the autocorrelation. Thus y_k=b_k-(a/4)sum_i X_(i,i+k)
   are nonnegative overlap averages, each at most ||p||_infinity. No claim
   that an arbitrary relaxed matrix is realizable is needed or made.

6. The phase-center alias E_s has mean0 and is periodic2-Lipschitz. The
   periodic Lipschitz variance bound gives Var(E_s)<=a^2/12 and hence
   c'Xc<=1/12+(m/a)^2. Signed triangle inequalities follow pointwise on a
   cube. Every dual multiplier required to be nonnegative is checked as
   an exact rational. A PSD repair is charged to the diagonal bounds.

7. U=[I;-1'] spans1-perp. Integer Bareiss divisions and strictly positive
   leading minors certify U'GU positive definite. Since X is PSD with
   range in1-perp, trace(GX)>=0. The signed functional therefore gives
   F_j(p)>=L_j(0)-eta_j*(m/a_j)^2. It is a necessary inequality for every
   admissible h, rather than a claim of sharpness or strong SDP duality.

8. Combine Fourier, periodic and nonnegative multiples of signed Gram
   functionals into Q. Combine all coefficients of m^2 BEFORE minimizing
   over a mean interval. If integral p Q>=L and D>=integral max(Q,0), then
   ||p||_infinity>=L/D. Exact kernel breakpoints plus outward remainder
   bounds cover all t. Arb orders2and4 and a separate rational/trigonometric
   implementation check the central case. Both public and fourth-order
   implementations check the outer cases. An exact coverage audit must show
   their union with the central interval covers the entire [-1,1] mean range.

9. For an upper witness, check exact mass, box and all differences of step
   endpoints. The overlap is affine between these shifts, so their maximum
   is its entire continuum supremum. The fractional witness is checked by
   the unchanged nonuniform event maps and a separate packed-convolution
   anchor calculation. Their exact fractions must agree. Finite small-case
   tests complement these analytic arguments; they do not replace them.

10. A publication manifest binds coefficients, proof notes, implementations
    and executed reports. Copy to a fresh project-local directory and run
    the documented commands; compare manifests before and after. A proposed
    command, old report with changed dependencies, or partial mean cover
    cannot establish the displayed global bound. This remains a manually
    derived computer-assisted argument, without proof-assistant formalization.

No step here asserts equality of the two bounds, global priority, optimality
of a numerical search, or a causal effect of the reasoning skill.
