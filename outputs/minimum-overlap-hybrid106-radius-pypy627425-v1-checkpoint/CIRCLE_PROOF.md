# Periodic triangle constraints and a continuous dual

This adds inequalities implied by the box constraint 0<=h<=1 to the Fourier
relaxation. Numerical linear programs discover coefficients. The continuous
bound depends only on the explicit decimal coefficients and outward integration.
This is a computer-assisted argument, not a proof-assistant formalization.

## Universal inequalities

Extend h periodically with period 2, retaining integral_0^2 h=1, and put

    q(s) = integral_0^2 h(x)(1-h(x+s)) dx.

For 0<=s<=2, splitting at the wrapped endpoint gives

    q(s) = p(s)+p(s-2).

The periodic autocorrelation integral h(x)h(x+s) is even, so q is even and
periodic. In particular, for any integrable period-2 function w,

    integral_0^2 q(s)w(s) ds = integral_-2^2 p(t)w(t mod 2) dt.

For a,b,c in [0,1], define d(a,b)=a+b-2ab. The following identities prove
the metric triangle and perimeter inequalities directly:

    d(a,b)+d(b,c)-d(a,c)
      = 2[b(1-a)(1-c)+(1-b)ac] >= 0;
    2-d(a,b)-d(b,c)-d(c,a)
      = 2[abc+(1-a)(1-b)(1-c)] >= 0.

Substitute a=h(x), b=h(x+s), c=h(x+s+t), and integrate over the circle.
Translation invariance and integral d(h(x),h(x+s))=2q(s) give

    q(s+t) <= q(s)+q(t),
    q(s)+q(t)+q(s+t) <= 2.

These hold for all real s,t, with their arguments understood modulo 2. No
regularity assumption beyond measurability and the stated box/mass constraints
is needed. Taking t=s and averaging over a cell I of length h gives

    (1/(2h)) integral_{2I mod 2} q - (2/h) integral_I q <= 0;
    (1/(2h)) integral_{2I mod 2} q + (2/h) integral_I q <= 2.

The image 2I is taken with multiplicity if wrapping occurs. For the power-of-two
grid used here, each doubled cell covers exactly two grid cells modulo 2.

## Exact finite step rows

Use n equal cells on [0,2], h=2/n. Let R=identity+reversal and let D have
row i equal to one half on cells 2i and 2i+1 modulo n. For an even test density
constant on each positive cell, the two averaged inequalities have coefficient
matrices

    A_low=(D-2 identity)R,    A_high=(D+2 identity)R.

For arbitrary p, each row is still a valid integral inequality with a piecewise
constant even test function: symmetrize its periodic weight under t -> -t.
The integral over [-2,2] on positive cell j then has coefficient
2h times that test function's value. Thus, for nonpositive multipliers z_low
and z_high, the combined even step function has positive-cell values

    step = (A_low^T z_low + A_high^T z_high)/(2h).

circle_certificate.py recomputes these values from exact Decimal sums of the
serialized multipliers, rather than trusting exported step values. n is a power
of two, so all cell endpoints and these divisions terminate exactly in decimal.
The script uses 120 decimal digits, far exceeding the finite coefficient sizes
in these certificates. The step vector is exactly symmetric under reversal.

## Continuous implication

Let y0,y2 be arbitrary real numbers and z_xi,z_low,z_high be nonpositive. Define

    Q(t)=y0+y2*t^2+sum z_xi*cos(xi*t)+step(t).

For every original admissible density with mean m, the Fourier and moment
identities in LOWER_PROOF.md and the inequalities above imply

    integral p Q >= L(m),
    L(m)=y0+y2*(2/3+m^2/2)+sum z_xi*sinc(xi)^2+2 sum z_high.

Multiplying an upper-bound inequality by a nonpositive number explains the
direction. The lower-circle rows contribute zero to L. Since p>=0,

    integral p Q <= ||p||_infinity * D,
    D=integral_-2^2 max(Q(t),0) dt.

For |m|<=c, use m^2=c^2 when y2<0 and m^2=0 when y2>=0 to obtain a uniform
lower numerator. If L_lower>0 and D_upper>0 are outward certificates, then
||p||_infinity >= L_lower/D_upper. This central mean case is combined with
separately executed ordinary Fourier certificates for the remaining mean bins;
a central check alone establishes no global bound.

## Integration and reproducibility obligations

The function Q is even. The checker integrates on [0,2] and doubles the result.
It splits at every exact step boundary, so no Taylor interval crosses a jump.
On each cell the step is constant, and the source analytic antiderivative plus
that constant times t is valid. Arb bounds each interval with either the
second-order or fourth-order Taylor enclosure. Positive intervals use the
analytic integral, negative intervals contribute zero, and unresolved final
intervals use length times the positive upper range. Every original cell is
fully covered by bisection. No floating root or LP residual is used as a premise.
The numerator is independently recomputed with Arb from the serialized decimals.

The unchanged public checker does not support these additional rows. Its
ordinary outer-bin replays remain applicable, while the new central calculation
has its own second- and fourth-order continuous replays. This extension must
remain explicitly identified in any delivery; it is not a claim that an
unchanged public checker verified the new central rows.

## General signed families (schema v2, separately tested)

For distinct integer positions r_i and integer weights b_i, let B=sum b_i.
For fixed a_i in [0,1], take independent Bernoulli variables X_i with means a_i.
Write S=sum b_i X_i, an integer. Direct expansion gives

    sum_{i<j} b_i b_j |X_i-X_j| = S(B-S) <= floor(B^2/4).

