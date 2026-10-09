# Coupling the phase mean row to its exact alias covariance

BERNOULLI_PROOF.md shows P_N=integral p(t)B2(t/a)dt=-Var(E_s)/(2a^2),
where a=2/N and E_s is the periodic cell-center error. PHASE_GRAM_PROOF.md
gives a*sum c_i r_i(s)=-m+E_s. Therefore the exact joint identity is

    c^T X c = (m/a)^2 - 2 P_N.

Consider a signed Gram certificate with nonnegative mean-row multiplier eta,
alias-error upper bound E>=1/12, and passed lower value L_delta at |m|<=delta.
Its positive semidefinite matrix is unchanged if the mean term in its
derivation is replaced by this exact equality. The result is

    F_gamma(p) - 2 eta P_N >= L_delta + eta E,  |m|<=delta.

To see the sign directly, remove the mean-row bound from the dual argument:
F_gamma>=L_delta+eta*(E+(delta/a)^2)-eta*c^T X c. Substituting the identity
and using m^2<=delta^2 gives the displayed inequality. This couples the
alias covariance to the overlap rather than estimating it independently.

The new kernel is piecewise quadratic (ordinary triangular hats minus
2eta times a periodic Bernoulli polynomial). It is not supported by the
current continuous verifier grammar. A numerical LP with exact-cell kernel
integrals is a discovery test only. Any global improvement needs a new
fully checked continuous integration bridge or a proved finite Fourier
replacement with its truncation cost paid explicitly.
