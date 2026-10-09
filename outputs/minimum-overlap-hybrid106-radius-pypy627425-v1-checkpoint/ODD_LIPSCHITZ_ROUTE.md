# Physical odd-overlap capacity

Let d(t)=p(t)-p(-t) on[0,2]. The identity in ODD_REFLECTION_FOLD.md gives
d(t)=H(t)+H(2-t)-1, so d(2-t)=d(t), d(0)=0, and
d'(t)=h(t)-h(2-t) almost everywhere. Thus d is1-Lipschitz. Its integral
on[0,1] is m/2: symmetry gives integral_0^2 t*d(t)=integral_0^2 d(t)=m.
Also |d|<=M whenever0<=p<=M. These are simultaneous necessary conditions
on the same odd profile; separate pointwise bounds discard that information.

For a fixed kernel, write A and B for its even parts at t and2-t, and
s for the sum of its odd parts there. In each pair p(t),p(-t), a fixed
difference d leaves their sum between |d| and2M-|d|. Maximizing the kernel
integral over those two sums therefore gives

    2M(A_+ + B_+) - (|A|+|B|)|d| + s*d.

Integrating on[0,1] and maximizing over d with the preceding physical
constraints bounds integral Qp from above. Dropping the Lipschitz and
mean constraints recovers the folded positive-part denominator exactly.
If a certified capacity upper bound is smaller than the existing exact
expectation lower bound L(m), the tested peak M is impossible at that mean.
Uniform mean coverage, a strict margin and an exact continuum return would
still be required to deduce a global lower bound.

The initial discriminator samples the coefficient functions at midpoints
and uses a piecewise linear d with exact-grid slope and area constraints
in a floating LP. It compares mean-only and mean-plus-Lipschitz capacities
on the same grid. This can expose a useful missing restriction, but the
finite LP is not itself an upper bound for the continuous capacity. A
positive numerical gap requires independent LP residual checks and a
rigorous bound for the unsampled coefficient and profile behavior.
No continuum bound or unrestricted optimality claim follows from the probe.