The last bound holds for every integer S, including values outside [0,B].
Taking expectations replaces |X_i-X_j| with d(a_i,a_j). Now substitute
a_i=h(x+r_i*s), integrate over the circle and divide by 2. Therefore

    sum_{i<j} b_i b_j q((r_i-r_j)*s) <= floor(B^2/4).

Evenness of q permits absolute differences. Averaging over a cell gives a
piecewise constant integral test. For distance k, its dilation row averages
the k cells k*i,...,k*i+k-1 modulo n with coefficient 1/k. The checker derives
all distance coefficients and the RHS directly from the serialized integer
positions and weights; arbitrary exported coefficients are not trusted.
It sums rational offsets with Fraction, including the nonterminating decimal
cases such as 1/3. The periodic step function is again symmetrized. Each family
has nonpositive multipliers and contributes its exact integer RHS times their
sum to L. The same continuous integration argument applies cell by cell.

The original triangle pair is positions (0,1,2), with weights (1,-1,1) and
(1,1,1). Schema-v1 checkpoints remain restricted to that pair. Small-grid
schema-v2 checks are diagnostics unless accompanied by the full mean cover
and all required executed replay records; no new global claim follows merely
from a stronger numerical family menu.

## Arbitrary rational intervals (schema v4)

For I=[a,b] contained in [0,2], put h=b-a. The same averaging proof gives
unnormalized weights

    w_low = (1/2) 1_{2I mod 2} - 2 1_I,       RHS 0,
    w_high = (1/2) 1_{2I mod 2} + 2 1_I,      RHS 2h.

The image 2I is counted with multiplicity if it wraps. Multipliers are
nonpositive. Because q is even and period2, replace w by
psi(t)=(w(t mod2)+w(-t mod2))/2. Then integral_0^2 q w equals
integral_-2^2 p psi. This follows by splitting p into its two wrapped pieces
and changing t to 2-t in the negative piece. The numerator contribution is
2h*z_high. A uniform normalized row's multiplier z_raw becomes z_raw/h in
this unnormalized representation; it defines exactly the same function.

circle_intervals.py compiles all interval endpoints, doubled endpoints,
wrapped pieces and reflected pieces with Fraction. It merges only adjacent
pieces with exactly equal rational values. verify_interval_data.py then
bisects every compiled piece with rational endpoints, using the same Arb
enclosures as above. No integration cell crosses a step jump. Exact equality
with all4096 cells of the current schema-v1 certificate, the numerator and
wrapped examples was checked; separate order2 and order4 replays passed the
same central target. Boundary optimization supplied no substantive new bound.

## Separately implemented integer interval replay

verify_integer_circle.py accepts schema-v1 and imports only the Python standard
library. Its periodic step compiler uses Fraction throughout and is separate
from the Decimal compiler above. It merges equal adjacent steps exactly.

Every arithmetic interval has endpoints that are integers divided by 2^192.
Addition is exact; products and quotients round down/up using integer floor
and ceiling division. Thus each operation encloses the exact operation on its
input intervals. Zero-containing denominators are rejected. To evaluate sine
and cosine, repeatedly halve the argument until its absolute upper endpoint
is at most1/8. Sum the Taylor polynomials through degrees49 for sine and48
for cosine, including the zero next coefficient in each case. Lagrange's
theorem bounds the remainders by (1/8)^51/51! and (1/8)^50/50!, respectively.
Enclose those remainders and recover the original argument by the exact
double-angle identities with outward integer operations. No value of pi is
needed, and no library trigonometric evaluation is trusted by this checker.

The checker independently evaluates Q and its first three derivatives,
using M4=sum |z|*xi^4 for the Taylor remainder. It covers every rational step
piece by dyadic bisection. Certified positive pieces use a separately coded
analytic primitive; certified negative pieces contribute zero. At terminal
width an ambiguous piece contributes width*max(upper range,0). The exact
rational upper bounds are added and doubled. The numerator is recomputed with
the same outward arithmetic, including the worst mean-square contribution.
The final comparison with the requested target is exact Fraction arithmetic.

This implementation is independent of Arb and the public parser, but shares
the stated mathematical inequalities and Taylor-integration method. Agreement
would test arithmetic and implementation errors, not provide an independent
proof of the universal inequalities. The recorded replay's passed field and
input/checker hashes determine whether it has actually checked a given target.

For schema-v2, verify_integer_hypermetric.py separately derives every distance
coefficient by summing b_i*b_j over pairs of integer positions. A distance k
spreads a multiplier z across cells k*i,...,k*i+k-1 with coefficient z/(k*h),
then the compiler averages that vector with its reversal. It sums the exact
integer family RHS times the multipliers for the numerator. This compiler
agrees exactly with the other schema-v2 compiler on all4096 cells of the
multi-scale certificate. Its integration engine and dyadic arithmetic are
shared with verify_integer_circle.py; both source hashes are recorded.

The multi-scale checkpoint uses four lower-triangle families at positions
(0,1,2),(0,1,3),(0,1,4),(0,1,5), with b=(1,-1,1), and the original perimeter
family b=(1,1,1) at positions(0,1,2). The independently compiled integer replay
passed the central target .38056576 on |m|<=.002042107568. Second- and
fourth-order Arb central replays passed as well; all174 outer cases passed
both the unchanged source checker and fourth-order checker. Two combined
coverage/hash audits establish the global bound mu>.38056576. This remains
a computer-assisted bound with reviewed analytic premises, not a full
solution or a proof-assistant formalization.
