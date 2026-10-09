# Odd reflection cancellation: a derived discovery route

For every admissible density h, extend h and g=1-h by zero outside [0,2].
Write H(u)=integral_0^u h(x) dx and p(t)=integral h(x)g(x+t) dx.
The autocorrelation of h is even. For 0<=t<=2, subtracting p(-t) from p(t)
therefore gives H(2-t)+H(t)-1. In particular,

    p(t)-p(-t) = p(2-t)-p(t-2).

If z is odd on [-2,2] and z(2-t)=-z(t) on [0,2], then integral z(t)p(t)dt=0.
Bounded measurable z suffice; the proof follows by pairing t with 2-t.
The sine functions sin(n*pi*t) are examples. Decimal approximations to their
frequencies do not have exact zero expectation; the existing sine grammar
keeps the accepted nonzero upper bounds for those decimal frequencies.

For any valid kernel Q with integral Qp>=1, let A be its even part at t,
B its even part at 2-t, and s the sum of its odd parts at t and 2-t.
An allowed z redistributes the two odd parts to u and s-u. Their four
positive parts have minimum

    A+B+max(abs(A)+abs(B),abs(s)).

Indeed, (A+u)_+ +(A-u)_+ = A+max(abs(A),abs(u)). Minimizing the sum of
this expression and B+max(abs(B),abs(s-u)) gives the displayed formula:
the absolute-value triangle inequality gives the lower bound, and the
intervals [-abs(A),abs(A)] and [s-abs(B),s+abs(B)] give a minimizing u,
whether they overlap or are disjoint. Choosing an interval endpoint or a
clamped endpoint measurably gives a bounded minimizing correction for
bounded Q. Integrating this expression on [0,1] is thus the smallest
positive-part integral after these null corrections. A certified upper
bound D for that integral would imply mu>=1/D.

This is a derived route, not an executed continuum certificate or novelty
claim. The proposal probe checked 100 scalar minimum fixtures and four
exact overlap identities for a balanced rational step density. Applied to
the fixed wide29 phase kernel, quadrature orders 16/32/64 suggested gains
of 1.49e-8, 1.88e-8 and 1.86e-8. Their integration errors are unresolved.
The route was deferred because the signed-sine optimization produced a
larger executed conditional improvement through the existing proof grammar.
A future folded checker would need independent outward integration of the
absolute values and maximum, plus complete global mean coverage and replay.
