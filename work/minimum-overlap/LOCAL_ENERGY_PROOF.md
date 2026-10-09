# A local overlap energy inequality

Status: established analytically in this work, pending independent review;
not a premise of a promoted bound. No novelty claim is made.

Let h,g=1-h on [0,2], zero elsewhere, with 0<=h<=1 and both masses one.
For 0<a<=1 put T_a(t)=max(1-|t|/a,0). Then

    integral p(t) T_a(t) dt >= a^2/6,
    y_0(a) := integral p(t) T_a(t) dt / a >= a/6.

This holds for fractional densities, without a centroid assumption.

Proof. Any density f<=1 of mass L has a generalized increasing quantile
q:[0,L]->R which pushes Lebesgue measure to f(x)dx. Since its cumulative
distribution is 1-Lipschitz, q(v)-q(u)>=v-u for almost every u<v.
For every nonnegative even kernel K nonincreasing on the positive axis,

    integral f(x)f(y) K(y-x) dx dy
        <= integral_[0,L]^2 K(v-u) du dv.

Atoms do not arise in f(x)dx. Gaps in the support only increase quantile
distances. The claim follows by the pushforward formula and monotonicity.

Write S_L for the self-energy of the interval [0,L] under T_a. Symmetry
and h+g=1_[0,2] give S_2=S(h)+S(g)+2E, where
E=integral h(x)g(y)T_a(y-x)dxdy=integral p T_a. Both self-energies
are at most S_1. For L>=a, direct integration gives S_L=La-a^2/3.
Thus E>=(S_2-2S_1)/2=a^2/6. Equality is attained by h=1_[0,1]
and g=1_[1,2]. This also verifies the orientation and factor of two.

The proof extends to 1<a<=2 with the lower bound
E>=a-a^2/6-1+1/(3a), since S_1=1-1/(3a). We initially test a<=1.

In the phase-Gram notation a=2/N and
y_0=1/2-a/12-(a/4)trace X, the same inequality implies trace X<=N-1.
It couples all phases through a common density and is stronger than the
independent-phase odd-grid energy bound. This derivation does not modify
the frozen phase-Gram verifier or certify a new matrix grammar.

Related primary background: Laurent and Seminaroti, The quadratic assignment
problem is easy for Robinsonian matrices with Toeplitz structure,
https://ir.cwi.nl/pub/22768/22768A.pdf (2014), Proposition1 and Theorem4.
Their ordering results suggested examining same-color self-energies. The
quantile argument and its application above are written explicitly so the
continuum return and density hypotheses can be checked directly.

Next discriminator: measure violation on the independently integrated
positive-set profile and optimize a nonnegative multiplier. A numerical
gain must justify a separate analytic-premise compiler, rational source
binding, unchanged legacy checks, full mean cover and fresh replay.
