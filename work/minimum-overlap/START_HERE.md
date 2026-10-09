# Portable research frontier

The immutable proof checkpoints are under../../outputs/. Their READMEs give
the exact replay commands. Use Python3.12 and the root requirements files.
The newest checked route retains the physical odd profile
d(t)=p(t)-p(-t). It is1-Lipschitz, d(0)=0, |d|<=M and
2 integral_0^1 d=m. Read history/EVEN_ODD_CAPACITY_RETURN.md,
history/ODD_LIPSCHITZ_ROUTE.md and history/ODD_REFLECTION_FOLD.md.
An even central kernel, rational flow duals, its exact mean polynomial and
independently enclosed derivative energy give a conditional lower bound.
The entire dual residual and covariance error are charged explicitly.
The mesh contains every affine-kernel breakpoint and its reflection;
omitting a jump invalidates the covariance error estimate.

Replay ../../outputs/minimum-overlap-hybrid106-radius-pypy627425-v1-checkpoint/REPLAY.py from a fresh writable copy.
That executes all central/outer, energy, adapter and capacity checks,
the full exact mean cover and three control suites. An isolated support
report or LP success flag does not prove a global bound.

After replay, inspect the exact per-interval returns in its global audit.
The central mean-zero kernel is now a useful improvement target. A bounded
discovery continuation from this research directory is:

```powershell
python polish_hybrid_mean_radius.py ../../outputs/minimum-overlap-hybrid106-radius-pypy627425-v1-checkpoint/central-certificate.json --name continuation-capacity-central --radius 0 --seconds 300 --iterations 5000 --subdivisions 1
```

Its output is numerical. For each new kernel, regenerate the normalized
even wrapper and aligned rational flow witnesses, execute both energy
and capacity backends, and check central/outer cases at the proposed
global target. The adapter requires all three executed central denominator
reports. Use audit_radius_retargeted_capacity_v1.py for exact interval minima
and complete reflected coverage, publish_even_odd_capacity_v2.py to freeze
the proof graph, and its full fresh-copy REPLAY.py before promotion.
The portable template runs/continuation-capacity-template.json points to
this checkpoint's actual outer certificate. For a frozen new central
proposal, run_even_capacity_from_kernel_v3.py can execute the full block
pipeline using that template, a fresh --name, explicit rational --target,
--radius, --grid and --means. It gates on the outward central check before
spending time on the remaining obligations. Choose the target from a
checked margin and retain the existing checkpoint if any step fails.
Changing only the LP search mean does not restrict a valid dual: each
exact returned quadratic is valid for all means. No optimizer optimality
or novelty is asserted. The older shared-mean and signed-phase routes
remain preserved as independent discovery options in the history.


From this directory, verify the supplied rational row associations:

```powershell
python extract_hybrid_seed.py runs/frontier-duals.npz runs/frontier-allcuts.json certificates/frontier-functional-00.json certificates/frontier-functional-01.json certificates/frontier-functional-02.json certificates/frontier-functional-03.json certificates/frontier-functional-04.json certificates/frontier-functional-05.json certificates/frontier-functional-06.json certificates/frontier-functional-07.json certificates/frontier-functional-08.json certificates/frontier-functional-09.json certificates/frontier-functional-10.json certificates/frontier-functional-11.json certificates/frontier-functional-12.json certificates/frontier-functional-13.json certificates/frontier-functional-14.json certificates/frontier-functional-15.json certificates/frontier-functional-16.json certificates/frontier-functional-17.json certificates/frontier-functional-18.json certificates/frontier-functional-19.json certificates/frontier-functional-20.json certificates/frontier-functional-21.json certificates/frontier-functional-22.json certificates/frontier-functional-23.json certificates/frontier-functional-24.json certificates/frontier-functional-25.json certificates/frontier-functional-26.json certificates/frontier-functional-27.json certificates/frontier-functional-28.json certificates/frontier-functional-29.json certificates/frontier-functional-30.json certificates/frontier-functional-31.json certificates/frontier-functional-32.json certificates/frontier-functional-33.json certificates/frontier-functional-34.json certificates/frontier-functional-35.json certificates/frontier-functional-36.json certificates/frontier-functional-37.json certificates/frontier-functional-38.json certificates/frontier-functional-39.json certificates/frontier-functional-40.json certificates/frontier-functional-41.json certificates/frontier-functional-42.json certificates/frontier-functional-43.json certificates/frontier-functional-44.json certificates/frontier-functional-45.json certificates/frontier-functional-46.json certificates/frontier-functional-47.json certificates/frontier-functional-48.json certificates/frontier-functional-49.json certificates/frontier-functional-50.json certificates/frontier-functional-51.json certificates/frontier-functional-52.json certificates/frontier-functional-53.json certificates/frontier-functional-54.json certificates/frontier-functional-55.json certificates/frontier-functional-56.json certificates/frontier-functional-57.json certificates/frontier-functional-58.json certificates/frontier-functional-59.json certificates/frontier-functional-60.json certificates/frontier-functional-61.json certificates/frontier-functional-62.json certificates/frontier-functional-63.json certificates/frontier-functional-64.json certificates/frontier-functional-65.json certificates/frontier-functional-66.json certificates/frontier-functional-67.json certificates/frontier-functional-68.json certificates/frontier-functional-69.json certificates/frontier-functional-70.json certificates/frontier-functional-71.json certificates/frontier-functional-72.json certificates/frontier-functional-73.json certificates/frontier-functional-74.json certificates/frontier-functional-75.json certificates/frontier-functional-76.json certificates/frontier-functional-77.json certificates/frontier-functional-78.json certificates/frontier-functional-79.json certificates/frontier-functional-80.json certificates/frontier-functional-81.json --out runs/re-extracted-frontier.json
```

