# Phase-averaged Gram relaxation: proposed route

This derives a necessary finite semidefinite relaxation for every admissible
measurable density. Numerical SDP output is not a certified bound. A rational
dual, exact PSD verification, and all multiplier signs remain obligations.

Put r=2h-1 on [0,2] and zero outside. Then |r|<=1 and integral r=0. Let
R(t)=integral r(x)r(x+t)dx. The even overlap e(t)=(p(t)+p(-t))/2 satisfies

    e(t) = (2-|t|)_+/4 - R(t)/4.

Fix N>=2 and a=2/N. For a uniformly distributed s in [-a,0], let
r_i(s)=a^-1 integral_[s+ia,s+(i+1)a] r, i=0,...,N. These N+1 cells cover
the support of r for every s, so sum_i r_i(s)=0. Define the real symmetric
matrix X_ij=E_s[r_i(s)r_j(s)]. Then X is positive semidefinite and X*1=0.
Its interior diagonal entries are at most 1; the two endpoint entries are
at most 1/3, by integrating the squared fraction of the cell inside [0,2].

For k=0,...,N, write T_a(u)=(1-|u|/a)_+. Averaging the origin of the grid
gives the exact identity

    a^2 sum_(i=0)^(N-k) X_(i,i+k) = integral R(t) T_a(t-ka) dt.

Indeed, for fixed x,y, the fraction of grid phases that puts them in cells
whose ordered index difference is k equals T_a(y-x-ka). Fubini applies to
these bounded, compactly supported functions. This argument includes k=0,
where both orders of x,y occur in a diagonal cell square.

If ||p||_infinity<=M, then e<=M and integral T_a=a imply

    M >= b_k - (a/4) sum_i X_(i,i+k),

where b_0=1/2-a/12, b_k=(2-ka)/4 for 1<=k<N, and b_N=a/24. These constants
come from integrating the triangular support term against T_a, including
its two corners at t=0 and t=2. Thus minimizing M subject to these inequalities,
X positive semidefinite, X*1=0, and the diagonal bounds gives a lower relaxation
for the original continuous problem. No step-density assumption or mesh error
is introduced by this derivation.

Further valid constraints follow because every r_i lies in [-1,1]. For any
three distinct indices, each of

    X_ij+X_jk-X_ik <=1, X_ij-X_jk+X_ik <=1,
    -X_ij+X_jk+X_ik<=1, -X_ij-X_jk-X_ik<=1

holds. Each left side before averaging is a multilinear polynomial on a
three-dimensional cube; its maximum is attained at a cube vertex, where
the inequality is elementary. Averaging preserves it. These constraints
do not imply that X is a rank-one matrix or realizable by a single density;
they are necessary conditions used for a universal lower relaxation only.

If the overlap mean is restricted to |m|<=delta, an additional necessary
constraint is c^T X c <=1/3+(delta/a)^2, where c_i=ia. To see this, let
epsilon_s(x) be the center of the cell containing x minus x. It is a
zero-mean sawtooth in s with E_s epsilon_s(x)^2=a^2/12. Writing
E_s=integral r(x)epsilon_s(x)dx gives E E_s=0 and, by Cauchy-Schwarz with
weight |r|, E E_s^2 <= (integral |r|)^2 a^2/12 <=a^2/3. Since
integral x*r(x)dx=-m and sum_i r_i=0, a sum_i c_i*r_i=-m+E_s.
Squaring and averaging proves the stated inequality. A check made with this
constraint covers only the specified mean interval; outer cases remain needed.

One can replace 1/3 by 1/pi^2. The periodic absolutely continuous E_s has
derivative -a sum_j r(s+ja) almost everywhere, since integral r=0. There are
N support terms for almost every s. Cauchy-Schwarz and integration give
E|E_s'|^2 <=a*N*integral r^2 <=4. The zero-mean periodic Wirtinger inequality
then gives E|E_s|^2 <=a^2/pi^2. This is an analytic necessary inequality;
the current SDP uses floating pi and has not certified its arithmetic.

### Sharper rational alias estimate

In fact the error constant can be replaced by **1/12**, sharply. The periodic
function E_s has zero mean and |E_s'|<=a*N=2 almost everywhere. The following
elementary periodic Lipschitz lemma gives E E_s^2<=a^2/12.

