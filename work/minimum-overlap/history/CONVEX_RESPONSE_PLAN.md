# Next deciding test: active convex-profile column generation

Status: proposed experiment. No claim of a new upper bound or intrinsic
convexity gap follows from this plan. The original minimum-overlap target
and the deadline remain unchanged.

The earlier convex_profile_probe.py used32 actual upper-search witnesses
and found no improving mixture. Those witnesses were optimized for their
individual peaks. A stronger discriminator builds new actual densities
against the current mixture LP dual, so their profiles can hedge one another.

Use a common even cell count n, initially256 or512. Each actual density h
has0<=h_i<=1, sum h_i=n/2 and sum(2i+1-n)h_i=0. The last condition fixes the
overlap mean exactly to0, inside every current central mean branch. Allow
general asymmetric densities. Reflection pairs provide the even profiles
e_h(t)=(p_h(t)+p_h(-t))/2, a convex mixture of two admissible overlap profiles.

At grid shift k, for integer heights a_i/d,

    e_h(2k/n)=sum_i[d(a_i+a_(i+k))-2a_i a_(i+k)]/(n d^2).

Include k=0 and n, with the last value0. These profiles are affine between
the common grid knots. A convex mixture LP minimizes their maximum with
nonnegative weights summing to1. Its lag dual weights lambda_k are
nonnegative and sum to1. Numerical LP output is only discovery.

Construct a best-response actual h by minimizing sum_k lambda_k e_h(2k/n).
Put width=2/n, T_ii=lambda_0, T_ij=lambda_|i-j|/2 off the diagonal, and
l_j=sum_(k<=j)lambda_k+sum_(k<=n-1-j)lambda_k. Then

    E(h)=width*l'h/2-width*h'Th,
    grad E=width*l/2-2width*Th.

First check this identity against a direct overlap sum and finite differences
on small fixtures. The quadratic is generally indefinite. A bounded
Frank-Wolfe search uses a box/mass/centroid linear oracle and exact scalar
quadratic line minimization on each proposed segment. Multiple actual
best-response starts can enrich the pool; none is a global optimization claim.

Quantize proposed heights to a fixed even integer denominator, repair the
mass, then repair the centroid using adjacent-cell integer transfers. Reject
any repair that lacks box capacity, rather than assuming success. Check both
equalities exactly. Preserve the actual repaired witnesses. The repair is a
proposal procedure, not a universal existence theorem.

Round nonnegative mixture weights to integers W_i and normalize by their
exact sum S. Compute every lag numerator exactly. The full even mixture peak
is max_k sum_i W_i counts_(i,k)/(S*n*d^2). Verify it by a separate literal
overlap implementation on small controls and selected full witnesses. Keep
mass, centroid, boxes, all shifts and input hashes in the executed report.

Every uniform linear-kernel certificate valid on the current central branch
also holds on this convex mixture. Hence its certified lower-bound value
cannot exceed this exact mixture peak. This bounds a proof method. The
mixture need not be the overlap profile of any single density, so it supplies
no upper bound for the original mu. A failed pool search proves no method
obstruction. A numerical peak below the verified global lower bound must
trigger an immediate mathematical/implementation audit with the witnesses
preserved; it must not be silently discarded.

Run one bounded column-generation campaign, inspect its exact mixture peak,
and use that evidence to choose between further linear certificates and a
new nonlinear/case-split bridge. Any individual density improving the true
upper witness must instead pass the unchanged full-shift exact upper checker.
The goal remains actual mathematical progress on Erdős #36, rather than
redefining success as a method diagnostic. This applies the skill's
representation/return obligation and the decision-making dependency test.
