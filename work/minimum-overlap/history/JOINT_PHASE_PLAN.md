# One shared profile across several phase-Gram cones

The sequential method fits each phase grid to an adversarial profile and
exports one separating functional at a time. Its retained finite list of
cuts is an outer approximation to the simultaneous phase feasibility
problem. The next bounded discovery test puts several Gram matrices and
one common profile in the same optimization, then exports their separate
dual functionals through the existing exact grammar.

Use a step profile p on a fixed discovery grid, mass and second moment,
cap M, all retained Fourier and periodic inequalities, and all 45 checked
Gram rows. For phase grids 31,33,43 introduce restricted PSD matrices Y_N
with X_N=V_N Y_N V_N', X_N*1=0, endpoint/interior diagonal bounds, the
mean-zero alias bound, and retained ordinary triangle inequalities. Tie
every phase hat average b_k-a*sum diag_k(X_N)/4 to the exact hat integral
of this same p. Minimize M in the numerical model.

If equality multipliers gamma_N are available, box/mean/triangle duals
compile into precisely the existing signed phase-functional format.
Certify every functional independently, including PSD repair and integer
Bareiss replay. A numerical shared cap is not a bound. An exported exact
separator can be added to the fine discovery LP, then any proposed bound
must survive the unchanged continuous checker, complete mean coverage,
independent arithmetic and fresh package replay.

The fixed step discovery grid introduces a restriction and possible
discretization artefacts. They may affect proposal quality, never the
meaning of the checked final result. Nothing from the shared profile or
solver feasibility becomes a proof premise. Use a bounded solve rather
than repeatedly extending time on a failed cone. The deciding outcome is
new useful exact functionals on the fine adversarial profile and their
independently checked continuous gain.

The 512-cell shared model completed in18.64seconds, with an inaccurate
numerical cap0.3809038352857441. This exceeded the retained actual upper
construction and was not promoted. A same-grid control without the three
explicit phase cones gave0.3808447373999421. Both fixed step-profile values
have substantial discretization restrictions relative to the fine4096-cell
frontier0.3806114549094438.

All three exported functionals independently passed exact PSD repair and
the unchanged integer checker. Their exact gaps on the fine adversarial
profile were negative: approximately -7.37e-6 (grid31), -7.00e-6 (grid33),
and -0.00038325 (grid43). No rows were added and no new bound followed.
The4096-cell shared model then failed in CLARABEL after its model had been
constructed; it supplied no usable primal/dual or certificate. Its traceback
is preserved. Increasing solver time alone is not the next action.

One possible conditioning repair would replace, rather than duplicate,
the old functional rows whose entire phase cones are now present, while
retaining the union of their triangle premises. This requires checking
each represented row's mean, nonnegativity and other premise types before
claiming cone containment. It is only a proposed numerical repair and is
deferred while bounded spectral refinement and the updated120-cell
common-phase fit produce independent evidence.
