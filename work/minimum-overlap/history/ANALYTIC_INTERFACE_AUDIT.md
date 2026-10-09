# Review of the analytic interfaces

This is a human-readable mathematical review, not an executed arithmetic
certificate or a proof-assistant verification. The finite arithmetic reports
and their fresh replays remain separate evidence. The open problem is not
resolved by the interval bounds in this packet.

## Discrete and continuous quantifiers

For a fixed admissible finite step function, midpoint Bernoulli sampling
factorizes each nonzero-shift expectation because the two indices differ.
The zero-shift count of an actual partition is identically zero and is
excluded from this factorization. A membership flip affects a fixed shift
count by at most two, including after earlier balancing flips. With 2N
variables, bounded differences gives exp(-u^2/(4N)); the cardinality event
has probability at most 2 exp(-u^2/N). The stated u=sqrt(12N log(4N)) pays
for all shifts and the cardinality event simultaneously. The finite step
count stays fixed while N tends to infinity.

Cell averaging an arbitrary admissible measurable density preserves its
box and mass constraints and converges in L1. The product identity gives
uniform overlap error at most twice that L1 error. Thus the fixed-step
return extends to the continuous infimum. Conversely each balanced binary
partition is an admissible step density, and its overlap is affine between
integer lag knots. These two directions establish the limit equivalence
used in PROOF.md without exchanging the two limiting operations.

## Physical odd profile

Writing H(t)=integral_0^t h, cancellation of the autocorrelation terms
gives d(t)=p(t)-p(-t)=H(t)+H(2-t)-1 on [0,2]. Consequently d(0)=0,
d(2-t)=d(t), and d'=h(t)-h(2-t) belongs to [-1,1] almost everywhere.
The first moment is m=2 integral_0^1 d. If the full overlap peak is M,
then |d|<=M. These restrictions are imposed on one common profile;
separate witnesses for separate restrictions would not suffice.

For an even kernel, the pair sums at t and 2-t lie between |d(t)| and
2M-|d(t)|. Maximizing both pair contributions yields the quartet bound
in EVEN_ODD_CAPACITY_RETURN.md, with coefficient |Q(t)|+|Q(2-t)|.
No sign or nonnegativity assumption on Q is needed.

## Phase-averaged Gram premises

For each phase the N+1 cell averages of r=2h-1 cover its entire support
and sum to zero. Their averaged outer product is positive semidefinite
and annihilates the all-ones vector. Endpoint cells have squared-length
average 1/3; interior cells have diagonal bound 1. The probability that
two points occupy cells with a fixed ordered index difference is the
triangular hat. This gives the stated autocorrelation trace identity,
including both orders in a diagonal cell square. Integrating the support
triangle at its two corners gives b_0=1/2-a/12 and b_N=a/24.

The phase-centering error is a zero-mean, a-periodic function with
derivative -a times the sampled sum of r, hence Lipschitz constant at
most 2. For a periodic L-Lipschitz function with range width D<=La/2,
the two arcs between a minimum and a maximum give variance at most
D^2/4-D^3/(3La)<=L^2 a^2/48. Therefore its variance is at most a^2/12.
The mean-cross-term vanishes before the squared mean restriction is
used, giving c^T X c<=1/12+(delta/a)^2. These are all necessary conditions
for a common phase-averaged matrix, without a realizability assertion.

Finally the rational restriction matrix has columns spanning the
orthogonal complement of the all-ones vector. Positive definiteness of
the restricted dual matrix, as checked by exact Bareiss elimination,
therefore makes its trace against every permitted X nonnegative. Any
diagonal repair is paid using the exact diagonal upper bounds. Signed
functional rows retain their scalar functional conclusion until a
separate continuous-kernel certificate combines them into a peak bound.

## Covariance and discontinuities

On one smooth cell of length h, the centered-product Green kernel is
min(s,t)-st/h. Its integral in t is s(h-s)/2, and the squared L2 norm
of this last function is h^5/120. This proves the covariance constant
h^(5/2)/sqrt(120) against a 1-Lipschitz function. Absolute values of a
smooth kernel remain absolutely continuous, so its zero crossings create
no omitted jump costs. Actual kernel jumps must be cell boundaries.

For c(t)=|Q(t)|+|Q(2-t)|, its derivative energy on [0,1] is at most
the full piecewise derivative energy of the even Q on [-2,2]. Summing
cell errors by Cauchy-Schwarz gives h_max^2 sqrt(E_Q/120). This statement
does not assign a global Sobolev derivative to a discontinuous kernel.
The separate physical fixtures include a jump counterexample to doing so.

## Rational duals and normalization

The flow identity follows by finite summation by parts with the exact
divergence convention in the proof document. Every residual coefficient
is charged by M times its absolute value; all edge and initial-cell
penalties are charged explicitly. Therefore a floating LP need not be
optimal, or even numerically feasible, to propose a usable rational dual.
The checker separately enforces the needed rational k_i in [-1,1].

The central wrapper is the same frozen kernel divided by an exact positive
normalization. Its wrapper radius and the radius recorded by a central
denominator report have different roles. The adapter recovers a valid
mean-zero numerator lower bound from each report and checks the wrapper's
normalization at the wrapper radius explicitly. It then retains an
all-mean quadratic numerator premise. The radius is not silently extended.

## Finite coverage and strictness

Each returned interval is checked using the exact minimum of a rational
quadratic and a positive denominator. The central interval, reflected
capacity intervals and outer intervals must cover the entire permitted
mean range [-1,1]. Only a finite complete cover with a strictly positive
margin above the target gives a strict lower bound for the infimum.
Isolated search-mean values and a numerical minimum do not supply this
argument. The global auditor and complete fresh-copy replay enforce the
finite arithmetic and file-dependency parts of this interface.

## Exact upper construction

For a nonuniform step density, each ordered pair of cells contributes a
translated triangular or trapezoidal overlap length. The sum is continuous
and piecewise affine, with all knots among differences of cell endpoints.
Its exact maximum is therefore attained at one of those knots. The generic
integer sweep checks those endpoint differences directly. The separate
fractional-cut implementation uses exact packed nonnegative convolutions
at the integer and half-cell anchors, then exact affine interpolation of
the knot values. For this one-cell cut geometry, the ordering can change
only at fractional cuts 0, 1/2 and 1. Literal rational fixtures cover
endpoints, tiny cuts and large height denominators. The selected full
witness still has its own executed generic nonuniform replay; fixture
agreement alone would not certify that witness.
