# Conditional joint Fourier tilt: discriminator and limit

This is a discovery experiment; no new premise entered a promoted proof.
The earlier scalar odd-tilt route is recorded in ODD_TILT_PLAN.md. The new
experiment jointly changes the even kernel and Fourier phases. It retains
the completing-square cost rather than treating sine coefficients as free.

For C=E cos(xi Z), S=E sin(xi Z), sigma=sin(xi)/xi, the already derived
Fourier inequality is C+alpha*S <= (1+alpha^2)*sigma^2. Thus for lambda>0
and arbitrary b, the universally nonnegative expectation kernel is

    lambda*(sigma^2-cos(xi t)) + sigma^2*b^2/lambda-b*sin(xi t).

The b=0 case is the existing even Fourier row. The perspective b^2/lambda
is convex; the zero-lambda extension requires b=0. The discovery pilot
allows sine coefficients only on the 229 initially positive Fourier
coordinates, with their lambda bounded below by 1e-14. This restricts the
search, and no completeness assertion follows from a failed pilot.

For a positive mean bin [lo,hi], the kernels yplus*(t-lo) and
yminus*(hi-t), yplus,yminus>=0, also have nonnegative expectation. The even
certificate's negative mean-square coefficient is paid at hi^2. Its
normalization therefore remains valid throughout the bin. Gauss quadrature
approximates the positive integral on both shift half-lines; the returned
value is a diagnostic, never an outward-certified lower bound.

The 76-row kernel was tested on [0.003277,0.003279], with 699 variables.
One hundred independent completing-square fixtures passed, and the initial
sine gradient cancelled exactly by reflection. Finite-difference gradient
diagnostics near narrow sign intervals were unstable; this is explicitly
preserved rather than called a passing derivative check.

The optimizer completed 1539 calls in 156.38 seconds. Its order-32 apparent
gain was 1.0153e-9. Re-evaluating the identical saved parameters at orders
16/32/64 gave gains 1.6993e-10 / 1.0153e-9 / 2.0598e-10. Their variation is
comparable to the apparent gain. No exact grammar extension is justified
by this selected test. It proves neither conditional optimality nor that
all joint Fourier-phase approaches fail.

Evidence: runs/hybrid76-conditional-phase-tilt and
runs/hybrid76-conditional-phase-tilt-refinement. The source snapshots and
saved parameter hash bind both runs. No original-problem bound is promoted.

The current normalized mean-square penalty is about 0.7198916893. Its
base second-moment contribution is 0.7198863946; all phase terms together
contribute about 5.295e-6. Consequently sharpening only the alias-error
mean penalty cannot remove the observed global loss of about 2.95e-6.
This is a measured reason to change the next investigation.
