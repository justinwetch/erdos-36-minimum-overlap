# Odd-grid phase energy

Let N>=3 be odd and m=N-1 be even. At a phase with endpoint support fractions
u and 1-u, write endpoint averages a,b and interior averages x_1,...,x_m.
Then |a|<=u, |b|<=1-u, |x_i|<=1 and a+b+sum x_i=0.

For even m and |s|<=1, the maximum of sum x_i^2 subject to sum x_i=s
is m-2|s|+s^2. A convex quadratic attains its maximum at a vertex of the
box section, where all but at most one coordinate are +/-1. The sum of
those m-1 coordinates is odd, hence the remaining coordinate has absolute
value at most 1-|s|. Conversely m-1 signs with sum sign(s), followed by
s-sign(s), attain the formula (choose either sign at s=0).

Consequently total squared energy is at most

    m + a^2+b^2 - 2|a+b| + (a+b)^2.

On either half of the endpoint rectangle cut by a+b=0, the displayed
quadratic is convex. Its maximum occurs at a polygon vertex. Put
w=min(u,1-u)<=1/2. At the intercept vertices a=-b=+/-w its excess over
m is 2w^2. At same-sign rectangle corners the excess is -2u(1-u)<=0.
At opposite-sign corners it is -2w+6w^2<=2w^2. Thus total energy is at
most m+2 min(u,1-u)^2. Averaging uniform phase u in [0,1] gives

    trace X <= N-1 + 1/6 = N-5/6.

The separate diagonal bounds would give N-1/3, losing 1/2. This is a
universal necessary constraint for the odd-grid Gram matrix. It does not
assert realizability or optimality, and no global minimum-overlap bound
uses it until a rational dual and its exact compiler have been checked.

Since y_0=1/2-a/12-(a/4)trace X and a=2/N, the same statement is
y_0>=a/8. This near-zero-shift constraint is far from active on the
tested profile: the N=33 fit has trace about17.86, compared with32+1/6.
No gain in that paired test is attributed to this inequality; ordinary
triangle cuts added in later rounds change the comparison independently.
