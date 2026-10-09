# A dyadic signed-functional return from overlap subadditivity

The subadditivity idea is recorded in the September Drynshock claim linked
from [the user-supplied page](https://erdosproblems.ai/problems/36) and its
[captured claim card](https://github.com/plasma-ai/erdos/blob/b83915c0e6e4ce25ddd97e87fa75e8a521f6ea71/wiki/problems/additive_combinatorics/E0036/claims/2026_09_19_drynshock.md).
No novelty claim is made here. The argument below independently derives
the necessary inequality and a typed finite family for this campaign.
It does not verify that competing claim's full certificate or optimality.

For a,b in [0,1], put d(a,b)=a+b-2ab>=0. For a,b,c in [0,1],

    d(a,b)+d(b,c)-d(a,c)=2[b(1-a-c)+ac]>=0.

If a+c<=1, its minimum over b is 2ac; otherwise its minimum is
2(1-a)(1-c). Thus the triangle inequality holds for probabilities as
well as binary colors, although d(a,a) need not be zero.

For 0<=t<=2, the physical overlap obeys

    F(t)=p(t)+p(-t)=integral_0^(2-t) d(h(x),h(x+t)) dx.

Apply the triangle inequality to h(x),h(x+s),h(x+s+t) on
[0,2-s-t], where s,t>=0 and s+t<=2. Its first right-hand integral
is bounded by F(s); after changing variable x+s, its second is bounded
by F(t). The omitted portions have nonnegative integrands. Therefore

    F(s+t)<=F(s)+F(t).

All integrands are bounded and measurable. The statement does not require
smoothness, a step-density approximation or a common randomization at
different points. In particular, F(2t)<=2F(t) for 0<=t<=1.

Let w>=0 be supported in [0,1]. Multiplication and integration gives

    integral_0^1 w(t)[2F(t)-F(2t)] dt >=0.

Changing variable u=2t yields a necessary signed-functional inequality
integral K(u)p(u)du>=0, where K is even and on [0,2]

    K(u)=2w(u) - (1/2)w(u/2).

Choose a=2/n and a triangular hat w(t)=max(1-|t-ja|/a,0), with
1<=j and (j+1)a<=1. On the fine n-cell hat basis, the wider hat
w(u/2) equals hat_(2j)+(hat_(2j-1)+hat_(2j+1))/2.
In the campaign's normalized gamma convention this gives the exact
weights

    gamma_j +=4a, gamma_(2j) -=a,
    gamma_(2j-1) -=a/2, gamma_(2j+1) -=a/2.

Nonnegative linear combinations retain lower bound zero for every mean.
`verify_dyadic_subadditivity.py` checks that typed construction and the
affine-kernel identity, with literal algebra and physical overlap fixtures.
This separate schema supplies only a signed functional. Combining it
with a kernel requires its own continuous return, actual arithmetic
checks, complete all-mean cover and full fresh replay before promotion.
