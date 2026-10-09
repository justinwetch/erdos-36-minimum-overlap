# Smoothing nearly flat kernels during discovery

The continuous dual objective is twice the integral of Q_+ on [0,2].
Its gradient can change sharply when a nearly zero kernel interval changes
sign. The current virtual positive-set profile is therefore useful for
proposing missing coordinates, but is not an admissible overlap density
or a certificate of stationarity.

polish_hybrid_softplus.py searches a different, explicitly untrusted model:
replace q_+ by epsilon log(1+exp(q/epsilon)) and integrate by Gauss
quadrature separately on every affine-kernel cell. The gradient is the
exact derivative of that finite quadrature model. The periodic multiplier
and functional coordinates retain their existing nonnegative parameter
bounds. Seven finite-difference fixtures check the softplus model algebra.

For exact integration, the replacement error would lie between zero and
4 epsilon log(2), since the positive half-domain has length two and the
objective doubles it. The quadrature has an additional, unpaid error.
Consequently no quadrature value or smoothing estimate is a proved bound.

Every twenty calls, and at every temperature transition, the existing
analytic-root discovery oracle evaluates the candidate. Only candidates
improving that separate numerical objective are exported. This still does
not prove root completeness. A useful export must pass the unchanged
outward central verifiers, a complete mean cover, relevant controls and
full fresh-copy replay before changing the promoted result. The known
verified checkpoint is retained throughout this experiment.
