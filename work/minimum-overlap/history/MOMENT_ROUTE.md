# Higher moments: diagnostic, not a universal separator

Center the support at[-1,1], write r=2h-1, and put
a_k=(1/2) integral_-1^1 r(u)u^k du. Mass gives a_0=0; the original overlap
mean m gives a_1=-m/2. For every n>=1, expansion of the bounded-support
moment generating functions yields

    E_p t^(2n) = 2^(2n+1)/[(2n+1)(2n+2)]
                 - sum_{k=0}^{2n} (-1)^k binom(2n,k) a_k a_(2n-k).

Indeed H(z)=sinh(z)/z+A(z), G(z)=sinh(z)/z-A(z), with
A(z)=sum a_k z^k/k!. The even part of H(-z)G(z) is
(sinh(z)/z)^2-A(-z)A(z). All series converge everywhere because the support
is bounded. This proves the identity without assuming h is symmetric.

For mean zero, the fourth and sixth moments reduce to

    E_p t^4 =16/15-6a_2^2,
    E_p t^6 =16/7-30a_2*a_4+20a_3^2.

An initial test fixing a_3=0 found no sixth-moment separation: at the relaxed
profile's implied a_2~.1689045, a box-constrained even r can have a_4 as large
as~.16065; its necessary sixth-moment lower bound~1.47168 is below the
profile's~1.55976. These are numerical diagnostics.

For an even r all odd a_k vanish, and the identities recursively reconstruct
its even moments from p's even moments, beginning a_2>0. moment_reconstruction.py
tested whether an even piecewise-constant r in[-1,1] could have those moments.
On4000 cells, scaled LPs match the requirements through p degree10 with
residuals below1e-11; they report infeasibility beginning at degree12.
This is neither a continuous infeasibility certificate nor an obstruction
for general h. Unscaled LPs dropped tiny coefficients and gave larger
residuals~1e-7, so scaled runs supersede those feasibility diagnostics.

The deciding extension allowed odd moments and general r. moment_fit_general.py
fits the full binomial identities, mass and mean, in a Legendre-scaled residual
basis using200 cells. Its best executed degree12 run has maximum scaled
residual~7.42e-10. A separate direct convolution and piecewise-affine integral
check confirms raw even-moment differences ranging from~2.7e-9 at degree4
to~1.57e-6 at degree12. Mass h differs from1 by~6.5e-13, and box constraints
hold numerically. The fit has substantial reflection asymmetry.

Thus the apparent symmetric obstruction is fragile once the omitted odd
moments are restored. This does not prove exact moment compatibility, match
the complete relaxed profile, or construct an improved upper witness.
Before using this route for a lower bound, a separator must apply to general
h, survive the odd-moment freedom, and yield a useful objective gain after
reoptimization. Another symmetric-only numerical infeasibility test would
not discharge that obligation.

Records: runs/moment-reconstruction-scaled-circle1/summary.json,
runs/moment-fit-general12-exact/summary.json and direct-convolution.json.
