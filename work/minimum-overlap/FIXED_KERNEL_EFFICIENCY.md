# Arithmetic loss in the frozen pre-SCS kernel

The isolated diagnostic in fixed_kernel_efficiency.py encloses the ratio
of the mean-zero expectation numerator to the actual positive-part integral
of the frozen H91 131072-cell kernel (SHA-256
c06dd9d43317f406d11f13ed103e5a399557562eacbbc32682d03c78589bd1c3).
This is the kernel before the new H97 SCS functional was added. Its outward
enclosure, rounded further
outward for readability, is

    0.38062741888158 <= fixed-kernel ratio <= 0.38062741888349.

The upper endpoint is **not an upper bound on mu**, on another kernel,
or on the full method. It concerns this one scalar expectation certificate.
Its width, about 1.893e-12, measures the remaining integral-enclosure loss
at mean zero. Changing the kernel or adding valid premises can change this
ratio; the enclosure does not certify numerical optimization.

The diagnostic forks the original Arb integration only to add a lower
integral. Each rigorously positive cell contributes the lower endpoint of
its exact antiderivative difference, clamped at zero. Negative cells and
ambiguous cells contribute zero to this lower integral. The original
positive-integral upper bound is retained. Five exact polynomial and
aligned-jump fixtures passed. The source-frozen replay binds all analytic
implementations, the source checker and the actual kernel before and after
execution. It took 77.404 seconds on the shared machine.

Reports: runs/hybrid98-fixed-kernel-efficiency-v3.json and
runs/hybrid98-fixed-kernel-efficiency-replay.json. An initial control used
a stronger-than-needed Arb ball ordering test at 4/3; its failed log is
retained. The corrected control compares exact rational endpoints. A later
run interrupted during a control-only source edit was discarded and the
unchanged-source v3 replay supplies the accepted diagnostic evidence.
No frozen proof checker or original-problem bound was changed by this work.

Separately, the already executed 65536-cell capacity returns show that the
tradeoff between central quadratic loss and the physical odd-profile
transition changes near mean radius 0.00007. This is a discriminator for
a new complete check, not a transfer theorem between two different kernels.
The H99 campaign therefore tests target 0.380627417 with
radius 0.00007, retaining 0.380627416 as a fallback. Both targets still
require their own central checks, exact mean cover, fresh replay and root
review. An isolated numerical radius sweep cannot promote either one.

## The changed kernel after the new Gram row

The same unchanged diagnostic was executed on the new H97 17-row kernel,
SHA-256 ccc9f53815b1a7c56d49caecfa549427748feb8133c5d591f716210df37967fd. Its outward enclosure, rounded further
outward for readability, is

    0.38062742560462 <= fixed-kernel ratio <= 0.38062742560649.

The source-frozen replay passed all five controls and took 92.693
seconds. Subtracting the exact old upper endpoint from the exact new lower
endpoint gives a strictly positive increase of at least 6.72114893478e-09
for these two scalar ratios. The new kernel includes both the added checked
Gram row and subsequent coefficient polishing; this comparison does not
isolate the row's causal contribution.

Reports: runs/hybrid97-newrow-fixed-kernel-efficiency-v1.json,
runs/hybrid97-newrow-fixed-kernel-efficiency-replay.json, and
runs/hybrid97-newrow-fixed-kernel-comparison.json. These are diagnostic
certificates for one scalar per kernel. The upper endpoints are not upper
bounds on mu, on other kernels or on the full method. A new global lower
target still requires its own central/transition/outer cover and complete
fresh replay. All proof implementations remain unchanged.
