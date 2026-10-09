# Finer actual-density discriminator

The retained uniform witness had 7168 cells. Repeating each cell twice
represents exactly the same density, rather than a new relaxed profile.
lift_uniform_witness.py checked its mass, box and every overlap knot in
both representations using two exact summation organizations. The exact
scores agreed. The 14336-cell representation has 28671 nontrivial shift
knots; piecewise affinity covers all intervening shifts.

An all-cell projected optimization from this identical density completed
4674 calls. Its exact score is

    389999179606768536975690608486141 /
    1024000000000000000000000000000000.

Thus the explicit uniform construction gives the strict upper decimal
0.3808585738347348993903229. The unchanged direct integer checker and
independent packed polynomial checker agree exactly. This improves the
earlier promoted nonuniform upper bound by about 1.96e-12. It is a tiny
refinement and does not materially close the open gap.

A second seed split each old cell into opposite rational perturbations,
preserving its average exactly. The perturbation was bounded by one ten-
thousandth of its box headroom, with recorded deterministic signs. Nine
exact pair/mass/box fixtures and all 28671 seed shifts passed. Projected
optimization from this different seed finished 7487 calls, with exact
feasible score about 0.3808585753727086. It remained above the incumbent.
These observations do not prove a resolution barrier or local optimality.

Four fractional circular-cut segments of the stronger uniform density
were then searched. The exact packed-anchor return selected integer cut
-1 and fraction 19999999929378691/20000000000000000. Its exact score is

    10919977028984812147789295189227209 /
    28672000000000000000000000000000000,

with strict upper decimal 0.3808585738345707361812673. The extra gain over
the finer uniform construction is about 1.64e-13. Independent nonuniform
integration and fresh-copy replay are mandatory before promotion; their
executed reports, rather than this note, establish the current status.

Evidence: runs/leader-refine14336, runs/leader-refine14336-projected,
runs/leader-refine14336-subcell, runs/leader-refine14336-subcell-projected,
runs/leader-refine14336-fractional and runs/leader-refine14336-fractional-exact.
The optimization is a construction search, with no optimality, priority or
causal skill-efficacy claim.

Promotion 2026-10-08T16:38:16.795207+00:00: unchanged nonuniform checker and corrected metadata
package v2 all5fresh replay PASS, 135.064336s. Interval upper is now
0.3808585738345707361812673. First package remains frozen with stale dependency wording;
v2 fixes that statement and was independently replayed.
