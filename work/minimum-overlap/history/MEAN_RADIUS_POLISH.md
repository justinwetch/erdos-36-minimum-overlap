# Optimize the certified interval rather than its center

The existing discovery oracle normalizes the mean-zero numerator to one.
For its nonnegative coefficient vector w, write D(w)=integral Q_w^+,
and the central numerator at |mean|<=delta as

    N_delta(w)=1-delta^2 P(w),
    P(w)=w_0/2 + sum_j w_j eta_j/a_j^2.

Here w_0 is the negated quadratic coefficient and the sum is over the
checked Gram functionals. This is the exact coefficient already used by
the unchanged hybrid checker. The cosine and periodic coefficients do
not enter P. All entries of its coefficient vector p are nonnegative.
Optimizing 1/D at zero mean need not optimize N_delta/D.

For a new nonnegative vector v, put t=1+delta^2 p.v and w=v/t. Then
N_delta(w)=1/t, and D(w)/N_delta(w)=t D(v/t). Conversely every w with
positive N_delta is obtained from v=w/N_delta(w). This is a bijection on
the relevant positive-numerator domain; it neither drops nor adds a
certificate premise. Multiplying the affine kernel Q_{v/t} by t makes
its constant term one and changes each coefficient feature by its
known delta^2 penalty. Its positive-part integral is convex in v.

The chain rule gives

    gradient_v [t D(v/t)] = g + delta^2 p (D-g.w),

where g is the existing oracle gradient at w. At delta=0 the transform
is the original objective. The implementation checks this chain rule on
seven independent quadratic-fixture coordinates before optimization.
The existing oracle's sampled root geometry remains discovery-only;
the transform does not certify root completeness or derivative accuracy.

polish_hybrid_mean_radius.py exports w using the original exporter and
schema. Hence the unchanged Arb and integer checkers can decide the
central claim without understanding this optimizer. A fixed-radius
gain still needs rejoining with the independently verified outer cases,
complete mean coverage, audit and fresh packaged replay for promotion.

The first bounded pilot uses the enriched 46-functional seed and the
currently promoted radius .002913797178, 32 subdivisions, 180 seconds.
It tests a different objective, not a larger search budget for the same
mean-zero objective. A small or absent gain will defer further polishing;
a significant gain warrants an unchanged outward interval check first.
