# Returning a fixed central kernel to a smaller mean window

Let the unchanged kernel have the universal numerator lower bound
L0+c*m^2 and a positive-part integral at most D>0. These properties are
established by the existing kernel, Gram and integral checkers. The
denominator D depends on the kernel, not on the requested mean radius.
For every |m|<=delta the peak is therefore at least

    [L0 + min(0,c)*delta^2] / D.

Suppose a checker was executed at radius delta0>=delta. Its denominator
enclosure can be used at delta. This is a new deduction from its actual
arithmetic output, not a change to that execution's target or radius.

For the Arb reports use the lower endpoint of `mean0_numerator_ball` and
the upper endpoint of `positive_integral_upper_ball`. For the independent
integer report use its exact upper denominator and recover L0_lower as

    numerator_interval[0] - min(0,c)*delta0^2.

The integer checker constructs that numerator by adding precisely this
constant to the same fixed-kernel mean-zero numerator interval. Subtracting
it therefore gives a valid lower bound on L0. Functional PSD repairs,
weights and gamma coefficients are unchanged: `hybrid_functionals.validate`
compiles each embedded certificate at mean zero, then records its exact
all-mean quadratic coefficient. No new density or realizability premise
is introduced by narrowing the mean window.

The versioned `retarget_central_mean_radius.py` implements only this
rational deduction. It rejects an enlarged radius, checks positive
denominators and exact integer numerator/denominator consistency, and
includes literal positive, zero and negative coefficient fixtures.
`audit_radius_retargeted_capacity_v1.py` retains the previous audit's
input, dependency, functional-premise, outer and capacity checks. It
explicitly distinguishes the executed central radius/target from the
newly returned radius/target, and requires every derived central bound
to exceed the new target strictly. It then checks the complete [-1,1]
mean cover using the returned interval and the dense capacity intervals.

The source execution reports are retained with their actual parameters.
They are never edited to say that the old checker ran at a different
radius or target. The new replay executes all three unchanged central
integral checkers again at their declared original radius and target,
then repeats the separate rational deduction. Both outer implementations
run at the new global target. Energy, capacity, exact coverage and
malformed-input controls are executed in the fresh copy as well.

The new files version the deduction and orchestration. All previously
frozen arithmetic, kernel, Gram, mapping, energy, capacity and outer
implementations remain byte-identical. A new global claim still requires
the actual original audit, controls and complete fresh replay to pass.
