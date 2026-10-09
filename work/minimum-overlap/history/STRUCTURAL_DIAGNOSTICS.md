# Additional valid constraints with small observed objective gain

These are derived within the same continuous contract. They were tested in
discovery LPs and are not needed by the current global certificate.

## Complement-glued extension

Set H(x)=h(x) for 0<=x<2 and H(x)=1-h(x-2) for 2<=x<4, extended with period4.
Then 0<=H<=1, integral_0^4 H=2, and H(x+2)=1-H(x). Its circular overlap

    Q4(s)=integral_0^4 H(x)(1-H(x+s)) dx

is even and period4, with Q4(s+2)=2-Q4(s). Splitting the integral into its
four wrapped/unwrapped pieces gives, for 0<=s<=2,

    Q4(s)=s+p(s)+p(-s)-p(s-2)-p(2-s)
         =s+2[p_even(s)-p_even(2-s)].

The same pointwise d(a,b)=a+b-2ab triangle identities as CIRCLE_PROOF.md,
now integrated over length4, imply

    Q4(s+t)<=Q4(s)+Q4(t),
    Q4(s)+Q4(t)+Q4(s+t)<=4.

For 0<=s<=1, t=s, and a uniform positive density grid, write
S=2(identity-reversal) and let D average each doubled cell. The integrated
rows are (D-2 identity) S p<=0 and
(D+2 identity) S p<=4-4*cell_center. These rows use only the first half
of the cell indices; the remaining ones are reflections.

antiperiodic_diagnostic.py found pointwise violations above1.1 in one relaxed
primal, while the checked upper witness passed. Independently computing the
complement-glued circular correlation agreed with the formula to about2e-16
in the numerical fixture. The decisive reoptimization gave only about1e-9
of extra relaxed cap on1024cells, so this menu was parked. Large violation
does not imply large objective gain when the primal can change cheaply.

## Original support cap

For a,b in [0,1], d(a,b)<=1. On the overlap of [0,2] and its translate by s,

    p(s)+p(-s)=integral d(h(x),h(x+s)) dx <=2-s,  0<=s<=2.

Thus p_even(s)<=1-s/2. Cell averages obey the same bound with s replaced by
the cell center. This is an ordinary pointwise support/box inequality, not a
claim about a sampled maximum. primal_relaxation.py --tail-cap appends it.

The circle-only primal violates this cap by more than.22 at some cells.
Adding the cap on1024cells raises the relaxed optimum only from about
.38056701136 to.38056701983. Combining it with the complement extension gives
.38056702032. These roughly8e-9 gains are numerical diagnostics only. They
do not justify extending the trusted global checker for this menu presently.

## A related nonperiodic triangle

Extend both h and g=1-h by zero outside [0,2]. Integrating
d(h(x),h(x+s))+d(g(x),g(x+s)) over the real line gives
2s+4p_even(s) for 0<=s<=2, and4 for s>=2. Each summand satisfies a triangle
inequality. Therefore p_even(s+t)<=p_even(s)+p_even(t) when s,t>=0 and
s+t<=2. Its equal-leg averaged row is already implied by the ordinary and
complement-glued triangle rows above, so it was not separately scaled up.

## Executed records and limits

The numerical programs and records are antiperiodic_diagnostic.py,
runs/antiperiodic-diagnostic.json, runs/primal-antiperiodic1024/,
runs/primal-tail-only1024/ and runs/primal-tail-cap1024/. No additional
continuous global bound is claimed from these tests. The useful outcome is
the cost check: these valid restrictions eliminate a particular relaxed
primal but scarcely change its optimal objective with the current frequency
menu. Further effort should target an actual dual gain or a coupling that
the primal cannot repair at negligible cost.
