# Removing a signed Gram certificate's mean restriction

This is an exact algebraic transformation of the certificates in
PHASE_GRAM_PROOF.md. It does not assume that a numerical relaxed profile
is realizable. Write a=2/N, c_i=i*a, and X*1=0. The signed functional is
F_gamma=sum gamma_k*y_k, where y_k=b_k-(a/4)sum_i X_(i,i+k).
Let eta be the coefficient of the conditional mean row in a passed dual.

Define gamma'_k=gamma_k+4*eta*a*k^2 and remove the mean row entirely.
The off-diagonal part of the resulting matrix change is
-eta*(c_i-c_j)^2/2-eta*c_i*c_j=-eta*(c_i^2+c_j^2)/2.
The diagonal change is -eta*c_i^2, the same formula at i=j. Thus

    G_new-G_old=-(eta/2)*(u*1^T+1*u^T), u_i=c_i^2.

This matrix vanishes on 1-perp. Every restricted principal minor is
unchanged exactly, and the original restricted PSD proof applies.
Equivalently c^T X c=-a^2 sum_(k>=1) k^2 sum_i X_(i,i+k), by X*1=0.

If L_old was checked at radius delta with alias error constant E, the
new lower value is

    L_new=L_old+eta*(E+(delta/a)^2+4/(3*a^2)+1/3).

Here 4*a*sum k^2*b_k=4/(3*a^2)+1/3, obtained by summing the stated
polynomial b_k and endpoint term. The transformed certificate has no
mean multiplier and hence proves F_gamma'>=L_new for every allowed mean.
Its header uses mean_abs_max=1 to make this scope explicit. The unchanged
rational compiler and integer PSD checker suffice to replay it.

This is a new functional, with new signed weights, rather than a larger
constant for the old functional. The remaining diagonal, triangle and
circle multipliers are unchanged. Exact equality of restricted matrices
and lower constants is checked by lift_gram_mean.py. Literal-profile gap
comparisons are diagnostics; a global improvement still needs continuous
dual verification and complete mean coverage.
