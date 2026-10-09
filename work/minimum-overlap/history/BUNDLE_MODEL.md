# Proximal bundle discriminator

Status: algebra controls passed; two bounded pilots exposed master precision
failures. Captured-master comparison supports a scaling repair. The new
100-step pilot finished, with a small accepted numerical improvement.
No new bound, convergence claim or measured speed comparison.

The calibrated full retained menu has 455 oracle-coordinate derivatives
below -1e-8, with minimum approximately -.0185876. Their 32/64 comparison
agrees within 7.58e-11. The earlier root quadratic models accept many small
steps but have not removed this obstruction. A different finite model can
retain observed values/gradients instead of using root curvature.

Store numerical planes alpha_i + g_i dot v, where alpha_i=D_i-g_i dot v_i.
Around center c use scaled displacements v=c+S*u and bounded u. The master is

    min_{lo<=u<=hi} max_i(beta_i + H_i dot u) + rho/2 * ||u||^2,
    H_i=g_i*S, beta_i=alpha_i+g_i dot c-D(c), rho>0.

For simplex weights lambda, put p=H^T lambda and

    u(lambda)=clip(-p/rho,lo,hi),
    q(lambda)=lambda dot beta+p dot u+rho/2 * ||u||^2.

This is the finite master's concave dual. Its gradient is beta+H*u.
The box minimizer is unique because rho>0; minimax duality applies to the
compact convex box and simplex. The reported primal/dual gap concerns only
this finite model. The planes use numerically sampled derivatives and are
not certified supports of the true continuous objective. Consequently the
master value and its gap are never bounds or proof gaps for the original
problem. The root diagonal is used only for positive coordinate scaling.

The pilot evaluates every proposed displacement in the original numerical
oracle. A sufficient actual decrease moves the center; a null step adds
the observed plane. Best actual proposals remain in the unchanged schema.
Outward interval, independent integer, full-mean cover and fresh replay
remain the only promotion route. No trusted checker or grammar changes.

`polish_hybrid_bundle.py` controls passed 16 dual finite differences with
maximum error2.20e-10, a known shifted positive-part minimizer and a
one-plane boxed closed-form minimum. The first pilot uses at most30 stored
gradients, avoiding an n-by-n matrix. This is an allocation description,
not a whole-process memory or performance measurement.

The first 100-step pilot improved the numerical mean-zero bound by only
8.87e-10. Late solver success flags accompanied master gaps larger than
predicted gains. An analytic scale-invariance control failed after a
1e-8 rescaling. Version2 normalizes the dual objective and passes that
control, but a second pilot stopped at the unchanged master-precision
gate: gap 3.70e-11, above the allowed fraction of predicted decrease.
It accepted no steps. These failures are retained rather than reported
as convergence or a new bound.

An added large positive coordinate constrained to [0,1] leaves the known
analytic minimizer unchanged. Version2 passed that control at scales 1,
1e-8 and 1e-12; this refutes the proposed simple asymmetric-box scaling
explanation on that fixture. The real failing master will be captured
before choosing a repair. No precision gate has been loosened.

The captured real failure has33314 variables and3 planes. On exactly that
fixture, absolute-span scaling uses units .000988546 and returns gap
3.6950984e-11, failing the existing gate. Scaling by the maximum attainable
row descent and the proximal bound uses units4.6185351e-7 and returns gap
1.3238574e-16, passing. This is a numerical comparison on a fixed fixture,
not an exact optimality certificate. Version3 uses

    units=max(max|beta_i|, max_i|sum_j min(H_ij*lo_j,H_ij*hi_j)|,
              rho/2*max(||lo||^2,||hi||^2), 1e-300).

Analytic scale and irrelevant-coordinate controls still pass. The new
pilot retains the same master precision gate and actual acceptance test.
The pilot completed in91.4024 seconds at mean-zero .38061110707971774,
gain1.48622e-9 over its own seed. It is weaker than the separate new
order43 sparse candidate. Complementarity remains -.00268042, so neither
convergence nor useful stationarity has been established. The fixed-master
repair is supported; another long unchanged bundle run is deferred because
the actual bound gain is small. This comparison has different seeds and
does not establish superiority or causal performance of either optimizer.
