# A precise obstruction to using dyadic rows alone

This separates two families of necessary conditions. It is not an
admissible density or a feasible point of the full Fourier/Gram relaxation.
No novelty claim is made.

Define a continuous trapezoid B on [1,2]: it increases linearly from zero
to one on [1,101/100], equals one on [101/100,199/100], and decreases
linearly to zero on [199/100,2]. Its integral is 99/100.
For t>0 in [0,2], choose n>=0 with 1<=2^n*t<=2 and set

    F(t)=(25/33)*2^(-n)*B(2^n*t),  F(0)=0.

Both choices at a dyadic junction give zero. Hence F is continuous,
nonnegative, zero at 0 and 2, and satisfies F(2t)=2F(t) on [0,1].
It is Lipschitz: each smooth piece has derivative magnitude at most
2500/33, uniformly in n. Continuity at zero also follows from F(t)<=25t/33.

The exact geometric sum gives

    integral_0^2 F=(25/33)*(99/100)*sum_(n>=0)4^(-n)=1.

Define the even virtual overlap p(t)=F(|t|)/2 on [-2,2], zero elsewhere.
It is continuous and nonnegative, has total mass one and mean zero, and
has exact peak 25/66. Every pointwise dyadic inequality holds with equality,
so every nonnegative weighted dyadic return holds. However

    p(3/2)=25/66 > 3*p(1/2)=0.

Thus the valid tripling condition is not a consequence of the complete
dyadic family plus these support, continuity, nonnegativity, mass and mean
conditions. The example has peak below the established minimum-overlap
lower bounds precisely because it is not a realizable overlap. Other
production premises may already exclude it; no independence from the full
Fourier/Gram system is claimed.

For comparison, the selected k=4 row is exactly redundant. If w is a fine
hat centered at j*a, its kernel equals twice the dyadic kernel for that
hat, plus one-half the dyadic kernel for the hat at 2j, plus one-quarter
each for the hats at 2j-1 and 2j+1. The wide-hat identity proves this
coefficientwise. Therefore the larger raw k=4 violation is not evidence
that it strengthens the full dyadic menu. Odd dilations, or the common
even/odd directed coupling, are the discriminating continuation routes.

check_subadditivity_obstruction.py checks the exact normalization, a finite
set of literal scale identities, the exact tripling failure and the k=4
vector redundancy. The displayed construction and geometric series prove
the all-scale claims; finite fixtures alone do not prove them.
