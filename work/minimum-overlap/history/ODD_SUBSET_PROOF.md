# Odd subsets: proved premises and deferred numerical tests

These are research premises. They have not entered a promoted certificate,
and the existing trusted phase-Gram checker has not been changed.

## Universal inequality

Let k be odd, let r_1,...,r_k belong to [-1,1], and let s_i belong to
{-1,1}. Then

    -sum(i<j) s_i*s_j*r_i*r_j <= (k-1)/2.

The left side is affine in each coordinate separately. Its maximum on the
cube is therefore attained at a vertex. At a vertex it equals

    (k - (sum_i s_i*r_i)^2)/2.

The sum is an odd integer, so its squared absolute value is at least one.
This proves the stated inequality. Taking expectations gives the same
linear inequality for any covariance X_ij=E[r_i*r_j]. All phase-cell
variables in PHASE_GRAM_PROOF.md meet the required box bounds.

Fixing s_1=1 loses no inequalities, because simultaneously negating every
sign preserves all products. The executed controls exhaust every cube
vertex and every retained sign pattern for k=5,7,9, and reject even sizes.

## Distinct information beyond smaller odd subsets

The matrix

    X = k/(k-1) * (I - J/k)

is exactly positive semidefinite and annihilates the all-ones vector.
It has diagonal one and off-diagonal -1/(k-1). Its all-positive k-subset
expression is k/2, violating the required right side by exactly 1/2.

For any smaller odd m and any signs, the corresponding expression is at
most m*(m-1)/(2*(k-1)) <= (m-1)/2. Thus all smaller odd-subset inequalities
hold in this example. This proves independence from those smaller inequalities
and PSD alone. It does not assert that this matrix satisfies the entire
phase-hat model or comes from an admissible density.

## Why sampling both endpoints was unhelpful

For a signed subset, the expression is

    (sum_i X_ii - s' X s)/2 <= sum_i X_ii/2

by PSD. In the phase model each endpoint diagonal is at most 1/3 and
every interior diagonal is at most one. A k-subset containing both
endpoints therefore has expression at most k/2-2/3, already strictly
below (k-1)/2 by 1/6. Such a generic inequality adds no restriction to the
existing model. All 80 selected seven/nine-variable violations in the
executed scan used interior indices. Future scans should spend their
samples on interior subsets, or use genuinely sharper endpoint premises.

## Weighted integer reformulation: a future discriminator

More generally take integer b_i with odd sum, and set

    Q_b(r) = -sum(i<j) b_i*b_j*r_i*r_j.

At cube vertices, sum b_i*r_i is odd. The same multiaffine argument gives

    Q_b(r) <= (sum_i b_i^2 - 1)/2.

For a proposed covariance X, put C=X+diag(1-X_ii). The violation equals

    (1 - b' C b)/2.

Thus separating this entire weighted family is an integer quadratic
search for an odd-parity vector b with b'C b<1. This identity preserves
the signs and the common covariance. A lattice heuristic could generate
candidates, but every candidate must be scored against the original X.
No such weighted search, new checker, or bound is claimed here.

## Executed deciding tests

Both numerical tests use the same fixed five-cone baseline, whose cap is
0.38062632701655985. The cones have grids 31,33,43,59,61; their rows, seed,
containment audit, coordinates and dependent-hat elimination are fixed.

* Forty selected five-variable inequalities give cap 0.38062640844963275,
  a numerical increase about 8.14e-8.
* Forty seven-variable and forty nine-variable inequalities give cap
  0.3806264012234209, a numerical increase about 7.42e-8. The final
  constraint defect is 2.41e-8; this is not an exact improvement claim.

Neither reaches the 1e-6 gain selected to justify an exact grammar extension.
The selected extensions are deferred. These finite experiments do not
refute the complete families or establish their maximum possible benefit.
Their functional exports are empty, and the actual exported matrices,
input hashes, controls, solver statuses and implementation snapshots are
preserved in the run folders. The campaign returns to a new compatibility
scale in the existing certificate grammar.

Earlier diagnostic logs sometimes use the word facet for a valid row.
No claim that these rows define facets of a polytope is needed or made.
