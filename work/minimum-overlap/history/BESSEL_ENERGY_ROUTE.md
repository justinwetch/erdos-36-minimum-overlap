# Finite Fourier energy discriminator

This is a derived necessary inequality and a floating relaxation experiment.
It is not yet part of any promoted certificate or a novelty claim.

Let h:[0,2]->[0,1] have integral one, g=1-h on this support, and
p(t)=integral h(x)g(x+t)dx with both densities zero outside the support.
For positive integer k write H_k=integral h(x)exp(i*pi*k*x)dx.
The support indicator has zero Fourier coefficient at each such k.
Fubini therefore gives

    integral_{-2}^2 p(t) cos(pi*k*t)dt = -|H_k|^2.

No symmetry of h is assumed. Replacing p by its even part leaves this
integral unchanged. If S is any finite set of distinct positive integers,
the functions exp(i*pi*k*x)/sqrt(2), k in {0} union S union (-S),
are orthonormal on [0,2]. Finite orthogonal projection gives

    1/2 + sum_{k in S}|H_k|^2 <= integral h^2 <= integral h = 1.

Thus sum |H_k|^2 <= 1/2, or equivalently

    -sum_{k in S} integral_{-2}^2 p(t)cos(pi*k*t)dt <= 1/2.

One may choose S after observing a proposed profile: validity holds for
every finite S and every admissible h. This does not authorize choosing
S after observing a test input in an algorithm with a different contract.
The selected S is frozen in the experiment's summary.

The 47-row step-profile proposal has nonnegative powers through k=64,
but negative powers occur later. Its positive powers selected through 1024
sum to approximately .96506, violating the necessary .5 energy ceiling.
The signed sum is only .49740, so summing all modes would hide the defect.
Four sets, selected through 128/256/512/1024, are supplied as additional
floating rows to the same 4096-cell LP with all previous premises retained.
The known actual upper density passes each selected energy test. The
Fourier-sign and factor-two identity is checked on 33 actual linear-profile
fixtures, with maximum floating error 5.60e-17.

The selected sums and LP output are diagnostic. A relaxed profile can
escape into other untested negative modes; an LP optimum is not an
original-problem upper bound. An improved numerical dual cannot be sent
through the existing Gram-only extractor as if it used the old grammar.
Promotion would require an explicit new exact analytic premise, rational
nonnegative multipliers, outward enclosures of every integer-pi kernel,
the full mean cover, independent implementations, and fresh-copy replay.
If the cap gain is negligible, retain this discriminator and defer that
grammar work. If it is substantial, first test further mode sets and
refinement to distinguish a useful inequality from a grid artifact.

The separate local common-phase probe passes at 7/15/31/39/47/55 modes.
Its 63-mode cold and warm local fits fail to reach spectral norm <=1.
These failures are not global phase infeasibility proofs. The inexpensive
energy discriminator is preferred because it has a direct universal
proof and does not depend on interpreting a local optimizer failure.
