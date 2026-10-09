# Verified findings

The campaign establishes the computer-assisted bounds

    .380627425 < mu < 0.3808585738345707361812673.

The remaining gap is 0.0002311488345707361812673. The lower target exceeds the pinned public
certificate's reported 0.38055470 by 0.000072725. This is a comparison with
that identified source, without a global priority claim. The upper
improvement is much smaller; its value lies mainly in preserving an
explicit exact witness and an independent replay.

[PUBLIC_COMPARISON.md](PUBLIC_COMPARISON.md) compares the selected bounds
with all six dynamically loaded claims on the user's erdosproblems.ai
page, including the stronger September lower claim 0.3805634. The
captured values are weaker than both selected endpoints. This describes
the captured public values, without external acceptance or priority claims.

## Mathematical scope

Erdos problem 36 asks for the limiting minimum peak number of differences
between two equal parts of {1,...,2N}, divided by N. The equivalent
continuous problem ranges over every measurable h on [0,2] with
0 <= h <= 1 and integral h = 1. Both h and its complement on that interval
are extended by zero. Write g=1-h on [0,2], and g=0 elsewhere.
The objective is the supremum, over every shift, of
p(t)=integral h(x)g(x+t) dx.
The lower bound is universal over that class. The upper bound comes from
one admissible density. The bounds do not meet, so the problem remains open.
The checkpoint's PROOF.md supplies the discrete/continuous return.

## What supports the bounds

The lower argument combines Fourier constraints, periodic triangle
inequalities and phase-averaged Gram constraints with a finite cover of
the density's first moment. Each kernel supplies a universal expectation
inequality and an independently enclosed positive-part integral. The final
transition argument also retains the physical odd profile
d(t)=p(t)-p(-t). Its Lipschitz constraint, boundary value and mean identity
give rational flow certificates. Every coefficient residual and covariance
error is paid explicitly. The aligned mesh includes every kernel jump;
an exact counterexample shows why omitting this condition would fail.

The lower checkpoint passed its original integrations, exact coverage
audit and a complete fresh-copy replay with all frozen inputs unchanged.
The upper checkpoint contains a nonuniform density with 14337 cells.
Two exact arithmetic methods checked its mass, box constraints and all
86017 shift knots; piecewise affinity covers the intervening shifts.
All five upper replay commands passed.

Replay the frozen [lower checkpoint](outputs/minimum-overlap-hybrid106-radius-pypy627425-v1-checkpoint/README.md)
and [upper checkpoint](outputs/minimum-overlap-refined14336-upper-checkpoint-v2/README.md). Their manifests,
implementation hashes and execution reports identify the assumptions and
shared dependencies. Independent arithmetic checks are not a
proof-assistant formalization. Packet validation also checks portable
imports, exact row reconstruction and control fixtures; it does not
replace either proof replay.

## Limits and continuation

Numerical LP and SDP outputs supplied proposals, without certifying their
optimality. Mean-zero scores and virtual profiles are not global bounds
or admissible overlap constructions. Failed gradient, calibration,
coverage and solver attempts are retained in the evidence and history.
Several earlier facet menus produced only small gains. The late
[joint alias/interior-trace route](work/minimum-overlap/JOINT_ALIAS_TRACE.md)
derives a further necessary inequality and is kept separate from the
frozen production grammar. Its numerical and standalone functional checks
do not by themselves promote a global bound. No result has been posted
or submitted.

The [current-kernel retargeting discriminator](work/minimum-overlap/CURRENT_RETARGETING_RESULTS.md)
produced a separately replayed functional with a strictly negative outward
fixed-line derivative. Its production-accepted weaker surrogate also has
a negative direction. This proves a local mean-zero kernel improvement
exists; it supplies neither a global target nor a full mean cover. Failed
calibration and time-limited finite LP prerequisites are retained.

The [subadditivity experiment](work/minimum-overlap/SUBADDITIVITY_RESULTS.md)
excludes the current virtual profile by an exact rational inequality and
checks a negative fixed-line derivative. The separate
[directed return](work/minimum-overlap/DIRECTED_SUBADDITIVITY_RETURN.md)
retains a coupling with the same physical odd profile and supplies exact
integer-dilation hat rows. These are continuation evidence and are not
premises of the selected production checkpoint.

The next useful target is a stronger central certificate, with explicit
treatment of nearly flat kernel regions, or a new realizability
constraint that excludes the remaining relaxed profiles. Improving a
transition cover alone cannot exceed its limiting central return.
Read [START_HERE](work/minimum-overlap/START_HERE.md) for executable entry
points and the full certification obligations.

The supplied hard-problem-reasoning skill was used as a working method
and is bundled unchanged. This single campaign does not establish that
the skill caused the improvement. Problem selection broadened beyond its
source collection; no canonical ranking of 500 open problems was assumed.

Primary references: [problem statement](https://www.erdosproblems.com/36),
[White's lower-bound paper](https://arxiv.org/abs/2201.05704),
[pinned lower certificate](https://github.com/Leeham06972452/erdos-36-lower-bound/tree/6bc610e40083ef61a40966dfb5d38612cabc4c5b),
[pinned upper construction](https://github.com/techno-optimist/erdos-minimum-overlap-bound/tree/29b938a3998d7e87cf8067625244c5ea20f4a5b0).
Latest read-only source checks are retained in evidence.

See [TIMING.md](TIMING.md) for the research cutoff and the actual completion
time of the final frozen verification. Later packet checks establish
delivery integrity and portability; they do not extend the discovery window.
