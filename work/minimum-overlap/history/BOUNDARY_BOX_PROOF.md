# Sharper phase-Gram endpoint box inequalities

These are universal analytic constraints, separate from the currently frozen
certificate. The discovery probe exports no dual certificate or new bound.

Use the notation of PHASE_GRAM_PROOF.md: a=2/N, phase s uniform on[-a,0],
r_i the width-a cell averages of r, and X_ij=E r_i*r_j. Put u=-s/a.
Support and |r|<=1 imply

    |r_0|<=1-u, |r_N|<=u, |r_i|<=1 for1<=i<N.

Consequently |X_0N|<=integral_0^1 u(1-u)du=1/6, and
|X_0i|,|X_iN|<=1/2 for every interior i. The diagonal bounds1/3 used in
the previous certificates are the corresponding second moments.

There is also a stronger triangle constraint. If signs(s,t,v) have product
-1, then for any interior i,

    s*X_0i+t*X_iN+v*X_0N <= 5/6.

Sign changes of the three variables reduce every allowed sign pattern to
(1,1,-1). A multilinear expression reaches its maximum on a rectangular
box at a vertex. At a vertex write r_0=(1-u)*e_0, r_N=u*e_N and r_i=e_i,
with each e equal to±1. If e_0=e_N, optimizing e_i gives1-u(1-u).
If e_0=-e_N, it gives |1-2u|+u(1-u). The former is larger: their
difference is2u^2 foru<=1/2 and2(1-u)^2 foru>=1/2. Thus the pointwise
upper bound is1-u(1-u); its phase integral is5/6.

All inequalities survive arbitrary measurable admissible densities. They
use no approximation, mean restriction, phase independence or assumed step
representation of r. They may still be redundant for a particular optimized
overlap profile. A paired numerical fit tests that practical question before
extending the exact dual compiler and its global continuous replays.
