# Cut the profile selected by the continuous dual

Status: discovery discriminator executed; no new bound or original
construction follows from the virtual profile. The46 candidate passed its
full audit and all8 fresh packaged commands in507.251s. The promoted lower
is0.380609298; the original problem remains unresolved.

The first frozen46 positive-set reconstruction found364 roots on4546
pieces. Independent primitive integration agrees with the Oracle to
1.03e-14, and Euler's identity agrees to2.48e-11. Nevertheless its
complementarity sum is0.0009035346, its cap is0.3807416656, and its second
moment misses2/3 by-0.0013710873. Cell averaging accounts for only3.73e-7
of that discrepancy. The profile therefore fails the intended
near-stationary/near-feasible prerequisite. No phase separator is being
automatically promoted from it. A curvature-scaled optimization test is
running to reduce this error, and LOCAL_ENERGY_PROOF.md supplies a
different independently derived necessary condition to test directly.

Follow-up discriminator: curvature scaling and a constrained root-Newton
model raised the numerical objective to0.38061077660866527. The8-subdivision
Oracle reported complementarity2.1068e-5 and moment error-1.28335e-5.
However independent32-subdivision sign reconstruction found375 roots
instead of373 and an Euler residual-0.0001210075, despite agreement in D
to1.98e-13. Its second moment error is+6.66393e-5. Thin components have
negligible integral Q but consequential volume and gradient. Thus
objective agreement alone fails the gradient/geometry prerequisite.
No separator will be fitted to this profile until that discrepancy is
resolved. check_continuous_discovery_geometry.py compares8,16,32,64 meshes;
finite stabilization remains discovery evidence, not root completeness.
The16/32/64 gradients agree to1.66e-12 in the maximum norm. A32-subdivision
Newton rerun made only a further2.2e-14 objective change before stalling.
The unchanged Arb4 checker establishes its mean-zero lower estimate
0.3806107766086188521, which remains conditional on zero mean.
Testing all retained constraints exposed a much larger omitted-periodic
active-set defect; see ACTIVE_PERIODIC_SET.md for the new discriminator.

The LP discovery profile lives on4096 fixed cells. Its arbitrary interior
solution need not be the profile that obstructs the polished continuous
dual, especially when the latter has hundreds of roots. The shared-profile
SDP was sensitive to coarse discretization and produced no useful cuts.
Use the continuous dual's own positive set as the next target instead.

In the normalized mean-zero Oracle, Q_v(t)=1+sum_j v_j f_j(t), with v_j>=0,
and D(v)=integral max(Q_v,0). The certified ratio is1/D when the numerator
normalization is one. Let V(v) be the measure of {Q_v>0}. For zero sets of
measure zero, differentiation and Euler's identity give

    D(v) = V(v) + sum_j v_j * partial_j D(v).

At a stationary constrained optimum, complementary slackness makes the
sum vanish. Thus the virtual profile p*(t)=1_{Q_v>0}/V(v) has mass one and
cap1/V, close to the current continuous objective1/D. Its mean is zero
by evenness, but it is not asserted to be any actual overlap profile.
The mass, second moment and retained functional residuals must be measured
before using it as a discovery target; numerical stationarity is not a
proof of their exact values.

There is a precise improvement bridge. Suppose an independently certified
new signed functional integral Kp>=L is violated by p*. Adding a nonnegative
coefficient mu for its normalized feature K-L changes the positive integral
with directional derivative

    dD/dmu at0 = integral_{Q_v>0}(K-L)
                = V(v) * (integral Kp* - L) < 0.

Consequently this exact strict separation forces a mean-zero continuous
dual improvement for a sufficiently small positive coefficient. The new
kernel and its numerator must use the same positive-half/full-axis
normalization as hybrid_functionals.py. Any finite numerical proposal
still goes through the unchanged outward checker. The full global bound
also needs the mean-square penalty and an outer-case join; a mean-zero
improvement alone cannot be promoted.

Q is analytic on each of finitely many kernel pieces. If at least one
distinct nonzero cosine coefficient survives, it cannot equal an affine
polynomial on an interval, so it is not identically zero on any piece;
its real zero set on those compact pieces has measure zero. This supplies
the differentiation premise. Cases with an identically zero piece need
an appropriate directional derivative rather than this formula.

Implementation prerequisite: freeze the selected polished dual, find its
sign changes on the exact rational kernel pieces with a fine discovery
mesh, and compute positive-length intersections with fine profile cells.
Compare positive integrals against the existing Oracle/Arb result and
check the Euler residual. Root finding is discovery only. Missed thin
components and cell-averaging moment errors must be measured; neither a
sampled sign map nor finite stabilization certifies all roots.

Fit a bounded phase Gram to this virtual profile. Certify a resulting
functional using the existing rational compiler. Compare it both against
the virtual profile and against the old LP profile. A cut useful only on
the virtual profile should not be automatically discarded: its negative
continuous directional derivative is the relevant test. It can be embedded
with a tiny positive multiplier in the frozen dual and polished directly,
without requiring the fixed-grid LP to choose it first. Keep the old dual
as a known-good snapshot, and independently check every claimed gain.
