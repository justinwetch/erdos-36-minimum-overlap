# Paired factor-retrieval discriminator

The exact convex-profile mixture is a ceiling for one linear certificate
method. It is not an admissible density. Recovering a common density whose
aperiodic power agrees with that mixture would supply a bridge to an actual
upper witness. Local failure does not prove that bridge impossible.

The difference-map formula was checked against Veit Elser's original paper,
equation 16: https://arxiv.org/pdf/math/0111080 . The comparison method is
alternating object/Fourier projection, discussed in Fienup's original work:
https://doi.org/10.1364/AO.21.002758 . These sources specify general methods;
the constraint sets and measurements below are this campaign's adaptation.

A projects onto real vectors supported on the first n of 2n coordinates,
with entries in [-1,1] and zero sum. B projects onto the prescribed Fourier
modulus. For beta=0.9 the implemented map uses

    a=A((1+1/beta)B(x)-x/beta),
    b=B((1-1/beta)A(x)+x/beta),
    x <- x+beta(a-b).

The feasible object a supplies h=(a+1)/2 on its support. All proposed upper
witnesses are then rounded and checked in exact arithmetic. Controls cover
58 power identities, affine intersections and disjoint affine sets, three
actual-factor fixed points, projection idempotence and support/box/mass.
All passed; no global convergence theorem is asserted.

The selected 256-cell, 119-component mixture was tested on 16 paired starts,
1000 iterations per method. Difference iterations use twice as many of
each projection, so this is not an equal-cost efficacy comparison. All
32 runs finished in 3.39 seconds. Best exact feasible peaks were about
0.3980376115904513 for alternating projection and 0.39892788201123985 for
the difference map. Minimum relative modulus discrepancies were about
0.08456 and 0.12444. Neither recovered the desired factor.

Direct optimization of the actual overlap objective from both selected
basins returned exact valid upper witnesses about 0.381993670406204 and
0.38184150746747997. Both exceed the retained 0.3808585738366948659232792
upper bound. This selected route is deferred; the observations establish
neither nonrealizability of the mixture nor optimality of the incumbent.

Evidence: runs/mixture256-difference-discriminator/summary.json and its
four exact seed verifications; runs/upper256-retrieved-alternating and
runs/upper256-retrieved-difference. The source snapshot is saved beside
each experiment. No causal claim about the reasoning skill is made.