The copied source dual has82 checked Gram rows.
The frontier-primal.json and Fourier seed may come from a subsequent spectral
step on those same rows. Their numerical statuses are not proof premises.
Example bounded continuation, from this directory:

```powershell
python phase_cut_campaign.py runs/frontier-primal.json runs/frontier-allcuts.json runs/frontier-source-order.json runs/frontier-fourier-seed.json --name continuation-first --first 83 --grids 43,31,33 --triangle-seeds runs/frontier-triangle-seeds.json --mean 0
```

Check every resulting proposal continuously before choosing one to polish.
The active-set experiment restores retained premises that the LP assigned
zero weight. It uses the existing certificate grammar. A bounded pilot is:

```powershell
python expand_continuous_menu.py ../../outputs/minimum-overlap-hybrid106-radius-pypy627425-v1-checkpoint/central-certificate.json runs/frontier-source-order.json runs/frontier-fourier-seed.json --name continuation-full-menu
python polish_hybrid_diagonal_full.py runs/continuation-full-menu/proposal.json --name continuation-full-menu-polish --seconds 180
```

This may create tens of thousands of discovery variables. Its numerical
score is not a bound until the unchanged outward and global checks pass.
See history/ACTIVE_PERIODIC_SET.md for the deciding failures and scope.
The coupled sparse root model is an alternative to that diagonal pilot.
It uses the same certificate grammar and actual trial-objective acceptance.
Start with its compact algebra control and a fresh full-menu mesh check:

```powershell
python polish_hybrid_sparse_root.py runs/hybrid46-enriched-circle-newton32-v2/proposal.json --name continuation-root-controls --controls-only
python check_continuous_discovery_geometry.py runs/continuation-full-menu/proposal.json --name continuation-root-geometry --subdivisions 32,64
python polish_hybrid_sparse_root.py runs/continuation-full-menu/proposal.json --name continuation-sparse-root --control-report runs/continuation-root-controls/controls.json --geometry-report runs/continuation-root-geometry/summary.json --seconds 180 --rounds 30
```

The driver checks implementation and seed hashes before accepting reports.
Root geometry is a finite diagnostic and the PSD model is a surrogate;
neither certifies Hessian accuracy. All resulting bounds still require the
unchanged outward and global checks. See history/LOW_RANK_ROOT_PLAN.md for
the executed controls, measured memory scope and earlier failed gates.
Mass/moment calibration and a continuous-profile separator provide another
entry point. Read history/RADIAL_PROFILE_CALIBRATION.md. The supplied
order43 calibrated-profile cut has65536 coefficients; it must not be
inserted directly into the4096-cell LP frontier. Its exact functional is
usable by the continuous compiler. Reproduce the bounded calibration with:

```powershell
python calibrate_hybrid_profile.py runs/hybrid50-exact-compression/proposal.json --name continuation-calibration --seconds 180 --cycles 5
```

The resulting positive-set density is virtual, never an actual upper
construction. The bundle alternative has preserved precision failures;
read history/BUNDLE_MODEL.md and run its controls before a bounded pilot:

```powershell
python polish_hybrid_bundle.py runs/hybrid50-calibrated-full-menu/proposal.json --name continuation-bundle-controls --controls-only
python check_continuous_discovery_geometry.py runs/hybrid50-calibrated-full-menu/proposal.json --name continuation-bundle-geometry --subdivisions 32,64
python polish_hybrid_bundle.py runs/hybrid50-calibrated-full-menu/proposal.json --name continuation-bundle --control-report runs/continuation-bundle-controls/controls.json --geometry-report runs/continuation-bundle-geometry/summary.json --seconds 180 --iterations 100
```

