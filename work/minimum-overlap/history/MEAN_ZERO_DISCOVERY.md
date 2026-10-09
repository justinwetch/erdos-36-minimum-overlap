# Tightening the conditional discovery model

For a checked signed phase-Gram functional,

    F_j(p) >= L_j(0) - eta_j (m/a_j)^2,

where eta_j>=0 and m is the overlap mean. Historical discovery rows used
the conservative right side at a positive mean radius delta, although the
discovery LP fixes the second moment to2/3 and thereby models mean zero.
The weaker right sides are valid, but discard information available inside
that conditional model.

The correction copies each certificate with mean_abs_max=0. Its exact
restricted Gram matrix is unchanged, and its exact functional lower bound
can only increase. Every copy is independently replayed by the existing
integer PSD checker. The normalized kernel coefficients remain identical;
only the normalized right side changes from-L_j(delta)/scale to-L_j(0)/scale.
The unchanged seed extractor recomputes every rational grid integral and
checks its association with the corresponding certificate before export.

zero_mean_discovery.py implements this bounded comparison on the39-row
model. The old certificates and frozen publications remain unchanged.
Mean-zero necessity alone supplies no global minimum-overlap bound. Any
resulting continuous candidate still requires its signed mean dependence,
outer cases, exact full coverage, independent integration and fresh-copy
replay before publication as a global result. Solver status and numerical
cap are discovery evidence rather than proof premises.

The executed39-row comparison passed all39 copied PSD checks and every exact grid-row association. Its bounded LP reached the time limit with numerical cap0.38061097489075574; this is not an optimum. The extracted847-frequency proposal passed the unchanged fourth-order mean-zero checker at0.380608468452630849937011116613806623010282421200105270478. Total comparison time171.418s. The conditional model is now used for subsequent new-grid discovery; its raw candidate does not replace the stronger polished38 candidate or any global checkpoint.
