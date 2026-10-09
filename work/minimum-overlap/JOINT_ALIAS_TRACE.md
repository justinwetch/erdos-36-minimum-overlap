# Coupling phase alias error to the interior Gram trace

Status: derived analytic necessary inequality, with exact physical fixtures
and numerical discrimination to be recorded separately. This row is not
part of the frozen production certificate grammar and has not promoted a
new bound. No novelty or priority claim is made.

Keep the phase-averaged notation of PHASE_GRAM_PROOF.md: n>=2, a=2/n,
r=2h-1 on [0,2], cell averages r_i(s) for i=0,...,n and s in [-a,0],
X=E_s[r_cell r_cell^T], c_i=i*a and overlap moment m. Put

    T_int = sum_(i=1)^(n-1) X_ii.

The proposed additional necessary inequality is

    c^T X c + (a/19)*T_int <= 2/19 + (m/a)^2.

For a mean window |m|<=delta, replace the last term by (delta/a)^2.
It can be imposed together with the existing 1/12 alias row. A stronger
analytic version replaces 1/19 by 1/(2*pi^2), but the rational version
below has a simple independent justification of its constant.

## Fiber projection and the shared energy budget

For u in [0,a) define F(u)=sum_(j=0)^(n-1) r(u+j*a). Define w on [0,2]
by w(u+j*a)=F(u)/n. Thus w is the a-periodic fiber average, restricted
to [0,2]. Its integral over each full period is zero, since integral r=0.
Let v=r-w. Fiberwise averaging gives the exact orthogonal decomposition

    integral r*w = integral w^2,
    ||v||_2^2 = ||r||_2^2-||w||_2^2 <= 2-||w||_2^2.

For each phase, every interior cell i=1,...,n-1 is entirely inside [0,2]
and has length a. Its integral of w is zero. Hence its average of r equals
its average of v. These interior cells are disjoint; Jensen therefore gives

    a sum_interior r_i(s)^2 <= ||v||_2^2.

Averaging phases proves

    a*T_int <= 2-||w||_2^2.

Endpoint cells are deliberately excluded. Replacing the interior trace by
the full trace without an additional endpoint argument is not justified.

## Alias variance from the same projection

Let E(s)=integral r(x)*(center_of_phase_cell-x) dx. This is absolutely
continuous, a-periodic, and has phase mean zero. For almost every phase,

    E'(s)=-a F(s+a)=-2w(s+a).

Since ||w||_2^2=2*average_phase(w^2),

    average_phase(E'^2)=2||w||_2^2.

The periodic Wirtinger inequality, or Parseval applied to the nonzero
Fourier modes of E, gives

    average_phase(E^2) <= a^2/(4*pi^2)*average_phase(E'^2)
                       = a^2/(2*pi^2)*||w||_2^2.

For completeness pi^2>19/2 follows from the inscribed regular 12-gon:
pi>3*(sqrt(6)-sqrt(2)), whose square is 72-36*sqrt(3)>19/2. The last
comparison follows by squaring sqrt(3)<125/72. Thus 1/(2*pi^2)<1/19.
Combining the two energy bounds yields

    average_phase(E^2)/a^2 <= (2-a*T_int)/19.

Finally a*c.dot(r_cell)=-m+E(s), and average_phase E=0. Squaring and
averaging gives c^T X c=(m/a)^2+average_phase(E^2)/a^2, proving the row.
All functions involved are bounded on finite support; the cell and fiber
identities use Fubini. No differentiability of h is needed. E is Lipschitz
even when h is only measurable, and Wirtinger applies to that periodic H1
function. The decomposition, interior cells and alias error refer to the
same r; independent witnesses would lose this energy budget.

## Why the row may help near the overlap frontier

The existing zero-lag hat inequality and endpoint diagonal bounds imply

    a*trace(X) >= 2-a/3-4M,
    a*T_int >= 2-a-4M.

Therefore any overlap of peak M obeys the corollary

    c^T X c <= (m/a)^2+(a+4M)/19.

At n=127 and M<=.381 this gives an alias constant below 1/12. The explicit
zero-mean alias-sharpness examples have very large overlap and interior
trace zero; they satisfy the new row and do not refute this coupled gain.

The corollary alone is a restriction on a proposed cap class, not a lower
bound on mu. A numerical SDP using the row supplies diagnostic evidence
only. To use its dual in a continuous-kernel certificate, implement a
separately versioned exact row reconstruction and PSD check, prove its
all-mean return, then execute the complete central/transition/outer proof
and a fresh-copy replay. Existing checkers must reject uncompiled duals
containing this row. The current incumbent remains unchanged.

## Standalone signed-functional arithmetic return

The standalone checker can reuse the unchanged exact PSD implementation
without pretending the new premise is in the old production grammar.
Let lambda>=0 be the joint-row multiplier. Form an old-schema surrogate
by increasing its ordinary alias multiplier by lambda and its interior
diagonal multipliers by lambda*a/19. This reconstructs exactly the same
dual matrix as the new joint row. The surrogate's old scalar bound pays
lambda/12 for the added alias row and lambda*a*(n-1)/19 for its added
interior diagonal rows. The actual joint row pays 2*lambda/19 instead.
Both pay the identical lambda*(delta/a)^2 mean-window term. Therefore

    L_joint = L_surrogate + lambda*(1/12-a/19).

The checker enforces that the allocated alias and diagonal multipliers
can be removed nonnegatively, requires the surrogate alias constant to
equal 1/12, reconstructs its rational matrix and checks positive
definiteness on 1-perp by the unchanged integer Bareiss implementation.
Any diagonal PSD repair is still paid in the surrogate. No solver
eigenvalue is trusted. The returned signed hat functional has the same
weights as the surrogate and the improved scalar lower bound above.
Its all-mean numerator retains the full total alias multiplier in the
negative squared-mean term.

This establishes only the signed functional under the general analytic
premise proved above. Its schema is deliberately distinct from the old
production hybrid schema. The continuous-kernel return and a complete
fresh global proof remain separate obligations.
