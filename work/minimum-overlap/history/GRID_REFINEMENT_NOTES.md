# Discovery-grid comparison, October 8

These are discovery results, not additional global bounds. The verified
hybrid29 checkpoint remains the public-facing lower bound until another
candidate completes every continuous, mean-cover and fresh-copy check.

The 4096-cell relaxation with 32 checked Gram rows gave a numerical cap
0.38060284399434763. Continuous polishing gave a mean-zero numerical score
0.38060171481693955 in 300.197 seconds. A finer discretization could reduce
this gap, but increasing the cell count also makes the dense Fourier part
of the discovery LP more expensive.

The first 8192-cell trial preserved all 986 Fourier frequencies. It reached
its 120-second LP limit, with primal cap 0.3806324059479103; this is not an
optimality result. Its extracted dual failed the unchanged continuous
checker at the existing target: the computed mean-zero bound was only
0.380306722212640803734006813526283118995318316452392188480.
The exact Gram premises themselves passed. Solver incompletion therefore
cannot be treated as an improved lower bound or an infeasibility result.

The deciding difference is whether a smaller active Fourier menu makes
the finer-grid LP finish usefully. A single bounded comparison reuses the
exact 8192-cell Gram rows, retains the nonzero Fourier terms in the polished
32-row candidate, and executes the unchanged exact row-association extractor
and outward continuous checker. Further grid refinement depends on this
executed result, not on an assumption that finer is always better.

The reduced trial retained283 frequencies and finished its full comparison
in76.824 seconds. The LP status was Unknown, so no optimality is inferred.
Nevertheless, its extracted exact coefficients passed the outward checker,
with mean-zero bound0.3805999869534377565520090476436454833016577903048481871508.
This raw refined candidate is below the polished coarse32 candidate and
below the new35-row candidate in progress. No claim compares fully optimized
fine and coarse optima. Because this executed refined proposal would not
change the next promotion choice, further fine-grid polishing is deferred.

Separately, a bounded three-step cutting-plane campaign fitted each new
Gram separator to the newly updated adversarial profile. Rows 33, 34 and35
used grids31,43,33. Their exact separators passed the existing PSD compiler;
the successive numerical caps were 0.3806031500884998,
0.38060684912499687 and0.3806076835115815. Their gains were approximately
3.061e-7, 3.699e-6 and8.344e-7. The 43-cell step warrants retaining its
triangle menu for the next updated adversary. None of these caps is an
upper bound for the original minimum-overlap constant.

This comparison applies the decision-making skill's dependency check:
test the claimed benefit of refinement against its measured solver cost.
It also applies the hard-problem-reasoning skill's return obligation:
discrete numerical duals must survive continuous integration and full mean
coverage before changing the original-problem bound. The campaign does
not identify a causal effect of either skill.

October8,09:17 UTC: Shared128 scales32,64,128 stopped after its first user_limit solve (124.203s), before adding triangles. The displayed mismatch.0634189934 is not a certified separation. Exact PSD repair and the unchanged functional/profile check returned negative gap -11556881331929692976033420903165127680605001237/153600000000000000000000000000000000000000000000. The dual is valid but does not exclude this profile; no row or global bound was promoted. Preserve runs/shared128-on39-cut.json and certificates/shared128-on39-functional.json as failed-route evidence. A paired frequency cutoff on the polished39 candidate was a no-op: both files have259 Fourier terms, maxfrequency1777.0330078553354. Both Arb4 bounds on radius.002829961964 were identical at.380608319801568183187924918230322423403813079203040990321; there is no performance-treatment inference. Check actual feature counts before future pruning tests.