If a periodic L-Lipschitz function f has period a, put D=max f-min f and
c=(max f+min f)/2. The circular distance between maximum and minimum is at
most a/2, so D<=La/2. Define g(y)=D^2/4-(y-c)^2 on the range of f. This is
nonnegative. Take a primitive G of g. On each of the two arcs between a
minimum and a maximum, the chain rule gives integral L*g(f)>=|G(max f)-
G(min f)|. Therefore E g(f)>=2/(La)*integral g(y)dy=D^3/(3La).
It follows that

    Var(f) <= E(f-c)^2 <= D^2/4-D^3/(3La) <= L^2*a^2/48.

The last expression increases up to D=La/2. With L=2 and E f=0 this proves
the claimed a^2/12 bound. Consequently every admissible density with
|m|<=delta satisfies c^T X c<=1/12+(delta/a)^2. Alternating -1,+1 values
on half-cells attain equality in the alias variance; three exact fixtures
check this sharpness. These examples need not have overlap mean zero.

Every even overlap average y_k=b_k-(a/4)sum X_(i,i+k) is nonnegative. The
periodic q(t)=e(t)+e(2-t) has smoothed grid values Q_0=y_0+2y_N and
Q_k=y_k+y_(N-k), 1<=k<N, with periodic indices. The endpoint factor 2
accounts for the smoothed tails at both -2 and 2. They obey a sum_k Q_k=1.

For an integer d>=1, averaging q(d(s+epsilon)) against T_a(epsilon)/a
at s=ka gives

    W_(d,k)=sum_(j=1-d)^(d-1) (d-|j|)/d^2 * Q_(dk+j).

This follows from the exact refinement identity for a triangular kernel
of width da into translates of width-a kernels. Therefore integrating the
pointwise periodic triangle and perimeter inequalities gives
W_(d,k)<=W_(1,k)+W_(d-1,k) and their three-term sum<=2, for d>=2.
These inequalities are necessary at every grid point, and introduce no
assumption that the unsmoothed q is a step function.

## Exact dual obligation

Write every linear inequality as trace(A_j X)+c_j M<=b_j. A nonnegative
multiplier list with sum_j lambda_j*c_j=-1 gives
M>=trace(G X)+L, where G=sum lambda_j A_j and L=-sum lambda_j b_j. Here
only cap rows have c_j=-1, so their multipliers must sum exactly to 1.
The verifier reconstructs all rational A_j and b_j from the stated formulas.

Because X*1=0 and X is positive semidefinite, it suffices that U^T G U be
positive semidefinite, where U consists of the N standard basis vectors
in the first N rows and a final row of -1's. Its columns span 1-perp.
The implemented checker requires the stronger positive definite property.
After clearing a common denominator, integer Bareiss elimination checks
every leading principal minor is strictly positive. Sylvester's criterion
then proves positive definiteness. The determinant divisions are checked
exactly; no floating eigenvalue or solver status is a proof premise.

Any diagonal PSD repair is paid in L by the exact diagonal upper bounds.
Older proposals used the rational upper constant .101322 for 1/pi^2.
The final checker accepts error constants at least 1/12 using the sharper
periodic Lipschitz lemma above; it needs no transcendental arithmetic.
The remaining analytic premises are the cell/phase identities and box
inequalities. Machin/arctangent arithmetic remains a diagnostic fixture.

A passed central certificate still needs a certified cover of all other
means. Source Fourier outer reports at a weaker target cannot be reused as
if they had executed a stronger target.

## Signed functional separators

The cap weights can instead be arbitrary signed rational numbers gamma_k,
without any normalization. If the same reconstructed G is positive on
1-perp, the derivation gives sum_k gamma_k*y_k>=L. This is a linear
functional inequality for every overlap density in the mean interval;
it is not by itself a lower bound on mu.

On the positive half-axis its even kernel is

    K(t)=gamma_0*T_a(t)/a + sum_(k=1)^N gamma_k*T_a(t-ka)/(2a).

Thus integral_[-2,2] p(t)K(t)dt>=L. At a literal trial profile, a positive
exact gap L-sum gamma_k*y_k refutes its realizability by any admissible
density in that mean interval. It also excludes an infinity-norm ball in
the vector of hat averages of radius gap/sum|gamma_k|. Neither implication
makes the relaxed cap of that trial profile an original-problem upper bound.
The row can be combined with the earlier Fourier/circle constraints, but
all subsequent lower-bound certificates need a fresh continuous replay.
