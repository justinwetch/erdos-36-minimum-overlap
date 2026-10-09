# Return the exact mixture autocorrelation to one density

The common-phase necessary tests found numerical fits at integer orders
32/64 and support-aware order12. They gave no exclusion. The next test
changes the return map: use the full aperiodic autocorrelation of the
actual mixture, rather than clipped periodic power from a relaxed profile.

For a uniform n-cell density write r_i=2h_i-1. A convex mixture supplies
C_k=sum_j w_j sum_i r_(j,i) r_(j,i+k) for every lag0..n-1. Its zero-padded
length-2n Fourier power is the average of actual squared magnitudes, so it
is nonnegative without clipping. A real factor with support n and the
same power would reproduce the full even mixture overlap. The missing
obligations are box |r_i|<=1, exact mass, and the actual directed overlap.
The even profile alone does not control the latter.

Use bounded alternating projections between the target zero-padded Fourier
magnitudes and real support/box/mass constraints. This is heuristic phase
retrieval; convergence or a unique factor is not assumed. Measure support
leakage and magnitude error after projection. Preserve every selected
actual repaired density, and rank by its full directed overlap. Any
improved upper claim must pass the unchanged exact all-shift checker and
fresh portable replay. A factorization failure is not nonrealizability.

The earlier round_phase_spectrum.py used a clipped cyclic spectrum derived
from a nonrealizable relaxed profile. This test has different input and
preserves all aperiodic lags, addressing those two failures. First verify
FFT/direct correlation normalization on small fixtures, and compare the
mixture target against independently computed density overlaps. If box
repair destroys its low profile or all exact directed scores are worse
than the incumbent, record that as a failed construction bridge rather
than a bound on the original optimum.

Executed: 32 starts and 1,000 alternating projections per start completed
in 3.49 seconds on the exact119-component mixture. Fifty-eight small
normalization checks passed, and the actual target's direct overlap/FFT
mapping error was 4.45e-16. The best selected actual density had exact full
peak 10314998695114574349338674856293 /
25600000000000000000000000000000, approximately 0.4029296365279131.
All four selected densities passed the unchanged exact all-shift checker.
The construction bridge failed: repairing support and boxes did not
preserve the low profile, and no improved upper construction resulted.
Further repetition of this heuristic is deferred. This is not a proof
that the target autocorrelation has no admissible factor.
