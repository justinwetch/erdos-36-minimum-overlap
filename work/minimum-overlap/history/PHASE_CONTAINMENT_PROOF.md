# Replacing implied rows in a shared phase-cone model

Status: exact discovery-row containment audit executed. This is a model
conditioning experiment, not a new bound or a change to trusted checkers.

Fix a phase grid N and the cone from PHASE_GRAM_PROOF.md: X is positive
semidefinite, X*1=0, with the established interior/endpoint diagonal
bounds, mean-zero bound c'Xc<=1/12, nonnegative overlap hat averages y_k,
and a specified finite list of triangle inequalities. The numerical model
ties every y_k exactly to the corresponding triangular average of one
common step profile p. Step profiles are a discovery restriction only.

A checked signed functional on this same grid has rational multipliers,
hat weights gamma, restricted PSD matrix G and lower constant L. Its
compiler identity writes gamma*y as L+trace(GX) plus a nonnegative
weighted sum of premise slacks. Thus gamma*y>=L on the exact cone if
every used premise is retained. The restricted PSD test suffices because
the range of X lies in1-perp. A larger source mean-error constant than
1/12 only weakens that source inequality and does not obstruct containment.

`audit_phase_containment.py` verifies each selected source certificate and
report hash, reexecutes exact integer PSD, reconstructs L and every
rational step-profile row coefficient, and checks its float projection.
It unions all nonzero source triangle premises with the retained grid
seeds. Every hat nonnegativity premise is included. Unsupported circle
premises, other grids or nonzero mean intervals remain explicit rows.
Nothing is removed merely because its grid number matches a cone.

For frontier50 and grids31/33/43, all12 selected rows passed;38 rows
remain explicit. The cone triangle counts are191,324,522. Controls accept
one correctly normalized row and reject corrupt rational coefficients,
rational RHS and float RHS. The executed audit took2.7355 seconds.

`joint_phase_reconditioned.py` binds that plan's input/implementation hashes
before constructing the model. Its `--retain-contained` arm keeps all50
old rows with identical explicit cones, permitting a paired conditioning
control. The optimized hat-matrix builder has executed comparisons against
the legacy builder on three nondivisor grids and retains the independent
hat-average diagnostic on each actual model. Numerical equality or solver
success is not an exact cone-feasibility or global proof claim.

Any exported dual uses the existing signed-functional schema. Exact repair,
the unchanged integer checker, a positive exact gap on the fine adversary,
continuous outward integration, complete mean coverage and fresh replay
remain necessary before promoting a new original-problem bound.

The first4096-cell solve failed in21.2097 seconds. The paired arm retaining
all50 rows also failed, at iteration1 with NumericalError. A fixed-cone
FAER backend test passed an analytic2x2 SDP but reproduced the same failure.
SCS returned a poor approximate point: cap.4316635 and maximum constraint
defect.253726. All three SCS duals were repaired and passed unchanged exact
PSD, but their gaps on the fine adversary were negative (-.00174,-.00160,
-.00484). None was added. These outcomes refute duplicate rows or backend
choice alone as sufficient repairs; they supply no infeasibility proof.

The captured equality block has112 rows and floating rank109, with three
singular values below1.7e-16 and RHS residuals below8e-16. An exact identity
explains the dependencies. With a=2/N and the established hat normalization,

    a*(y_0/2 + sum_{k=1}^N y_k) = integral_0^2 p(t)dt = 1/2.

The hats partition unity. The same weighted base sum is exactly1/2, and
the corresponding covariance matrix is (1/2)*11', which vanishes after
restriction to1-perp. Thus, given mass and the first N hat matches, the
last match is implied. One matching equality can be omitted from each
phase cone without weakening the exact model. Its exported multiplier is
zero. Every hat nonnegativity constraint remains explicit.