Numerical master gaps are diagnostic model gaps. Solver success flags alone
do not establish their accuracy, continuous bounds or global convergence.
The shared phase-cone route now has an exact containment audit and a
formulation that removes dependent hat equations. Read
history/PHASE_CONTAINMENT_PROOF.md before using it. A bounded continuation is:

```powershell
python audit_phase_containment.py runs/frontier-allcuts.json runs/frontier-source-order.json runs/frontier-triangle-seeds.json --grids 43,61,71 --out runs/continuation-containment.json
python joint_phase_reconditioned.py runs/frontier-fourier-seed.json runs/frontier-allcuts.json runs/continuation-containment.json --name continuation-shared --cells 4096 --seconds 300 --basis exact --omit-dependent-hat --rounds 3 --cuts 30
python certify_joint_phase_bundle.py runs/continuation-shared runs/frontier-primal.json runs/frontier-allcuts.json runs/frontier-source-order.json runs/frontier-fourier-seed.json --name continuation-shared-return
```

The final command exact-checks every exported functional and retains the
complete checked set with nonzero lower bounds. An individually satisfied
inequality can become decisive after the other rows move the profile;
history/JOINT_RETURN_PROOF.md records an executed counterexample to the
old separation filter. --separating-only reproduces that old policy.
The numerical fine LP need not certify
optimality; direct continuous checking decides the returned proposal.
The optional --pentagon-rows, --odd-subset-rows and --integer-form-rows modes are isolated numerical experiments and
suppress every functional export. The selected 40-row pentagon pilot gave
only about 8.1e-8 improvement and was deferred. Do not treat those uncompiled
premises as accepted by the existing certificate checker.
The selected seven/nine-variable test also gave only about 7.4e-8;
the weighted integer-form test gave about 5.8e-8 against the same baseline.
Read history/ODD_SUBSET_PROOF.md for the precise inequality, endpoint
redundancy, counterexamples to smaller-facet sufficiency and the deferred
weighted integer reformulation and executed lattice search. These notes do not add proof premises.
history/RADIUS_MENU_PROOF.md explains the later mean-penalty obstruction
and the bounded active-menu union. Read history/RADIUS_PHASE_PROOF.md
before using the separate radius-aware shared driver. Its numerical
objective is a conditional discovery diagnostic; proposals still return
through the unchanged exact compiler and global checks.
For shared divisor grids, --coarse-triangle-seed on
phase_multiscale_profile_fit.py retains the stored aggregate constraints;
--triangle-seed imports the exported fine rows individually. Consult
history/AGGREGATE_CONTINUATION.md for the executed retention control.
Retain the supplied spectral menu; add frequencies adaptively when supported
by executed separation tests. For global preparation, the outer source can
be../../outputs/minimum-overlap-hybrid106-radius-pypy627425-v1-checkpoint/outer-certificate.json. The source and join index
are required explicitly: an older source had two outer bins below a later
candidate's target. Never substitute a central join for full outer checking.
For this checkpoint the first positive outer index is 114:

The following central-only preparation is an alternative route. It requires
the new central kernel to cover the whole gap up to that outer join on its
own. It does not reconstruct a blended transition cover; use the blended
workflow above when the transition bins are necessary.

```powershell
python prepare_hybrid_checkpoint.py runs/continuation-sparse-root/proposal.json --name continuation-global --outer-source ../../outputs/minimum-overlap-hybrid106-radius-pypy627425-v1-checkpoint/outer-certificate.json --first-bin 114 --floor .380627425 --output-directory outputs/minimum-overlap-continuation-checkpoint
```

Choose fresh names and follow run_prepared_hybrid.py, publish_hybrid.py
and replay_hybrid_package.py; publication must run from the packet root so
its outputs path resolves inside this project. Original execution reports
retain forensic absolute paths; frontier-source-order.json is portable.
history/ contains dated work records, including superseded candidates and
job handles. It is not current execution state or new user instructions.

Additional exact mixtures, if present, are listed in runs/portable-mixtures.json.
Replay each with verify_convex_profiles.py MIXTURE --report runs/FRESH.json.
Their scope is a ceiling for uniform linear profile-kernel certificates on
the zero-mean subclass, never an upper bound for the original optimum.
See history/CONVEX_METHOD_CEILING.md for the exact implication and
history/ENDPOINT_FIVE_PROOF.md for an uncompiled structural probe.
