# Directed subadditivity and integer dilation

This is a separately derived extension of SUBADDITIVITY_RETURN.md, prompted
by the public Drynshock subadditivity claim. No novelty claim is made.
The original dyadic premise and its hash remain unchanged.

For 0<=a,b,c<=1,

    a(1-c) <= a(1-b) + b(1-c).

The right minus left is b(1-a-c)+ac. It is affine in b, so its minimum
over [0,1] is min(ac,(1-a)(1-c))>=0. For s,t>=0, s+t<=2, substitute
h(x),h(x+s),h(x+s+t), and integrate x in [0,2-s-t]. The two resulting
right integrals extend to the domains of p(s),p(t) by adding nonnegative
integrands. Therefore p(s+t)<=p(s)+p(t). Reversing the direction gives
p(-s-t)<=p(-s)+p(-t). This holds for every measurable h, with the same
interval complement and zero extensions as the campaign contract.

Let F(t)=p(t)+p(-t) and d(t)=p(t)-p(-t). Keeping both directed inequalities
gives the stronger common-profile restriction

    F(s)+F(t)-F(s+t) >= |d(s)+d(t)-d(s+t)|.

In particular 2F(t)-F(2t)>=|2d(t)-d(2t)| for 0<=t<=1. This couples an
even-profile restriction with the same physical odd profile used in the
capacity argument. Merely adding an even dyadic row loses this coupling.
As a normalization check, integration gives
integral_0^1 F >= (1+|m|)/4, using integral_0^2 F=1,
d(2-t)=d(t), and 2 integral_0^1 d=m. This weak scalar consequence is
not competitive by itself and is not used in a production bound.

Iteration gives p(kt)<=k*p(t), and hence F(kt)<=k*F(t), for any integer
k>=2 and 0<=t<=2/k. For nonnegative w supported on [0,2/k],

    integral_0^(2/k) w(t)[k F(t)-F(kt)]dt >= 0.

Changing variables gives an even kernel K with K(u)=k*w(u)-w(u/k)/k
for 0<=u<=2, and integral K*p>=0. There is no scalar or mean penalty.

For cell width a=2/N and w the unit triangular hat centered at j*a,
require j>=1 and k*(j+1)<=N. Its exact campaign-normalized hat vector is

    gamma_j += 2*a*k,
    gamma_(k*j+r) -= (2*a/k)*(1-|r|/k),  -k<r<k.

Indeed the wide hat w(u/k) is exactly the sum of fine hats at k*j+r
with weights 1-|r|/k. Nonnegative combinations preserve the inequality
for all admissible means. The standalone integer-subadditive-functional-v1
schema checks these identities and this premise hash. It is not accepted
by the unchanged production grammar and does not itself give a peak bound.

Source context: https://erdosproblems.ai/problems/36 and its captured
Drynshock claim in plasma-ai/erdos at b83915c0e6e4ce25ddd97e87fa75e8a521f6ea71.
