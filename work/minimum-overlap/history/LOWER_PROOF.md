# Analytic and arithmetic basis of the lower certificates

This note reviews the reduction in the pinned public lower-certificate source
(commit 6bc610e40083ef61a40966dfb5d38612cabc4c5b), and records the additional
fourth-order integration enclosure used in this campaign. The optimizer and its
floating roots are discovery tools, not premises of the proof. This is a
computer-assisted mathematical argument, not a proof-assistant formalization.

## Universal constraints

Let h:[0,2] -> [0,1], integral h=1, and let g=1-h on that interval. Both
functions are zero outside it. Independent X,Y with densities h,g have
difference Z=Y-X with nonnegative density p(t)=integral h(x)g(x+t) dx,
supported in [-2,2], with integral p=1. Write m=E Z. The rearrangement bounds
1/2 <= E X <= 3/2 and E X+E Y=2 give -1<=m<=1. Also

    E Z^2 = E X^2+E Y^2-2 E X E Y = 2/3 + m^2/2.

For any real nonzero xi, define centered Fourier transforms H,G and
sigma=sin(xi)/xi. Since H+G=2 sigma and |H|,|G|<=1, writing H-G=a+ib gives

    C = E cos(xi Z) = sigma^2 - (a^2+b^2)/4,
    S = E sin(xi Z) = -sigma b.

The identity |H|^2+|G|^2=2 sigma^2+(a^2+b^2)/2 implies

    2 sigma^2-1 <= C <= sigma^2,
    |S| <= 2 |sigma| sqrt(1-sigma^2),
    C+alpha S <= (1+alpha^2) sigma^2.

The last inequality follows by completing the square in b and dropping the
nonpositive term -a^2/4. The limiting xi=0 case is valid, though the certificate
audit rejects zero trigonometric frequencies because antiderivatives divide
by them.

For a mean bin I=[l,u], these give bounds E phi(Z)<=B_I for the nine accepted
term types: t, -t, t2, -t2, cos, -cos, sin, -sin, cos+alpha*sin. The moment
bounds use u, -l, 2/3+max_I(m^2)/2 and -2/3-min_I(m^2)/2. The remaining
bounds are the corresponding displayed Fourier inequalities. The checker
recomputes each B_I; stored B fields are never proof premises.

## Dual implication and finite return

Any finite nonnegative multiplier list defines

    q_I(t)=1+sum_j lambda_j (B_I,j-phi_j(t)).

For every admissible p with mean in I,

    1 <= integral p q_I <= ||p||_infinity * integral max(q_I,0).

Consequently an outward-certified D_I bounding the last integral yields
||p||_infinity >=1/D_I. If finitely many bins cover [-1,1] and every D_I<1/C,
then max_I D_I<1/C, so the continuous infimum is at least 1/max_I D_I>C.
This finite maximum supplies a uniform strict margin; individual strict
inequalities without a uniform margin would not justify the same conclusion.

For a balanced finite integer partition, represent its memberships by binary
cells of width 1/N on [0,2]. Its overlap is piecewise affine, with values
r(k)/N at grid shifts k/N. Thus its continuum supremum equals the maximum
integer overlap divided by N. The universal density lower bound applies to
every such partition and therefore to the asymptotic constant. The shift
orientation reverses k, which does not change a maximum over all shifts.

## Why changing certificates remains valid

Multipliers from any source mean bin can be used on a different bin after
recomputing all right-hand sides for the new bin. Every nonnegative mixture
of multiplier lists is another valid list; exact normalization of mixture
weights is unnecessary. The campaign uses this to refine bins, reoptimize
weights and blend distinct lists. No numerical optimization guarantee is
needed once the resulting explicit list passes verification.

There is a useful additional phase simplification. At one frequency combine
cosine and cos+alpha*sin rows, putting A=sum lambda and B=sum lambda*alpha,
where a pure cosine has alpha=0. For A>0 their trigonometric part is
A*cos+B*sin. The single valid row with multiplier A and alpha=B/A has RHS
sigma^2*(A+B^2/A). Cauchy-Schwarz gives B^2/A<=sum lambda*alpha^2, so this is
no larger than the sum of the original RHS values. Thus the exact
simplification decreases q by a nonnegative constant. compress_phase.py
exports explicit decimal proposals for A and B/A; because division is
rounded, the final argument relies on direct Arb verification of that new
valid row, not on an unverified exact dominance claim for serialized floats.

Under reflection t -> -t, swap t with -t, sin with -sin, and change alpha to
-alpha in cos+alpha*sin. Cosine and squared terms remain unchanged. Reflect
the mean interval as [l,u] -> [-u,-l]. This explains the mirrored certificates;
the checker still verifies each mirrored bin separately.

## Fourth-order outward enclosure

For each q, compute its first three derivatives at c using Arb balls. Let

    M4 = sum_harmonic_terms |lambda| |xi|^4 A,

where A=1 for a signed sine or cosine and A=sqrt(1+alpha^2) for
cos+alpha*sin. Polynomial terms have fourth derivative zero. Every harmonic
phi satisfies phi''=-xi^2 phi and phi'''=-xi^2 phi'. Hence M4 bounds |q''''|
everywhere on [-2,2]. For |x-c|<=r, Taylor's theorem gives

    |q(x)-q(c)| <= |q'(c)|r + |q''(c)|r^2/2
                   + |q'''(c)|r^3/6 + M4 r^4/24.

All operations, including centers, radii and endpoints, are outward ball
operations. Denote the resulting interval bounds by L,U. If U<=0, the
positive-part integral contributes zero. If L>=0, integrate q using the
explicit elementary antiderivative. Otherwise bisect; at final width the
contribution is bounded above by interval_length*max(U,0). The final
intervals cover [-2,2]. Overlapping proposed root neighborhoods can only
overcount a nonnegative integral. Missing roots cannot remove intervals.

The implementation reuses the pinned source's parser, analytic RHS,
antiderivative, cover repair and per-bin target comparison, replacing only
its second-order interval range enclosure. Full original-verifier replays
are retained as cross-checks where executed. The fourth-order derivative
formulas were additionally tested against 100-digit numerical differentiation
for every accepted term type at several points (216 finite checks). Those
diagnostics use explicit tiny tolerances for numerical zero cancellation and
endpoint equality; they are not used in the rigorous integral proof.

## Executed scope and audit obligations

The accepted target must appear explicitly in the command and every covered
bin must pass. Root estimates, a subset replay, or a float minimum alone
establish no global bound. audit_lower.py checks complete mean coverage,
nonnegative finite multipliers, accepted term types, nonzero frequencies,
executed indices and file hashes. Tiny source endpoint gaps are closed by
widening bins before recomputing RHS values. The analytic inequalities above
and the Taylor enclosure are separately reviewed mathematical premises.
