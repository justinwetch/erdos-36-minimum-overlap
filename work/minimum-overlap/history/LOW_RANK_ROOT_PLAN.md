# Full-menu root models

Status: both models implemented and executed. Dense-factor and sparse
candidates passed the unchanged outward checker at mean zero. Global mean
coverage and fresh replay remain pending. No global improvement is
asserted here. The original proposed bridge and its assumptions follow.

The full retained menu has 33,298 discovery variables and only hundreds
of sampled kernel roots. Its diagonal preconditioner improved the
mean-zero score modestly but left a large complementarity residual.
The dense root-Newton implementation cannot simply be applied at this
size: an n-by-n double matrix would take about 8.87 GB for n=33,298,
before the oracle's separate storage and solver workspace.

Within a fixed smooth root topology, if D(v)=2*integral_0^2 Q_v^+ and
Phi(r)=gradient_v Q_v(r), implicit differentiation gives

    Hessian D = sum_roots [2/|Q'_v(r)|] Phi(r) Phi(r)^T = R^T R.

This formula assumes simple roots, complete root enumeration, and no
parameter crossing at a fixed piece boundary. Those assumptions have
failed in earlier discovery runs; objective agreement alone did not
validate derivatives. Do not assert Hessian accuracy from the formula.

A root-feature matrix R with 427 rows and 33,298 columns uses about
114 MB. Matrix-vector products R^T(R d) avoid the n-by-n allocation.
Use the retained root features only as a positive semidefinite quadratic
model, with an explicit denominator floor and positive ridge. Solve a
bounded displacement model in diagonally scaled coordinates, then
accept a step only after evaluating the actual discovery objective.
The ridge and floor change the model and are not mathematical premises
of the final certificate.

Deciding tests before a large pilot:

1. Check the matrix-free quadratic objective and gradient independently
   on small rectangular random factors, including box-active directions.
2. On the compact enriched seed, compare its operator with the existing
   dense root matrix. This checks algebra and scaling, not Hessian truth.
3. Check 32/64 root geometry for the chosen seed; report differences and
   refuse a derivative-accuracy claim if refinement changes them.
4. Run a bounded full-menu pilot, keep the best original-schema proposal,
   measure time and memory, and compare with the already executed diagonal
   pilot. Any candidate improvement needs the unchanged outward checker
   before it can support even a mean-zero claim.

If the low-rank model repeatedly rejects steps or reproduces the small
gain, stop that model rather than loosening a curvature or proof gate.
If it gives a meaningful outward-confirmed gain, rejoin the outer mean
cover and run all independent checks and fresh packaged replay. The
same full original problem and deadline remain in force.

## Executed bridge, October 8, 12:30 UTC

Restoring every retained periodic position and the 48 exact functional rows
gave 33,300 variables. The seed passed the 32/64 discovery geometry check:
the largest gradient difference was 2.30e-12. The dense-factor implementation
`polish_hybrid_root_factor.py` passed rectangular product controls, compact
dense-Hessian algebra comparisons and 67 finite-difference coordinates,
including three box-boundary points. The corrected boundary fixture is v2;
the first fixture had not actually placed its chosen coordinate at zero.

The 12-round dense-factor pilot took 90.19 seconds and improved the numerical
mean-zero bound from .3806107963312777 to .3806108291450862. The unchanged
Arb4 checker returned lower ball .3806108291450501947968166 in 63.57 seconds.
A scoped process sample measured 1,647,992,832 bytes working set and
2,432,843,776 bytes peak working set. Factor buffers alone were 117–241 MB;
their size is not the whole process memory.

The periodic root features admit a sparse-plus-rank-one form. With the same
column scaling as the oracle, write the feature action as

    Phi(d) = S d_s + (B dot d_c - C d_c)/scale + F d_f.

Here C is the transpose of the periodic cell-incidence matrix sampled at
roots, B is the circle-bound vector, and S/F hold scalar, cosine and
functional features. `root_feature_operator.py` implements this action,
its exact structured transpose, and the corresponding PSD surrogate.
The diagonal uses B^2 sum(w) - 2 B(C^T w) + (C^2)^T w; tiny negative
roundoff is clipped in discovery only. No certificate premise changes.

`polish_hybrid_sparse_root.py` passed three rectangular product controls,
adjoint and diagonal controls, 99 finite-difference coordinates with three
boundary points, and compact equivalence to the dense factor (relative
product errors at most 6.85e-16). The warm seed passed 32/64 geometry with
largest gradient difference 1.76e-11. Its 30-round pilot took 118.73 seconds,
improving the numerical mean-zero bound from .3806108291450867 to
.3806109974251118. The last model stored 5,394,984 bytes, versus 245,887,200
bytes for an equivalent dense feature matrix. This excludes oracle and
solver storage. The pilot ended before process sampling, so no sparse
process peak memory measurement exists.

Complementarity improved from approximately -.071 (old diagonal pilot)
to -.0264 (dense factor), then -.00498 (sparse pilot). These are sequential
different-seed pilots, not controlled performance comparisons or proofs of
stationarity. All steps require numerical objective acceptance; these
operators remain surrogates, not verified Hessians. The earlier failed
curvature gate remains failed. Only unchanged outward, independent integer,
full-mean coverage and fresh-copy replay can promote a stronger global bound.

Portable compact algebra control:

    python polish_hybrid_sparse_root.py runs/hybrid46-enriched-circle-newton32-v2/proposal.json --name fresh-sparse-controls --controls-only

Then use a fresh 32/64 geometry report and that implementation-bound control
report for any new full-menu pilot. Each driver retains its CLI seconds
budget independently of the original campaign date.

The longer warm sparse pilot completed 180 rounds in 525.57 seconds and
passed unchanged Arb4 at mean zero after exact premise compression:
.3806110905738071342301465. Its final complementarity was +.00397568;
the sign change still leaves a nonzero residual. A scoped sample of this
different run measured 1,161,535,488 bytes working set and 1,665,175,552
bytes peak working set. It is not a controlled comparison with the earlier
dense pilot. The first sparse pilot still has no process measurement.
The terminal deep proposal compressed to 10 functional premises and 406
nonzero cosines using exact identities; see EXACT_PREMISE_COMPRESSION.md.
