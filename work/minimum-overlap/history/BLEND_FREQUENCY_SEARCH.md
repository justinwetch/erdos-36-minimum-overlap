# Frequency perturbation discriminator

The shared-mean search changes Fourier multipliers and phases at fixed
frequencies. A separate numerical test changes selected frequencies while
retaining their multipliers, phase ratios, all Gram premises and the exact
shared-mean numerator. For a phase term with multiplier w, phase alpha and
frequency xi, the kernel contribution is

    w[(1+alpha^2)sinc(xi)^2-cos(xi*t)-alpha*sin(xi*t)].

Its frequency derivative is

    w[(1+alpha^2)(sinc(xi)^2)' + t(sin(xi*t)-alpha*cos(xi*t))].

All unchanged proof checkers recompute the RHS at the exported decimal
frequency. This test introduces no new proof grammar. Its numerical positive-
part integral uses Gauss quadrature; any gain requires independent export
reevaluation, continuum integration, complete mean coverage and fresh replay.

The first implementation passed five isolated derivative fixtures but stopped
at its actual-kernel finite-difference gate (step1e-5, hinge smoothing1e-8).
No optimization result was produced. Its original actual derivative residuals
were not saved. The separately versioned v2 records every residual at four
steps and two smoothing scales, and requires an accurate scale for both
objectives before proceeding. This distinguishes a finite-difference step
crossing many nearly active quadrature nodes from a persistent analytic
derivative error. The executed records decide whether that repair succeeds.

Evidence is under runs/hybrid82-shared-frequency-lower-v1 and v2, with the
fork provenance runs/blend-frequency-v2-fork.json. These are numerical
discriminators, with no continuum, optimality or causal efficacy claim.
