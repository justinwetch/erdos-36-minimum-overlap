# Returning the physical odd-profile capacity to an exact bound

This proof route has separate verifiers. The capacity700 and block750
checkpoints have passed their original and complete fresh global checks;
each later kernel must independently pass those gates. The route preserves
the minimum-overlap contract and uses numerical LP values only to propose
rational witnesses.

Use an even kernel Q with checked positive-part integral at most D and
expectation at least the exact quadratic L(m). On0<=t<=1 let
A(t)=Q(t), B(t)=Q(2-t), and c(t)=|A(t)|+|B(t)|. The quartet argument in
ODD_LIPSCHITZ_ROUTE.md gives, for any admissible overlap of peak M,

    integral Qp <= M D - integral_0^1 c(t)|d(t)|dt.

Here d(t)=p(t)-p(-t) is1-Lipschitz, d(0)=0, |d|<=M and
2 integral_0^1 d=m. These conditions concern the same function d.

Partition[0,1] into intervals of lengths h_i. Every affine-kernel
breakpoint, including its reflected2-t breakpoint, must be a boundary.
The kernel may jump at those boundaries; no global Sobolev assumption
across its jumps is made. Write z_i for the average of d on cell i.
Then |z_i|<=M, |z_0|<=h_0/2, and

    |z_(i+1)-z_i| <= (h_i+h_(i+1))/2,
    2 sum h_i z_i = m.

Let I_A,i and I_B,i be the exact integrals of A and B on cell i. Jensen
gives h_i average(c)>=|I_A,i|+|I_B,i|=:C_i. For any exact k_i in[-1,1],

    -h_i average(c)|z_i| <= -k_i C_i z_i.

There is a covariance error because c and |d| vary inside a cell. If f
is absolutely continuous there and g is1-Lipschitz, the centered integral
has the Green-kernel identity with K(s,t)=min(s,t)-st/h. Since K>=0,

    |integral fg-h average(f)average(g)|
       <= (1/2) integral s(h-s)|f'(s)|ds
       <= h^(5/2)/sqrt(120) * ||f'||_2.

