# Retaining useful coordinates at a nonzero mean radius

This is a discovery reformulation. Every proposed certificate still uses
the unchanged exact compiler, continuous integration and global checks.

In the normalized continuous oracle write

    Q_w(x)=1+sum_i w_i A_i(x),     D(w)=integral max(Q_w,0),
    w_i>=0,                      L_delta(w)=1-delta^2 p.w.

Here p_0=1/2 for the nonpositive quadratic coefficient. For a signed phase
functional its entry is minus the exact mean-square coefficient; Fourier
and periodic coordinates have entry zero. All current entries are
nonnegative. Only L_delta>0 can yield a useful bound.

Put v=w/L_delta(w), t=1+delta^2 p.v. Then w=v/t and L_delta(w)=1/t.
Maximizing the fixed-radius certificate bound is equivalent to minimizing

    F(v)=t D(v/t)
        =integral max(1+sum_i v_i(A_i(x)+delta^2 p_i),0).

This is a convex objective on v>=0. This algebra does not certify the
floating root oracle, a solver optimum, or completeness of its root list.
The numerical derivative used is

    grad F = g + delta^2 p (D-g.w),       g=grad D(w).

The existing root feature model is treated as a PSD surrogate. If Phi
is its feature operator, a transformed feature operator is

    Phi_delta d = [Phi d-(Phi w) delta^2(p.d)]/sqrt(t).

The implementation checks its adjoint, products, diagonal and quadratic
gradient against explicit small matrices, along with independent
finite-difference controls for the perspective derivative. Actual
numerical objective decrease is required at every accepted trial.
None of these controls is called Hessian certification.

## The observed menu loss

The promoted 62-row candidate has numerical mean-zero bound
0.380626572830783 and mean-square penalty about 0.7198721272. The next
89-grid proposal, after polishing, improved the mean-zero bound to
0.380626667512339 but increased the penalty to about 0.8087953776.
At the promoted radius 0.003274688233 the latter has bound only
0.380623366267072, below the promoted candidate's 0.380623634542647.
Its global preparation therefore failed the improvement floor.

The newer exported proposal omitted four of the five functionals used by
the promoted candidate and 23 of its Fourier coordinates. An optimization
restricted to its active mean-zero menu cannot necessarily recover the
better fixed-radius candidate. This is a search-space loss, not an invalid
certificate or a trusted-checker failure.

merge_hybrid_active_menus.py starts from the promoted candidate, adds
missing Fourier and phase coordinates at zero weight, and activates only
periodic coordinates that were nonzero in another actual proposal. These
receive a tiny negative rational multiplier; their exact RHS cost is
added to y0, preserving the numerator. Exact fixture controls check
numerator preservation, input immutability and idempotent union.

The first union has 235 cosines, eight phase functionals and nine periodic
families, with only 74 extra active periodic coordinates. This keeps the
promoted candidate available while allowing the newer coordinates to
help at the required mean radius. Its 32/64 subdivision comparison agrees
to 3.6e-14 in the gradient. Radius-aware optimization improved the numerical
fixed-radius bound by about 8.39e-8. The unchanged central, outer and exact
coverage checks passed at target 0.380623711 and radius 0.003276909315.
All eight fresh-copy commands subsequently passed in 557.18 seconds;
37 packaged files retained their manifest hashes. This target is promoted.

A later 76-row union improved the numerical fixed-radius objective again.
Its exported kernel has narrow sign intervals: a 32/64 mesh comparison
agrees in the objective to 2.3e-13 but disagrees in the gradient by 7.75e-5.
That derivative instability is an explicit unresolved discovery issue.
It does not invalidate a separately passed exact certificate, but further
optimization must address the hidden intervals before trusting derivatives.

The follow-up extrema_hybrid_oracle.py inserts every detected stationary
point into the sign-root partition. It finds 411 roots on each of the
16/32/64 meshes, repairing the two missed roots in the original 32 mesh.
Gradients then agree to 2.70e-12 and 1.72e-13 across refinements. Four
independent narrow positive/negative quadratic-island fixtures pass.
Finite-difference probes still become ill-conditioned near almost tangent
roots; these are diagnostic outputs, not passing gradient certificates.

The explicit extrema polisher fork gained only 5.81e-10 in 182.34 seconds
at the current radius. This does not justify another global replay. The
previous exported 76-row candidate has separately passed the unchanged
global checks and all eight fresh-copy commands at 0.380623750. The
stationary-point oracle is a discovery tool, with no root-completeness
or Hessian-certification claim.
