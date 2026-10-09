# Phase-sensitive five-variable box inequality

Status: analytic necessary inequality and proposed discovery test. No new
original-problem bound or change to a trusted certificate compiler follows.

For the common-phase cell averages in PHASE_GRAM_PROOF.md, write u=-s/a.
Then |r_0|<=1-u, |r_N|<=u, and every interior |r_i|<=1. Choose three
distinct interior indices i,j,k and arbitrary signs b_l in {-1,1} on
positions {0,i,j,k,N}. The following stronger five-variable inequality holds:

    -sum_(l<m) b_l b_m X_lm <= 11/6.

The polynomial in the five cell values is multilinear. Its maximum on the
phase-dependent rectangular box occurs at a vertex. At any such vertex,
the sum of the five squared values is 3+(1-u)^2+u^2. Consequently

    -sum_(l<m) b_l b_m r_l r_m
      = (3+(1-u)^2+u^2 - (sum_l b_l r_l)^2)/2
      <= 2-u+u^2.

Equality is attainable in that box: choose the signed interior values to
sum to 1 and the signed endpoint values both negative, summing to -1.
Integrating the bound over uniform u in [0,1] gives 11/6. This uses the
actual common phase, not independent endpoint distributions. It is a
necessary inequality for every admissible measurable density, regardless
of its mean. It does not assert that every box vertex trajectory can be
realized by one density.

More generally, the same argument with both endpoints and 2m-1 interior
indices gives m-1/6 for the odd clique of size 2m+1. The three-variable
case recovers the previously derived endpoint triangle bound 5/6; the
five-variable case improves its ordinary box bound 2 by 1/6.

The deciding experiment retains all ordinary triangles, nonnegativity and
the earlier endpoint box constraints in both runs. It scans only the
five-variable facets containing both endpoints, then adds the strongest
violated ones to the second SDP fit of the same literal profile. A useful
fitted gain would motivate an independently checked exact grammar; a tiny
or absent gain would defer that work. Solver values remain discovery.

Executed result: the 33-cell fit of the 45-row literal profile retained
324 ordinary triangle rows and all earlier endpoint box constraints.
All 3,333 exact vertex/sharpness controls passed. Scanning 79,360 endpoint
five-variable facets found zero violations; the largest signed violation
was approximately -0.0175605. No additional facet entered the second run,
so both displayed mismatches were exactly the same, approximately
0.000243378834. Both numerical statuses were optimal_inaccurate. This
specific prerequisite failed; the new exact compiler is deferred. The
analytic inequality remains valid but is not a premise of a promoted bound.
