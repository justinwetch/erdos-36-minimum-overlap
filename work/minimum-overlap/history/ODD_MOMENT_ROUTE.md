# Historical odd-moment discovery notes (superseded)

The authoritative correction, continuous conditional proof and cheap-escape
test are now in ODD_JOINT_PROOF.md. In particular, the endpoint-envelope model
below is too restrictive for the relaxed profile's cell averages. No verified
global bound depended on it. The current default uses averaged constraints.

Obstruction: the even overlap relaxation has no requirement that its moments
come from one box-constrained density. Symmetric reconstruction fails at
degree12, while an asymmetric fit can repair it. That repair is not free:
the same odd density component creates an odd overlap component, which must
fit beneath the original maximum cap. This is a coupling the prior moment
fit discarded.

## Exact identities inside the original contract

For 0<=t<=2 define a(t)=p(t)-p(-t). Expanding the two overlaps cancels their
autocorrelation terms and gives

    a(t)=integral_0^t h(x)dx-integral_(2-t)^2 h(x)dx,
    a(2-t)=a(t),
    a'(t)=h(t)-h(2-t) almost everywhere.

Center h on[-1,1], put r=2h-1 and r_odd(u)=(r(u)-r(-u))/2. Then
a'(t)=r_odd(t-1), |r_odd|<=1. If v(u)=r_odd(u) for0<=u<=1, then

    a(t)=-integral_(1-t)^1 v(u)du,       0<=t<=1.

For p_even(t)=(p(t)+p(-t))/2 and M>=||p||_infinity,

    |a(t)|<=2[M-p_even(t)].

Combining reflection at2-t yields an envelope with p_even(t) replaced by
max(p_even(t),p_even(2-t)). The mass constraint and mean-zero branch require
integral_0^1 v(u)u du=0. For a general mean m, this integral is -m/2.

Write a_k=(1/2) integral_-1^1 r(u)u^k du as in MOMENT_ROUTE.md. For odd k,
a_k=integral_0^1 v(u)u^k du. The odd overlap moments satisfy

    E_p t^(2n+1)=-2 sum_(odd k<=2n+1) binom(2n+1,k)*a_k/(2n+2-k).

In particular E_p t^3=-2a_1-2a_3 and
E_p t^5=-2a_1-(20/3)a_3-2a_5. This follows from the odd part of
H(-z)G(z), namely -[2sinh(z)/z] A_odd(z). No reflection symmetry of h is
assumed. check_odd_mapping.py executed108 exact rational fixture checks,
including all odd-profile grid shifts and moments through degree12.

## Executed fixed-profile diagnostic

odd_cap_diagnostic.py holds the4096-cell even profile from
runs/circle-interior-original4096/primal.json fixed. It maximizes each odd
moment of a256-cell v in[-1,1], with mean zero and the reflected cap envelope.
It checks both endpoints of every even-profile cell; a is affine there on the
nested grid. Thus there is no missed interior maximum for this finite model.
The profile and LP values are floating proposals, not exact constraints or a
continuous universal certificate.

The maximum absolute moments found were approximately:

    |a3| <= .000090927,
    |a5| <= .000150345,
    |a7| <= .000208797,
    |a9| <= .000266281,
    |a11|<= .000322793.

The earlier asymmetric degree12 moment fit had a3~.00139078, a5~.00066221,
and a7~.00029969. It cannot simply be combined with this fixed even profile
and cap. That incompatibility changes the next test; it is not a new bound.
Another asymmetric density might match the moments with much smaller odd
moments, or the relaxed even profile may readjust cheaply.

The first degree5 LP returned an Unknown status, which was not interpreted as
infeasibility. Retrying with presolve disabled and dual simplex completed
successfully. The final records are runs/odd-cap-circle2/summary.json;
maximum floating envelope violations are below4e-11.

## Next discriminating test and obligations

First refit the general density moments subject to these necessary odd-moment
bounds, on the same256-cell odd grid. If this succeeds accurately, the coarse
moment bounds are insufficient; then test the full linear cap envelope or
close this reduced separator. Failure of a nonlinear optimizer is not an
infeasibility proof. If the joint model does separate, quantify the objective
cost while allowing the even profile and cap to vary before investing in a
trusted extension. Previous valid cuts often had negligible reoptimized gain.

A universal result would require: an analytic separator valid for all h,
outward evaluation of any polynomial or auxiliary integral, coverage of the
mean and any branched moment variables, a positive margin, and a bridge back
to the original cap. The fixed-profile LP and one failed nonlinear fit cannot
replace any of these obligations.
