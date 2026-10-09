# Merging the endpoint phase cells

Status: derived strengthening of the necessary row in
[JOINT_ALIAS_TRACE.md](JOINT_ALIAS_TRACE.md), with exact physical fixtures.
It has no production certificate grammar, compiled dual or global bound.
No novelty claim is made.

Keep n, a=2/n, r, w, v, X and c from that note. The endpoint phase cells
are partial cells: cell 0 intersects [0,s+a], and cell n intersects
[s+2,2], for s in [-a,0]. Merge these two intervals into one circular
cell. Their total length is a. They are disjoint from all interior cells
and together these n circular cells partition [0,2].

Since w is a-periodic with integral zero per period, its integral over
the merged endpoint pieces is zero as well: translate the right endpoint
piece back by 2-a, an integer multiple of a, to obtain [s+a,a]. The left
piece is [0,s+a]. Thus the merged cell's average of r is its average of v,
and is exactly r_0(s)+r_n(s), with the same denominator a used for both
partial-cell averages.

Jensen on each circular cell now gives the stronger energy budget

    a * [sum_(i=1)^(n-1) r_i(s)^2 + (r_0(s)+r_n(s))^2]
      <= ||v||_2^2 <= 2-||w||_2^2.

Average over phases and combine with the unchanged alias-variance bound
from the same w. The result is

    c^T X c + (a/19) * [trace(X)+2*X_0n]
      <= 2/19 + (m/a)^2.

This is at least as strong as the previous interior-trace row because
`X_00+X_nn+2*X_0n = E[(r_0+r_n)^2] >= 0`. It does not replace this
quantity by either endpoint diagonal alone. The off-diagonal term is
essential. In matrix form its extra term over the old joint row is the
positive semidefinite rank-one matrix
`(a/19)*(e_0+e_n)*(e_0+e_n)^T`.

The argument applies to every bounded measurable admissible density;
Jensen is used on sets of total measure a and the same physical r supplies
all cells and the projection. There is no independence assumption.

`check_circular_alias_projection.py` checks exact phase integrals for
24 piecewise constant physical densities, including nonzero moments,
alias-sharp periodic densities and a step density. It compares both row
left sides, checks the stronger projection-energy budget, and includes
cases with a strictly positive merged-endpoint contribution. These are
fixtures; the universal argument is the one above.

To use this row for discovery, change the SDP row and its dual-matrix
reconstruction together. A positive multiplier adds the rank-one matrix
above. Reusing the old compiled functional's scalar improvement without
reconstructing its changed matrix would not compile this stronger row.
The current signed-functional replay and global lower-bound proofs use
their original immutable premises and remain separate.
