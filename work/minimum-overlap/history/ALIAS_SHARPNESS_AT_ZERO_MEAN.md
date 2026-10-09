# Mean zero alone cannot sharpen the alias constant

The phase-averaged Gram relaxation uses the necessary alias bound

    c^T X c <= 1/12+(m/a)^2.

The rational constant 1/12 cannot be reduced merely by imposing m=0.
This is an explicit physical-density counterexample to that possible
strengthening, not an optimality claim for the minimum-overlap problem.

For any integer n>=2 put a=2/n. On each period [ja,(j+1)a], set r=+1
on the first and last quarter and r=-1 on the middle half. Put h=(1+r)/2
on [0,2], and extend r,h and the interval complement of h by zero as
appropriate. The density is admissible: 0<=h<=1 and integral h=1.
It satisfies h(2-x)=h(x), hence its overlap is even, d=0 and m=0.
Equivalently its first density moment is exactly 1.

Write u=s+a in [0,a] for the phase variable. The phase-centering error
E(u)=integral r(x)*(center_of_phase_cell-x) dx has E(0)=0, since every
full cell's r is symmetric about its midpoint. Its derivative is
-a times the n sampled support values of r, namely -2r(u). Therefore

    E(u)=-2u                 on [0,a/4],
    E(u)=2u-a               on [a/4,3a/4],
    E(u)=2a-2u              on [3a/4,a].

Its phase mean is zero and the exact phase average of E^2 is a^2/12.
The identity a*c.dot(r_cell)=-m+E then gives c^T X c=1/12 at m=0.
The general periodic Lipschitz estimate is thus sharp even on this
zero-mean physical class.

These examples have large overlap: directly at shift a/2,
p(a/2)=1-a/4. Thus they do not rule out a sharper *joint* restriction
that also uses a small peak cap, or other information about the same
density. That coupled question remains a possible continuation route.

The standalone exact checker check_zero_mean_alias_sharpness.py uses
rational cell-intersection integration of the physical density. It
checks n=2,3,7,16,127,128, mass, reflection, first moment, 102 literal
phase integrals, exact piecewise-affine variance, and the stated overlap
value. The report is runs/hybrid97-zero-mean-alias-sharpness.json.
No production proof checker, alias premise or promoted bound was changed.
