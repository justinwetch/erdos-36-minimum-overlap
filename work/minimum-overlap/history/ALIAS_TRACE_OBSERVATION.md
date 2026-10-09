# Alias variance versus phase trace: a deferred analytic observation

Status: derivation in this work, pending independent review and exact
fixtures. It is not part of a promoted certificate. No novelty claim.

Use the N+1 phase cells in PHASE_GRAM_PROOF.md, a=2/N, r=2h-1,
X=E_s[r_i(s)r_j(s)], and E_s=integral r(x)epsilon_s(x)dx. Write
u(s)=sum_j r(s+ja), where r is zero outside [0,2]. This is a-periodic.
For any fixed partition phase s and z in [0,a], sum_i r_i(s)=0 gives

    u(s+z)=sum_(i=0)^N [r(s+ia+z)-r_i(s)].

The indexed cells include all of the support. Cauchy-Schwarz with N+1
terms, followed by integration over z, yields

    integral_0^a u(s+z)^2 dz
       <= (N+1) [integral r^2 - a sum_i r_i(s)^2].

The left side is independent of s. Average the right side in s. Since
E_s'=-a*u(s), integral r^2<=2 and the mean of E_s is zero, periodic
Wirtinger gives

    Var(E_s)/a^2 <= (N+1)/(N*pi^2) * (1-trace(X)/N).

The trace is at most N by the same Jensen estimate, so replacing 1/pi^2
by the rational upper bound 1/9 is valid. Together with the exact mean
identity, this gives the proposed coupled necessary condition

    c^T X c + (N+1)/(9*N^2) trace(X)
       <= (m/a)^2 + (N+1)/(9*N).

This is different from estimating alias variance independently by 1/12.
It needs a separately checked grammar if used for a bound; it cannot be
serialized by silently lowering the old mean_error_upper field.

The current shared 43/61/71 numerical matrices have trace/N about
0.6192/0.7202/0.7597. The new rational RHS after subtracting the trace
term is about 0.04826/0.04159/0.04061, whereas their actual mean rows are
0.00640/0.01011/0.01353. All have ample slack. Therefore this condition
does not exclude the selected shared solution. The measured tiny phase
contribution to the total mean penalty is a second reason to defer it.
These floating observations are not exact feasibility certificates.
