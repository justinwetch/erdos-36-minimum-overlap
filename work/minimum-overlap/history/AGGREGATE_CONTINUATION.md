# Retaining shared-phase aggregates during continuation

The shared84-cell fit uses coarse grids21,28,42,84. For L=dN, the common
phase identity is X_N=(1/d)sum_j B_j X_L B_j'. An interior coarse triangle
therefore has a positive expansion into d^4 ordinary fine triangles with
weight1/d^4 each. The coefficient sum is exactly1. This is the existing
MULTISCALE_GRAM_PROOF.md identity, not a new independent inequality.

The first fit stored36 aggregate inequalities and exported456 nonzero
weighted fine rows in its discovery dual. Importing those exported rows as
individual SDP constraints would create a different constraint set. In
particular, aggregates with zero previous dual multipliers could be lost.
The new --coarse-triangle-seed importer instead reconstructs all stored
aggregate inequalities, ignores their previous multipliers, and refits their
dual weights on the next profile. It checks the grid, interior positions,
signs, exact total expansion weight and the expanded/lifted coefficient match.

A control run on the original profile reproduced the original final actual
mismatch exactly in the displayed doubles:0.004299563066705925 in both runs.
All36 aggregate rows were retained; the maximum coefficient difference
between the lift and expansion was0 in this control. The control took
25.882 seconds. These diagnostics test the representation and history
retention. They do not prove SDP optimality or measure a speedup against a
separately solved fine-row model.

The continued fit uses the newly updated43-row adversary and adds new
aggregate cuts. Its exported proof proposal still contains only ordinary
fine triangle rows with nonnegative exact rational weights. The unchanged
exact compiler must repair and check its full restricted PSD matrix; a
positive literal-profile separation must then be checked before adding a
discovery LP row. Continuous and full mean-cover verification remain due
for any resulting global bound.

The continued84-cell fit finished in164.292s and expanded its dual into2122 ordinary fine rows. Exact PSD repair and the literal-profile check gave separation gap0.007261036190302471. The44-row numerical cap was0.3806113971830304, only4.55e-8 above the43-row cap. The earlier43-row gain was6.04e-8. These small marginal gains, together with the43-row numerical dual standardized weight9.79e-8 for the84 row versus1.43e-5 for a33 row, favor testing deeper33-cell constraints next. Dual sensitivities are properties of one untrusted numerical proposal; no optimality or causal efficacy is inferred.