The last constant follows from integral s^2(h-s)^2 ds=h^5/30. It is sharp
for g(t)=t and f'(t)=t(h-t). Applying this cellwise to f=c and g=|d|,
then Cauchy-Schwarz across cells, bounds the total error by

    E <= max(h_i)^2 * sqrt( integral_full Q'(t)^2 dt /120 ).

Indeed, on each smooth piece c'=sign(A)A'+sign(B)B', so the sum of the
cell energies of c' is at most2 integral_0^2 Q'^2, the full energy of the
even kernel. The required aligned mesh prevents omitted jump costs.

Choose arbitrary rational edge flows v_i, mean multiplier tau and first-
cell multiplier kappa. Let div(v)=(-v_0,v_0-v_1,...,v_last), and define

    R_i = -k_i C_i -2 tau h_i -div(v)_i -kappa*1_(i=0),
    T = sum |v_i|(h_i+h_(i+1))/2 + |kappa|h_0/2.

The preceding constraints and summation by parts give

    integral Qp <= M(D+sum |R_i|) +tau*m+T+E.

Consequently

    M >= [L(m)-tau*m-T-E] / [D+sum |R_i|].

The numerator is an exact quadratic. Its exact interval minimum returns
a checked mean interval; finitely many intervals, the central case,
reflection and the existing outer cases can establish a uniform margin.
The floating LP only supplies k,v,tau,kappa. The verifier needs no LP
solver and charges its entire remaining residual explicitly.

The normalized central wrapper is exactly H/ell with theta=0. The adapter
checks its embedded H against the original central certificate, all three
executed denominator reports and their transitive hashes. Each original
denominator is divided by the same exact positive ell; their maximum is
used. The normalization premise is independently checked from each mode.

Derivative energy is bounded independently with Arb and standard-library
dyadic arithmetic. On each smooth subcell, Q' is its quadratic Taylor
polynomial plus a remainder bounded by ||Q''''||_infinity*r^3/6. The
polynomial square integrates exactly; the cross term and remainder square
are charged outward. Each backend also integrates the cell coefficients
analytically through its own primitive evaluator and encloses every R_i.
All new reports bind the input kernel, dual bundle, old denominator graph,
energy report and proof implementations. A new global audit and full
fresh-copy replay are mandatory before this route changes the bound.

## Detailed analytic return

The following argument is independent of the numerical LP and applies to
every admissible measurable density in PROOF.md. All derivatives below
are almost-everywhere derivatives on the stated intervals.

For0<=t<=2, subtract the two overlap integrals. The autocorrelation terms
cancel, leaving

    d(t) = integral_0^(2-t) [h(x)-h(x+t)] dx
         = H(2-t)+H(t)-1.

The cumulative function H is absolutely continuous. Thus d(0)=0,
d(2-t)=d(t), and d'=h(t)-h(2-t) lies in[-1,1]. The first moment of p is

    m = integral_0^2 t*d(t)dt = 2 integral_0^1 d(t)dt.

The existing moment lemma places m in[-1,1]. If M is the full overlap
supremum, both p(t) and p(-t) lie in[0,M], so |d(t)|<=M. Their sum u lies
in[|d|,2M-|d|]. The same holds for the pair at2-t, with the same d.
For even Q, maximizing these two pair sums gives exactly

    A*u+B*v <= 2M(A_++B_+) - (|A|+|B|)|d|.

The four shifts t,-t,2-t,t-2 cover the full integration domain as t ranges
over[0,1]. Also integral_full Q_+=2 integral_0^1(A_++B_+). Integration
therefore proves the quartet capacity bound for any checked upper D.

For a cell J=[a,a+h], write averages with a bar. Since |d| is1-Lipschitz,
the covariance identity and Green-kernel estimate give

    integral_J c|d| >= h*cbar*average_J(|d|)
                       - h^(5/2)/sqrt(120)*||c'||_(L2(J))
                    >= h*cbar*|z| - error_J.

For completeness, integration by parts expresses the centered product as
the integral of f'(s)g'(t) times K(s,t)=min(s,t)-st/h on[0,h]^2. Its
integral in t is s(h-s)/2. Bounding |g'| by1 and applying Cauchy-Schwarz
uses integral_0^h s^2(h-s)^2 ds=h^5/30, giving the displayed constant.
This is an estimate on each smooth kernel cell; it assumes no continuity
of Q across different cells.

On a cell, A and B are absolutely continuous. Their absolute values are
also absolutely continuous, and

    |c'|^2 <= 2(|A'|^2+|B'|^2).

Summing the right side over[0,1] gives2 integral_0^2 |Q'|^2, which equals
the full piecewise derivative energy because Q is even. Cauchy-Schwarz
over cells and sum h_i^5<=max(h_i)^4*sum h_i=max(h_i)^4 yield E. Zeroes
of Q cause no extra jump term in |Q|. An affine-kernel discontinuity does
require a cell boundary, which is why the verifier checks every such
boundary and its2-t reflection before integrating any coefficients.

Jensen gives C_i=|integral_J A|+|integral_J B|<=h_i*cbar_i. For arbitrary
k_i in[-1,1], -h_i*cbar_i*|z_i|<=-k_i*C_i*z_i. The cell-average constraints
follow by averaging the Lipschitz inequality: the mean distance between
points in two adjacent cells is(h_i+h_(i+1))/2, and the mean distance from
zero in the first cell is h_0/2.

With the stated divergence convention, the exact flow identity is

    -sum k_i*C_i*z_i
       = tau*m + sum v_i*(z_(i+1)-z_i) + kappa*z_0 + sum R_i*z_i.

Taking absolute values only on the last three terms gives tau*m+T+
M*sum|R_i|. Combining this identity with the quartet bound and covariance
estimate proves the returned quadratic inequality for every mean m.
Neither optimality nor feasibility of the floating LP solution is used:
any rational k,v,tau,kappa satisfying |k|<=1 are valid, because every
coefficient residual is paid. The search peak and search mean are merely
witness-discovery metadata.

For the theta-zero wrapper, the old central kernel H has expectation at
least L0+C*m^2. The adapter independently checks L0+min(0,C)*r^2>=ell
using all three executed central reports. Dividing by ell>0 gives

    integral Qp >= [ell-min(0,C)*r^2+C*m^2]/ell = L(m).

This is an all-mean premise; r defines the normalization, rather than
limiting where this quadratic may be used. The old positive integral of
H divided by ell bounds that of Q. The adapter uses the maximum of the
three checked denominators. Capacity reports independently enclose the
cell-integral coefficients with Arb and integer interval arithmetic.

Finally, each exact interval minimum returns a uniform lower bound on M
for every density whose mean lies in that interval. The central case,
reflected capacity cases and the outer cases form a finite cover of
[-1,1]. If every returned lower bound strictly exceeds a rational target,
their finite minimum also strictly exceeds it. Taking the infimum over
all admissible densities, and applying the bridge in PROOF.md, proves the
strict target bound for mu. The global auditor checks this complete cover;
a collection of isolated search-mean scores does not supply that step.

## Optional outward block primitive

The separately versioned integer capacity checker may explicitly select
integer_block_primitive.py. The original direct checker remains unchanged.
For a uniform grid of step delta, a block begins with checked intervals for
sin(xi*x0), cos(xi*x0), sin(xi*delta) and cos(xi*delta). It repeatedly uses

    sin(a+b)=sin(a)cos(b)+cos(a)sin(b),
    cos(a+b)=cos(a)cos(b)-sin(a)sin(b).

Every multiplication and addition rounds outward with integer floor and
ceiling. Induction on the block index therefore encloses the exact sine
and cosine at each grid point, and consequently the analytic primitive.
The same exact frequency belongs to every input interval; treating their
uncertainties separately only enlarges the enclosure. No floating
recurrence or uncharged accumulated error is used. Each64-point block
resets from direct Taylor/halving/doubling enclosures. A nonuniform point
uses the unchanged direct evaluator. Polynomial terms and the affine
prefix are also enclosed explicitly. The block length and grid are bound
in the report and checked by the versioned global auditor.

Short blocks keep widths useful, rather than supplying a new analytic
assumption: interval containment holds at any length. The implementation
rejects an excessively wide interval. Exact polynomial fixtures, direct
trigonometric consistency fixtures, nonuniform fallback fixtures and a
512-point actual-kernel benchmark were executed before integrating this
backend into a separate proof pipeline. A production claim using it still
requires a complete original and fresh global replay, with all hashes and
the expanded control suite checked. The direct integer campaigns continue
independently and are never relabeled as block executions.

The alignment requirement has an exact physical counterexample if omitted.
Take h=1 on[0,1] and h=0 on[1,2], so d(t)=t on[0,1]. Let the even kernel
be1 for1/2<|t|<1 and0 elsewhere. Then c(t)=1 for1/2<t<1 and0 for0<t<1/2.
On the falsely unsplit cell[0,1], its covariance with d is
3/8-(1/2)(1/2)=1/8, despite zero piecewise derivative energy. Splitting
at1/2 makes the covariance zero on each cell, as the correct argument
requires. check_capacity_physical_fixtures.py independently executed this
counterexample and45 rational physical-density/kernel fixtures, including
22 nonzero covariance cases and15 reflection/moment checks. These tests
support the interfaces; the general proof above supplies their extension
to arbitrary admissible measurable densities.
