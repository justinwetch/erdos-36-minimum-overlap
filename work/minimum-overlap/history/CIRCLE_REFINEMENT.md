# Exact finer-grid continuation

The central certificate's periodic multipliers live on a finite grid.
Doubling that grid opens additional supported coordinates without
requiring a new inequality or changing the starting kernel.

For each family, replace a multiplier z_i by z_i/2 in both cells 2i and
2i+1. Keep every Fourier, polynomial and Gram term unchanged. The
normalizing expectation is unchanged because the sum of multipliers in
each family is unchanged.

For a dilation k, the original coefficient z_i/k is distributed over the
k consecutive cells starting at ki, modulo n. On the doubled grid, the
two half multipliers distribute z_i/(2k) over 2k consecutive fine cells
starting at 2ki, modulo 2n. These are exactly the two fine children of
each original cell. The factor 1/(2h) in the kernel doubles when h halves,
so the fine kernel coefficients equal the original coefficients, repeated
twice. Reflection pairs the same children in reverse order. Thus the
full periodic offset is identical pointwise away from finitely many
irrelevant endpoints. All remaining kernel terms are literally identical.

refine_circle_seed.py checks this coefficient identity with exact
rational arithmetic. Three fixtures cover different grids and wrapped
dilations; the actual 4096-to-8192 starting kernel also passed. The
optimizer may subsequently vary the two children independently, retaining
nonpositive family multipliers under the existing proof grammar.

This is an exact inclusion of the old search space in a richer one,
without a guarantee of improvement. Numerical objective gains must still
pass the unchanged central checkers, energy/capacity return where used,
complete mean cover, negative controls and full fresh replay. A better
mean-zero score alone does not improve the global bound.

The deciding comparison is a bounded search with an exactly identical
initial kernel, followed by the continuous outward check. This avoids
confounding a new grid with a changed starting score or a weakened
mathematical contract.
