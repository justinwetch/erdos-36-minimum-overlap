# Independent normalization review

This is a manual review guide. It adds no premise or formal-proof claim.
The original proof notes and executed checkers remain authoritative inputs.

For r=2h-1 extended by zero and R(t)=integral r(x)r(x+t)dx,

    (p(t)+p(-t))/2 = (2-|t|)/4 - R(t)/4  for |t|<=2.

The linear terms in r cancel only after averaging the two orientations.
Thus the Gram construction uses the even part of p; it does not assume
that h or p is symmetric. An even kernel has the same integral against p
and its even part, so this loses no validity for the retained dual kernels.

Let a=2/N and average the translated grid phase uniformly over[-a,0].
The cell mean r_i is normalized by the full cell width a, including the two
partially supported endpoint cells. Their sum is integral r/a=0 at every
phase. Counting the allowed phases for a pair of points gives

    a^2 sum_i X_(i,i+k) = integral R(t) T_a(t-ka)dt,

where T_a(t)=max(0,1-|t|/a). Therefore the overlap hat averages are
y_k=b_k-(a/4)sum_i X_(i,i+k). The base values are b_0=1/2-a/12,
b_N=a/24, and b_k=(2-ka)/4 otherwise. Each y_k lies between0 and||p||_infinity.

For signed weights gamma_k, the even kernel is

    K(t)=gamma_0 T_a(t)/a
       +sum_(k>=1) gamma_k [T_a(t-ka)+T_a(t+ka)]/(2a).

The zero-shift coefficient has twice the positive-half coefficient used
at other knots. This explains the factor2 in the exact positive-half
grid-row compiler. The full integral is integral p K=sum_k gamma_k y_k.

The mean m=integral t p(t)dt equals-integral x r(x)dx. The grid-center alias
has phase mean zero because integral r=0. Its almost-everywhere derivative
is a finite grid sum with absolute value at most2. The sharp periodic
Lipschitz variance estimate then gives c'Xc<=1/12+(m/a)^2. Consequently,
all signed Gram penalties must be combined with the base moment coefficient
before minimizing over m^2 on a central mean interval. The second overlap
moment is exactly2/3+m^2/2; the two moments are not independent design data.

For a periodic hypermetric family, independent Bernoulli variables with
parameters equal to the sampled h values satisfy S(B-S)<=floor(B^2/4).
This remains valid when sample arguments coincide: independence is a
permitted auxiliary construction, not a claimed property of h. Integrating
over a period converts each symmetric cut probability to twice the wrapped
overlap q. The period length2 cancels this factor, leaving the stated
right side floor(B^2/4), rather than twice that number.

Finally, a balanced binary partition on2N cells of width1/N has overlap
peak equal to its largest difference multiplicity divided by N. Independent
rounding of a cell-average density controls every nonzero discrete shift;
the zero-shift binary overlap is identically0. Balancing o(N) cells changes
each multiplicity by o(N). Piecewise affinity and the L1 overlap perturbation
bound complete the return to all shifts and arbitrary measurable densities.
These normalizations therefore concern the original finite limit.
