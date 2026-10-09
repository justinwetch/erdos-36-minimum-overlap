# A common-bin blend at the central/outer boundary

Status: derived in this work; numerical discriminator positive. A new
explicit checker is being tested. No stronger global claim is promoted.
Existing trusted checker files are unchanged. No novelty claim.

For one fixed mean bin I, let Qh be an existing hybrid even kernel with
the independently derived inequality integral p Qh >= Lh(I)>0. Let Qo
be an original Fourier outer kernel for the same bin, whose inequality
is integral p Qo >=1. Choose an exact rational ell>0 and verify ell<=Lh(I).
For any rational theta in [0,1], the full-line asymmetric kernel

    Q = (1-theta) Qh/ell + theta Qo

satisfies integral p Q>=1 for every admissible density with mean in I.
Thus outward integration D>=integral max(Q,0) proves ||p||infinity>=1/D.
It may improve on both endpoint kernels because their positive regions
need not agree. All premises concern the same p and the same mean bin;
no unrelated witness gluing or symmetry assumption is used.

The proposed grammar embeds both source certificates, I, theta and ell.
The checker recomputes the phase matrices and Lh(I), every accepted outer
RHS and the signs of all inequality multipliers. A stored source score
does not establish ell<=Lh(I). Its exact rational partition contains the
hybrid knots on [0,2] and their reflected negatives. On a negative piece,
the affine slope changes sign. The outer Fourier kernel is evaluated at
the actual signed argument; it is not reflected or averaged.

Each exact piece is fully covered by rational bisection. The second-order
or fourth-order Taylor remainder bounds apply to the sum of scaled
harmonic terms and affine shifts. Positive pieces use an outward
primitive increment; ambiguous final pieces use width times an outward
positive range bound. Nothing depends on quadrature nodes finding roots.
Controls exercise merged jets at both endpoint weights and an interior
weight, and full-line constant/linear integrals at both Taylor orders.

The numerical pilot used Gauss orders16/32/64 on all rational hybrid
pieces. At I=[.00319,.00321] its approximate blended bound is .3806240252,
versus .3806238773 for the central kernel and .3806206665 for the outer
kernel. At I=[.00327,.00329] the approximate gain is about4.24e-7 over
the better endpoint. These are discovery values, without outward support.
The complete infinite-domain return remains PROOF.md. A new global bound
also needs central coverage below the new transition, both reflected
blend-bin covers, fresh outer coverage above it, an exact coverage audit,
independent integration and fresh-copy replay. One successful bin alone
does not change the promoted interval.

Executed update 2026-10-08T17:02:30.655182+00:00: prototype passed bothArborders and independent
integerintegration. All12positivebins passed bothArborders; fullinteger
cover running. No newglobalpromotion beforecompleteauditandfreshreplay.
