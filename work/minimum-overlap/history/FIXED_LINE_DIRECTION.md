# A certified rejection of one coefficient direction

This is a statement about one fixed line of kernels. It is not an
optimality claim for joint optimization or a bound on the original mu.

Let Q be the retained H97 kernel, K the newly checked signed functional,
and L its mean-zero scalar lower bound. Add a nonnegative coefficient rho
for that functional and decrease the free constant coefficient by rho*L.
The mean-zero expectation numerator stays fixed. The new denominator is

    D(rho) = integral max(Q(t)+rho*(K(t)-L),0) dt.

It is convex in rho. Its right derivative at zero integrates K-L wherever
Q>0, zero wherever Q<0, and max(K-L,0) wherever Q=0. All quantities refer
to the same frozen kernel and separately replayed signed functional.

`enclose_added_functional_direction.py` aligns all affine jumps and knots,
uses outward fourth-order Arb Taylor bounds to classify signs of Q,
integrates the affine direction exactly on positive cells, and encloses
its possible contribution on unresolved cells. Exact zero cells use the
positive affine integral. Four literal positive, negative, identically
zero and crossing fixtures pass. In particular, zero intervals are not
silently treated as negative intervals.

For the original joint-alias functional, the actual outward derivative
enclosure is approximately [0.00244666375240706,0.00253572091676559], with
strictly positive exact lower endpoint in
`runs/hybrid97-joint-alias-direction-enclosure.json`. Convexity therefore
gives `D(rho) >= D(0)+rho*D'_+(0) > D(0)` for every rho>0. With its
positive unchanged numerator, this coefficient line strictly worsens the
mean-zero fixed-kernel ratio. A numerical positive gradient alone would
not establish this conclusion; the outward enclosure supplies the check.

The other coefficients are held fixed. Reoptimizing them, selecting a
different functional, or changing the analytic restrictions can still
help. This conclusion does not rule those possibilities out.

Replay from the research folder:

```powershell
python enclose_added_functional_direction.py runs/hybrid97-newrow-capacity627424-v1/central-frozen.json certificates/hybrid97-joint-alias-functional-v1.json runs/hybrid97-joint-alias-functional-replay.json --out runs/continued-joint-direction.json
```
