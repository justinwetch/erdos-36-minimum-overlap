# Joint first moments and Gram matrices: an unimplemented route

Status: derived identities and a completed discovery pilot; no continuum
certificate or novelty claim accompanies this note.

Use the phase cells in PHASE_GRAM_PROOF.md, with a=2/N, r=2h-1,
X=E[r_vec r_vec^T], and m_vec=E[r_vec]. Besides X positive semidefinite,
the augmented matrix [[1,m_vec^T],[m_vec,X]] is positive semidefinite:
it is the expectation of [1;r_vec][1;r_vec]^T. Its row sums corresponding
to r_vec are zero. These first moments were not retained by the current
pure quadratic Gram export.

Writing T_a for the triangular hat, averaging the cell origin gives

    m_i = (1/a) integral_0^2 r(x) T_a(x-ia) dx.

For b_i=-b_(N-i), set phi_b(x)=sum b_i T_a(x-ia). It is antisymmetric
about x=1. The exact identity d(t)=p(t)-p(-t)=H(t)+H(2-t)-1 gives
d'(t)=(r(t)-r(2-t))/2 almost everywhere and d(0)=d(2)=0. Therefore

    b.m_vec = -(1/a) integral_0^2 d(t) phi_b'(t) dt.

The odd piecewise constant kernel O_b, equal to -2 phi_b'(t)/a for
positive t and extended oddly, has integral O_b p = 2 b.m_vec.

The existing functional derivation gives integral F p = L+trace(GX)
after the stated linear inequalities. If the augmented block

    [[c, b^T U], [U^T b, U^T G U]]

is positive semidefinite, where U spans 1-perp, then
trace(GX)+2 b.m_vec+c>=0. Consequently

    integral (F+O_b) p >= L-c.

For a checked positive definite U^T G U, the sufficient Schur cost is
c >= (U^T b)^T (U^T G U)^(-1) (U^T b). This is another quadratic
perspective when the multiplier on the original functional is free.
It couples odd observables to the same phase-cell covariance, rather than
checking only separate scalar Fourier inequalities.

The cheapest useful discriminator would keep one checked active Gram
functional fixed, optimize a small antisymmetric b in its well-conditioned
eigenspace against the current conditional kernel, and compare the
quadrature gain with the paid Schur cost. An unsuccessful floating search
would not refute the inequality or prove optimality. A successful search
would still require a new explicit grammar for odd affine pieces,
independent exact block-PSD verification, independent outward integration,
full mean coverage and fresh replay. None of those obligations is currently
discharged, and existing checkers must remain frozen.

The initial pilot avoids an unstable inverse. Reflecting the density
reverses the phase-cell indices and preserves its even overlap and the
mean-square restriction. Averaging an existing functional's proof with
its reflected proof therefore retains F and L and replaces G by
G_s=(G+RGR)/2. For an antisymmetric v, b=G_s v is antisymmetric and
c=v^T G_s v gives a valid augmented block by completing the square on
1-perp. If the functional's existing coefficient is u>0, use b=u G_s v
and c=u v^T G_s v. The discovery code chooses v in well-conditioned
antisymmetric eigendirections and then exports exact rational v, b and c.
Stored b and c would have to be recomputed by a future checker, and the
reflection proof and all existing multiplier signs would remain premises.

The completed pilot used the 64-sine wide29 kernel at quadrature order64.
It checked five floating gradient fixtures, explored the active Gram
functionals separately, and returned an exact rational proposal in 18.55s.
Its initial numerical bound was 0.38062519179108 and its best was
0.38062519244381, a gain about 6.53e-10. The route was deferred because the
128-sine search gave a much larger gain through the existing grammar.
No new continuum checker was implemented. This small gain is neither a
refutation nor a statement of optimality for a joint Gram relaxation.
