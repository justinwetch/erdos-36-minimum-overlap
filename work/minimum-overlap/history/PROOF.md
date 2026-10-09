# What a uniform step certificate proves

Let n be even, h=2/n, D a positive integer, and a_0,...,a_{n-1} integers with 0<=a_i<=D and sum a_i=nD/2. Set f=a_i/D on [ih,(i+1)h), and set g=1-f there; extend f AND g by zero off [0,2]. These conditions establish exact box feasibility and integral f=integral g=1.

For s=mh, direct integration gives

    C_f(mh) = 2/(nD^2) sum_{max(0,-m)<=i<min(n,n-m)} a_i(D-a_{i+m}).

For two individual cells, their overlap length under a translation is a triangular piecewise-linear function with knots on h times the integers. Multiplying by their nonnegative constant heights and summing over all ordered cell pairs therefore makes C_f continuous and affine on each [mh,(m+1)h]. It vanishes for |s|>=2. An affine function on a compact interval attains its maximum at an endpoint, so the finite maximum over -(n-1)<=m<=n-1 is EXACTLY sup_s C_f(s). No shift sampling error remains. The exact checker implements all ordered pairs, then recomputes each lag through a separate sliced integer sum. It verifies one function, not global optimality.

## Direct return to the discrete partition problem

This argument establishes the sufficient direction without relying on a numerically stated continuum equivalence. Fix any such f. For each positive integer N let t_i=(i-1/2)/N, i=1,...,2N, and independently put i in a random set A with probability p_i=f(t_i). Let B be its complement. For nonzero integer k, let Z_k count pairs with a-b=k. Then

    E Z_k = sum_i p_i(1-p_{i-k}),

where terms outside 1,...,2N are omitted. The corresponding integrand f(t)g(t-k/N) lies in [0,1] and has at most 2n+2 discontinuities. Every sampling interval containing no discontinuity is integrated exactly by its midpoint. Each exceptional interval contributes at most 1/N quadrature error. Hence, uniformly in k,

    E Z_k <= N sup_s C_f(s) + 2n+2.

Similarly |E |A|-N|<=n+1. The extra constants cover endpoint conventions and coincidences. There are fewer than 4N potentially nonzero shifts. Changing one membership bit changes each Z_k by at most two, so the bounded-differences inequality yields

    P(Z_k - E Z_k >= u) <= exp(-u^2/(4N)).

Changing one bit changes |A| by at most one, so Hoeffding yields

    P(abs(|A|-E|A|) >= u) <= 2 exp(-u^2/N).

Taking u=sqrt(12N log(4N)), the union bound over fewer than 4N shifts and the cardinality event is strictly less than one for every N>=1. Thus a simultaneous outcome exists. Move r=abs(|A|-N)<=n+1+u integers between A and B to balance them. Each move changes every overlap count by at most two, independently of previous moves. The balanced partition therefore satisfies

    max_k Z_k <= N Q + 4n+4 + 3 sqrt(12N log(4N)),

where Q=sup_s C_f(s). The k=0 count is zero for every actual partition. Dividing by N and taking limsup gives limsup M(N)/N<=Q. If mu denotes the known limit, mu<=Q. This proves the needed infinite-quantifier implication for every fixed finite-step certificate; it does not prove existence of the limit or a lower bound.

## Rounding and repair

Search floats are proposals. Round each height to the nearest multiple of 1/D, clip to [0,1], and restore the exact numerator sum by adding or removing mass only inside available headroom. The checker recomputes Q AFTER this operation; it never assumes the score survives. If f and f' are both admissible, the product identity and 0<=f,g<=1 imply

    |C_f(s)-C_f'(s)| <= 2 ||f-f'||_1

uniformly in s. For the uniform n-cell representation this is <=(4/n)sum_i |f_i-f'_i|. This is a conservative independent sanity bound, not a replacement for exact recomputation.

## Weak-bridge audit

- Complement outside support: g is zero there, not the global function 1-f.
- Shift zero: the random expectation factorization is used only for distinct indices; actual zero-shift overlaps are zero.
- Balancing: changes all shifts by at most 2r; expected mass alone is insufficient.
- All N: the step count n is fixed before N tends to infinity; the error tends to zero uniformly in k.
- No claim that local optimization gives a universal lower bound.

Status: the support convention, distinct-index expectation, balancing penalty,
union-bound constants and order of quantifiers were reviewed separately. Arithmetic
certificates have separately recorded executed checks. No formal proof-assistant
verification is claimed.

## Existence of the limit and continuum equivalence

For completeness the two one-sided arguments also yield the known equivalence.
Let c_cont be the infimum of ||C_h||_infinity over all admissible measurable h.
Every finite binary partition gives an admissible step function whose continuum
maximum equals its normalized discrete maximum, as shown above. Hence

    c_cont <= liminf_N M(N)/N.

For any admissible h, average h on uniform cells to obtain f_n. Conditional cell
averages preserve its range [0,1] and total integral exactly, and f_n -> h in L1.
One way to justify the last fact is to approximate h in L1 by a continuous
function, use uniform continuity for that function's cell averages, and use
the L1 contraction of cell averaging for the two approximation errors.
The uniform correlation bound proved above gives

    ||C_f_n - C_h||_infinity <= 2 ||f_n-h||_1 -> 0.

Fix n first and apply the random-partition return; it yields
limsup_N M(N)/N <= ||C_f_n||_infinity. Then let n -> infinity and take the
infimum over h. Thus

    limsup_N M(N)/N <= c_cont <= liminf_N M(N)/N.

The limit therefore exists and equals c_cont. The order of limits matters:
the finite step count is fixed throughout each application of the random
construction. This is an explanatory derivation of the known model equivalence,
not a claim of a new theorem.
