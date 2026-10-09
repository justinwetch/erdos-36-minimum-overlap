# Discovering phase functionals for a prescribed mean interval

This is a new discovery driver; it changes no trusted checker or theorem
contract. Its proposals are recompiled and independently checked by the
existing return and continuous-verification chain.

For an original admissible density with overlap mean m, the even overlap
has mass one and second moment 2/3+m^2/2. For |m|<=delta its moment lies in
[2/3,2/3+delta^2/2]. The phase identities in PHASE_GRAM_PROOF.md imply

    c^T X c <= 1/12+(delta/a)^2,     a=2/N.

An exactly checked signed phase functional with mean multiplier eta>=0
obeys L(p)>=L0-eta*(delta/a)^2 on this entire interval. If an original
normalized discovery row is -L(p)/s<=rhs0=-L0/s with s>0, its valid
radius-adjusted RHS is

    rhs_delta=rhs0+eta*(delta/a)^2/s.

audit_radius_phase_containment.py first runs the original exact containment
audit. It then rechecks every source certificate's hash, integer PSD,
reported L0 and exact normalized row identity, and derives each adjusted
RHS rationally. The explicit cones use the same adjusted mean bound.
Removed rows remain implied at the radius. All nonnegative hat and box
premises remain present. Twelve rational fixture controls check the lower
identity, monotone relaxation and identity at radius zero.

joint_phase_radius.py is an explicitly recorded discovery fork of
joint_phase_reconditioned.py. It uses the adjusted RHS list, the adjusted
phase mean bounds, and a single second-moment equality with an auxiliary
variable z in [0,1]: moment=2/3+(delta^2/2)z. Thus it contains the entire
central interval rather than assuming the mean is an endpoint or zero.
It retains the same spectral constraints, four periodic scales, exact
PSD basis, independent hat equations and adaptive triangles. Its solver
output remains numerical and is not a bound or overlap construction.

The phase dual coefficients can still be exported at mean zero: the PSD
matrix depends on their multipliers, not the scalar RHS of the mean
constraint. The unchanged exact compiler independently reconstructs that
matrix and its mean-zero L0. The existing hybrid compiler then derives
the full mean-square penalty for every radius. This prevents a numerical
radius-specific objective from being mistaken for a certified global
bound. Every proposed improvement still needs the full continuous checks,
mean cover, independent integration and fresh-copy replay.

The deciding test is whether these radius-aware shared proposals improve
the checked fixed-radius certificate after merging its useful active
coordinates with the promoted candidate. A better mean-zero LP cap alone
does not satisfy that criterion.

The selected 43/61/71 pilot returned three independently checked rows,
increasing the retained portfolio from 73 to 76. Their complete mean-zero
fine LP has numerical cap 0.3806282581021. The merged fixed-radius kernel
passed the unchanged full global checks at 0.380623750. All eight fresh-copy
commands then passed in 599.22 seconds, with 37 manifest files unchanged.
This is a promoted global lower bound; the numerical LP cap is not.

Alternate37/59/89return produced79exactrows and promotedglobaltarget
.380623753 afterall8freshchecks (616.456s). Later83/97return produced82
rows, finecap .3806285688272917. Itsfixedradiuspolishgain3.08e-8 remains
numerical; those82rows are notall embedded in the promoted13functionals.