The rational basis U=[I;-1'] used by the exact checker avoids dense
near-zero orthonormal-basis coefficients. Any X>=0 with X1=0 has a unique
representation X=U Y U', where Y is its leading N-by-N block and Y>=0.
Conversely every Y>=0 gives such an X. This is a cone-coordinate change,
not a relaxation. Changing the basis alone still failed. Starting from
that exact-basis formulation, removing the three dependent hat equations
returned AlmostSolved in48.7074 solver seconds (66.9671 total), numerical
cap.38062092422201543, maximum constraint defect7.43e-9. This is a discovery
improvement, not a promoted bound or a general solver-performance claim.

All three actual grids passed exact rational base and restricted-matrix
identities; their numerical hat-partition residuals were exactly0 in the
executed floating calculation. The independent exact dual return is
recorded separately and remains decisive for any claimed improvement.

All three independent-hat duals passed exact PSD repair and unchanged
integer verification. The31-grid gap was positive8.26950e-9;33 was negative
8.08263e-9 and was excluded;43 was positive1.01274e-5. The two positive
rows were added to the retained fine LP, yielding52 rows and numerical
cap.38062090431776086. That LP returned Unknown, not an optimality
certificate. Its extracted proposal has7 active phase functionals and213
cosines. Independent continuous outward and actual-witness checks are
running before any global preparation or claim. No optimality inference
depends on either approximate solver status.

The direct unchanged Arb4 mean-zero check passed at
.3806186050193697690569250. All7 active functionals passed exact consistency
on the supplied7168-cell admissible density. A120-round sparse root pilot
then reached numerical.38061974567876494 in49.3925 seconds; unchanged Arb4
passed at.3806197456787248403844698. These are central-case results only.

The initial global target.380616807 exposed two outer cases at
|mean| in[.003125,.00625] whose old certificate gave only.380613607.
Adaptive reuse of three valid Fourier parents split that positive interval
into5 leaves and reflected them. The new204-bin source has186 selected
outer cases; both unchanged outer implementations passed at.380616807.
Two preexisting sub-1e-12 endpoint mismatches were explicitly aligned in
the new certificate and replayed, matching the established tiny-gap
repair rather than assuming coverage. The initial strict-adjacency
construction failure is preserved. Exact central integer integration and
the corrected full-mean audit passed at.380616807; fresh package replay
is pending. The polished global preparation targets.380617915, also
unpromoted until all independent and fresh replay obligations pass.

Update, October 8 at 14:16 UTC: all eight fresh packaged baseline commands
passed in 370.237 seconds, with all 37 distributed files unchanged. Thus
the global lower bound .380616807 is promoted. The polished .380617915
target passed its original independent checks and exact global audit;
its fresh-copy replay is still pending. These statements supersede the
pending baseline status immediately above.

The adaptive shared driver now saves each actual covariance matrix and
successfully solved dual before adding constraints. At most 30 new violated
triangle inequalities per model are added per round. All four sign patterns
are checked on the eight vertices of [-1,1]^3; their maxima are exactly one.
Their multiaffine form therefore proves the inequalities throughout that
cube. A known invalid covariance triple triggers a violation of 1.7, while
a valid rank-one all-ones example triggers none. Existing rows are deduplicated.
Canonicalization is charged to the wall budget, and a later failed solve
leaves the last solved exports intact. None of this changes the exact
compiler, checker, or accepted certificate grammar.

Further executed results, October 8 at 14:34 UTC: the larger shared
43/59/61 cones returned one useful exact 61-grid functional. With two
earlier adaptive rows, this gives a 55-row retained frontier. The baseline
global .380621480 passed all eight fresh packaged checks in 139.086 seconds.
A compact root polish then raised the global target to .380622152; all
eight fresh checks passed in 154.147 seconds. Both packages retain 37
unchanged manifest-bound files. Thus .380622152 is the strongest promoted
global lower bound at this time. The unchanged exact nonuniform upper
bound remains .3808585738366948659232792.

A simultaneous five-cone model returned four more useful exact functionals,
giving a 59-row frontier. Its retained numerical LP cap is .3806261148893905,
and independent continuous Arb4 gives mean-zero .38062428902446891916.
Neither is a global lower claim. A bounded root polish reaches numerical
mean-zero .38062505647916806; its global checks remain pending.

An isolated pentagon probe tests -sum(i<j) s_i*s_j*r_i*r_j <= 2 on five
bounded coordinates, for each sign vector with s_0=1. The expression is
multiaffine; at vertices its value is (5-(sum s_i*r_i)^2)/2 <= 2. Exact
vertex controls pass for all 16 patterns. The PSD matrix with diagonal one
and off-diagonal -1/4 passes every triangle inequality but violates the
all-plus pentagon by 1/2. Thus this is a genuinely stronger premise.

However, the paired fixed five-cone numerical test added 40 such rows
and moved the cap only from .38062632701655985 to .38062640844963275,
about 8.14e-8. This did not meet the preselected 1e-6 gain needed to justify
a new exact grammar. It is deferred, not refuted. The probe suppressed all
functional exports; no pentagon premise entered any promoted certificate,
and no trusted checker was changed.
