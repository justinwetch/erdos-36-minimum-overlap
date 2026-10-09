# Restoring omitted periodic dual directions

Status: bounded discovery experiments completed; no new global bound.
The promoted46 checkpoint remains0.380609298 after all8 fresh checks.

The continuous optimizer constructs its periodic variables only where the
input certificate has a strictly negative z coefficient. Consequently it
cannot activate inequalities assigned zero weight by the fixed-grid LP.
This is a restriction of the search, not of the universal certificate.
The independently reconstructed Newton positive-set profile violates172
omitted periodic constraints, with maximum violation0.2918457598. The
maximum violation among already active periodic rows is1.58684e-5.
Thus further polishing the same active set cannot repair the main
feasibility defect. This is stronger deciding evidence than the residual
of the moment alone.

For a periodic family with coefficient matrix C and bound B, the exact
existing premise is integral T p <= B, where T=C R/(2a) on positive-half
base cells, a=2/n, and R folds p(t)+p(2-t). For a cell-average profile p,
the full integral is2a*T*p=C R p. All signs and normalizations therefore
match the original finite LP and the existing circle compiler.

enrich_circle_active.py selects the64 most violated omitted rows, sets
their z to-epsilon, and adds epsilon*B per row to y0. This preserves the
numerator exactly and adds epsilon*(B-T) to Q. The negative gradient
on the virtual profile supplies a genuine local descent direction when
its geometry is accurate. The chosen epsilon is discovery data, not a
guarantee that a finite perturbation improves the objective. The first
serialization used rational fraction strings which the numerical Oracle
cannot parse; the corrected helper writes terminating exact decimal
strings and checks their rational equality. No proof checker changed.

The enriched seed is optimized with32 sign subdivisions and a constrained
curvature model with actual-objective line search. Any result still needs
unchanged Arb checking, an independent sign-geometry refinement if used as
a new target, full mean coverage, integer replay and fresh packaging.

The alternative nearest-profile repair required about0.12319 in L1 at
cap0.380612, so the original virtual profile was not nearly feasible under
all retained constraints. Both interior point and dual simplex returned
a maximum residual1.10504e-8 against the fixed1e-8 gate, including after
tightened primal tolerances. Their profiles remain failed prerequisites;
solver status alone is not accepted. That route is deferred rather than
used as evidence of a valid original overlap or upper bound.

Next decision after enrichment: if it gives a useful independently
checked improvement, restore newly violated inactive rows in a bounded
exchange loop. Otherwise compare a new phase-grid menu against the latest
fully constrained LP profile, or refine a distinct actual upper density
from the convex-response pool. Keep at most these three routes active.

The64-row enriched Newton pilot ended at mean-zero numerical estimate
0.3806107864031534 in42.498s, only9.79e-9 above the preceding candidate.
A broader test then restored all483 retained Fourier frequencies,46
checked functionals and8 periodic families, activating32768 periodic
positions with a tiny exact numerator-preserving seed. The resulting
33298-variable pilot uses sparse curvature-diagonal statistics, avoiding
a dense full Hessian. Its180s budget is a bounded test of the active-set
restriction. An unchanged Arb4 check is required before using its score;
no numerical feasible-profile or global optimality claim follows.
