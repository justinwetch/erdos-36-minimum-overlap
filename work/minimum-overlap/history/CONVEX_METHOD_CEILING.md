# What an exact profile mixture can establish

This is a proof-method diagnostic. It does not replace the original
minimum-overlap objective or establish a new construction for that problem.

Let H0 be the admissible densities with centroid integral (x-1)h(x) dx=0.
For h in H0, reflection h*(x)=h(2-x) is also in H0 and its overlap is
p_h*(-t)=p_h(t). Thus e_h=(p_h(t)+p_h(-t))/2 is a convex mixture of two
actual admissible overlap profiles. For finitely many densities h_j and
nonnegative rational weights w_j summing to one, put q=sum_j w_j e_hj.
Then q is nonnegative and is a convex mixture of actual overlap profiles
in the zero-centroid subclass. It need not itself be an actual profile.

Suppose a uniform certificate on H0 uses an integrable real kernel K and
proves integral K(t)p_h(t) dt >= L for every h in H0. Put
D=integral max(K,0)>0. Averaging that inequality over all reflected pairs
gives integral Kq >= L. If the exact supremum of q is P, nonnegativity gives

    L <= integral Kq <= P integral K+ = P D.

Consequently its lower-bound value L/D cannot exceed P. Finite combinations
of uniform linear profile inequalities also obey this ceiling. This
includes a central-mean certificate whose hypotheses include mean zero.
It does not cover every possible nonlinear or subdivided proof method.
Even P below the best known actual construction would not prove a gap
between the original optimum and this convex relaxation.

For n equal cells on [0,2], heights a_i/d with exact box and mass bounds,
every p_h is affine between knots 2k/n. This follows by decomposing it into
pairwise overlaps of equal-length intervals; those overlaps are triangular
functions with grid-aligned breakpoints. Reflections and finite mixtures
preserve the common knot set. Thus checking every knot checks every real
shift, including zero outside [-2,2]. The independent checker uses direct
ordered-pair integer sums in both directions rather than the discovery
code's packed convolution or numerical optimizer.

The centroid check is exact: integral (x-1)h(x) dx equals
2 sum_i (2i+1-n)a_i/(n*n*d). Under mass one the overlap mean is minus twice
this quantity, so every component lies in the required mean-zero branch.
Reflection preserves zero centroid. All arithmetic premises are checked
component by component, and rounded mixture weights are normalized by
their actual integer sum.

The first 256-cell, 40-round search passed the separate checker with
60 active components and exact peak
9751920707347736019522321163623427303 /
25600000000051200000000000000000000000, approximately 0.38093440263000905.
It was above the known construction, so that run alone gave no useful new
method limit. Longer and refined searches are separate experiments.

The discovery quadratic and gradient passed 340 small controls before the
first campaign. Local Frank-Wolfe termination and the mixture LP dual are
not global optimization certificates. Only the repaired density witnesses,
positive rational mixture weights, and independent full-shift arithmetic
enter a checked ceiling claim.

The seeded 256-cell continuation completed in 240.8 seconds and passed the
independent checker with 117 active components, giving ceiling
812154714235156708282021768066206559 /
2133333333337600000000000000000000000, approximately 0.3806975222969683.
The fresh 512-cell search gave only 0.38086230911822483, illustrating the
importance of the actual witness pool rather than grid size alone.

An additional 256-cell run sampled existing active witnesses as well as
new linear-oracle vertices for response starts. Its independently checked
119-component mixture gives the stronger exact ceiling

    48724374601394393909559222049310795677 /
    127999999999232000000000000000000000000
      = approximately 0.38065917657567766.

Its mixture SHA is
429cc30adf0f0a6897e833fe2a0bfd216b48364ddb36aee5b18584ac28d36932.
The standard-library checker SHA is
e62f9cfd23fa9f8c6b81b1d3f42de30573888ea684bb0ee05f14778488820eb4.
The exact check passed mass, boxes, zero centroid, positive weights,
all 257 nonnegative knots and reflected negative shifts, with no conflict
with the verified lower bound. A hand-computed mixture of peak 15/32 and
two unchanged-upper-checker comparisons passed; nine corrupted-premise
controls were rejected. Discovery objective controls passed separately.

Refining the earlier 117 active components to 512 cells preserved their
profiles exactly before new response generation. That bounded run reached
only approximately 0.38069752229693493, effectively retaining its seed.
It does not establish a grid-size effect or global convergence. No
individual full-overlap construction from these runs beat the retained
actual upper witness.

Relative to the verified lower 0.380608859, this method ceiling leaves
about 0.000050318 of potential uniform linear-kernel improvement. The
gap to the actual retained construction is about 0.000249715. This is a
reason to investigate a nonlinear or density-dependent case split, not
a proof that the original optimum exceeds the convex relaxation.
