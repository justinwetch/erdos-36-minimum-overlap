# A common Fourier phase vector: proposed nonlinear route

The exact convex-mixture ceiling motivates a necessary condition that keeps
one density's Fourier coefficients coherent. This is a proposed route, not
a new lower bound or a certified infeasibility result.

For k>=1 let H_k=integral_[0,2] h(x) exp(i*pi*k*x) dx and H_0=1. Since
g=1-h has mass one and its nonzero integer Fourier coefficients are -H_k,
the two Toeplitz matrices with diagonal 1 and off-diagonals respectively
H_(j-i) and -H_(j-i) are positive semidefinite at every finite order.
Indeed each quadratic form is the integral of h or g times the squared
modulus of the corresponding trigonometric polynomial. Equivalently, if
T has zero diagonal and these H off-diagonals, -I<=T<=I.

The overlap convolution identity gives

    integral p(t) cos(pi*k*t) dt = -|H_k|^2, k>=1.

Here Fourier convolution multiplies H_k by the conjugate of -H_k. The
sine part is zero at these integer frequencies, even if p is asymmetric.
Thus a literal even overlap profile determines the magnitudes |H_k|, but
one common choice of phases must make both finite Toeplitz matrices PSD.
Separate positive Fourier-magnitude tests do not enforce this common choice.

The sufficient bridge is explicit: if all full-shift profiles with cap M
and all valid existing constraints can be excluded from admitting any
such common finite phase vector, then no original admissible density has
cap<=M. A local numerical phase search cannot prove that exclusion.
Conversely a successful finite phase fit proves only feasibility of this
necessary finite test, not existence of a density or overlap construction.
Any rigorous exclusion must handle all phases and the full continuum
profile family, using certified subdivision, an exact polynomial
certificate, or another uniform argument. Those obligations remain open.

Cheapest prerequisite: verify nonnegative squared magnitudes before a
phase fit. The 45-row adversarial step profile violated this basic test:
among integer modes 1..64, sixteen squared magnitudes were below -1e-10;
the smallest was about -0.00313416. Such a profile already fails an ordinary
linear Fourier inequality. Fitting phases after clipping those entries
would test a changed profile. First add all 64 integer-frequency tests to
the discovery frontier, retain all 45 exact Gram rows, and re-extract the
dual. Only then attempt a phase fit, or use actual mixture witnesses for
which every magnitude is automatically nonnegative.

This ordering applies the skill's common-witness obligation and attacks
the weakest prerequisite first. It also preserves a direct return to the
original minimum-overlap objective. The separate mixture diagnostic is
completed evidence, rather than a substitute target.

Executed prerequisite: adding all 64 integer modes retained all 45 Gram
rows, passed exact row association during re-extraction, and completed in
31.52 seconds. The new numerical cap was 0.3806114549094438, versus the
earlier unfinished 0.3806113797136458. All displayed squared magnitudes
were nonnegative (minimum about 2.54e-12). This is a bounded discovery
result, not an optimality or original-bound claim.

The strongest actual mixture also passed local common-phase feasibility
tests at Toeplitz orders 32 and 64. Best displayed spectral norms were
0.9999999999929408 and 1.0000000002111518. The latter is within the declared
1e-9 numerical tolerance, not an exact PSD claim. The spectral objective
gradient passed five finite-difference coordinates with maximum error
4.30e-9, and a known admissible density passed the order-32 control.
These fits give no exclusion. Simply increasing the integer order is
deferred pending a stronger discriminator.

The integer-frequency representation retains only a periodic folding of
the nonperiodic autocorrelation. A proposed next test restores support
information with spacing delta=pi/2. Use centered Fourier coefficients
Z_k=integral r(x) exp(i*k*delta*(x-1)) dx and
U_k=integral exp(i*k*delta*(x-1)) dx=2*sin(k*delta)/(k*delta), with U_0=2 and Z_0=0.
For one density, both finite Toeplitz matrices U+Z and U-Z are PSD, since
they are the Gram integrals weighted by 2h and 2g. The full even profile
determines |Z_k|^2 by the Fourier transform of R=triangular-support-4e.
For a mixture this magnitude can be computed directly by averaging the
components' |Z_k|^2. One common phase vector must satisfy the two matrices.
The nonzero, fixed U off-diagonals prevent the free phase gauge used by the
integer model. Keep all phases as variables.

Cheapest falsifier: order 12 with this fixed U, the known actual density as
a positive control, and the exact mixture as the candidate. Check objective
gradients independently. A successful numerical fit weakens this route;
failed local fits do not prove infeasibility. U becomes ill-conditioned as
the order grows, so report raw eigenvalue residuals and avoid unvalidated
whitening or interpreting numerical rank as exact. Any global lower claim
still requires uniform phase/profile exclusion and the continuum return.

Executed support-aware order12: all five gradient coordinates passed
(maximum error3.24e-9), the actual-density control had minimum eigenvalues
8.12e-11 and9.38e-8, and the integer-coefficient return differed by less
than6.85e-16. Complementing the density swapped the two matrices as required.
The sixth start found mixture phases with minimum eigenvalues approximately
-4.45e-11 and2.42e-9, within the declared1e-9 numerical tolerance. It gives
no exclusion or exact PSD claim. The finite support matrix itself had
minimum eigenvalue7.11e-8; no whitening or numerical rank assumption was
used. This weak test is deferred in favor of a different construction
return and shared-profile phase-Gram discovery, recorded separately.
