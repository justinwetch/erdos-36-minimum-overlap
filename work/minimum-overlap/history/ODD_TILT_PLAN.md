# Odd mean terms: a tested bridge and its present limit

No result in this note replaces the promoted global bound. The inequalities
below are derived; their numerical kernel integrations remain discovery.

Write a(t)=p(t)-p(-t) for 0<=t<=2. Expanding the overlaps gives

    a(t)=H(t)+H(2-t)-1,  H(t)=integral_0^t h(x)dx.

Hence a(2-t)=a(t). If m=integral_{-2}^2 t p(t)dt, reflection shows
m=integral_0^2 a(t)dt. These identities assume neither symmetric h nor
zero m. They agree with the mean convention used by the pinned outer
certificate. ODD_JOINT_PROOF.md and check_odd_mapping.py supply the earlier
independent exact mapping controls.

For a checked even kernel Q with integral p Q >= L0-C*m^2, consider a
positive mean bin [lo,hi]. A nonnegative beta and any measurable w with
w(t)+w(2-t)=2*beta define the odd kernel W(t)=sign(t)*w(|t|).
Reflection gives integral p W=beta*m. Therefore

    integral p [Q+W-beta*lo] >= L0-C*hi^2.

For negative bins reflect the odd kernel. The simple choice W(t)=beta*t
is valid, but it discards freedom in w. Its scalar probe passed 25
quadratic-integral and derivative fixtures (maximum errors 4.45e-16 and
2.34e-14); the actual baseline matched the old oracle to 6.22e-15.
At mean .002914 its gain is only on the order of 1e-12.

The full reflection freedom can be eliminated pair by pair. For t in[0,1]
put q=Q(t)-beta*lo and r=Q(2-t)-beta*lo. Define

    psi(q,w)=(q+w)^+ + (q-w)^+
            =2*q^+ + (|w|-|q|)^+.

The exact infimum over w(t)+w(2-t)=2*beta is

    2*q^+ + 2*r^+ + (2*beta-|q|-|r|)^+.

Indeed the excess cost is at least (2*beta-|q|-|r|)^+ by the triangle
inequality. Allocate w(t) in[0,2*beta], first within capacity |q| and then
within |r|; this attains the lower value. That prescription is measurable,
so pairwise minimizers assemble into one valid kernel. The full positive
integral is the displayed expression integrated over t in[0,1]. This is a
return argument for the auxiliary kernel, not a density construction.

reflection_mean_probe.py checked the pair formula on 100 piecewise-linear
fixtures by independently enumerating all breakpoints in w. Maximum error
was 4.45e-16. It integrates the change from the original kernel, reducing
baseline quadrature cancellation. Gauss orders 16/32/64 at mean .002914
give gains 3.02058e-8, 3.02032e-8, 3.02024e-8. Their baseline integral
errors are 2.54e-9, -5.06e-10 and 2.62e-10. These agreements are numerical,
not outward enclosures or proof of scalar global optimality in the
continuous model. At mean .00625 the numerical gain is about 1.52e-7;
the remaining quadratic penalty is still much larger.

The comparison explains the linear tilt failure: using reflection lets
the odd term allocate its cost across paired points. That recovers much
more than an odd linear term, but still too little to justify a new exact
integration grammar now. No odd-kernel fields were silently inserted into
the old hybrid schema. A future promotion would need outward integration
of the paired max/absolute-value expression, an independent arithmetic
implementation, interval rather than point mean bins, complete coverage,
and fresh-copy replay. Additional Lipschitz constraints on a would be a
different route with new obligations; the present pair minimization does
not use them.
