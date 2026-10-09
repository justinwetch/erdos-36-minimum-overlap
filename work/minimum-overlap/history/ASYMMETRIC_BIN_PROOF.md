# Optimizing compatible coordinates on one mean bin

Status: analytic return derived in this work; numerical pilot in progress.
No new promoted bound. The certificate grammar and both blend checkers
are unchanged by this discovery driver. No novelty or skill-efficacy claim.

The scalar blend restricts the two valid kernels to one mixing coordinate.
For a fixed bin I=[lo,hi] with0<=lo<=hi, write each normalized even kernel
coordinate as Phi_j^0, with expectation >=-p_j*m^2 and p_j>=0. These are
the second moment coordinate, upper cosine inequalities, periodic rows,
and signed Gram functionals. Thus Phi_j^I=Phi_j^0+p_j*hi^2 has nonnegative
expectation on the whole bin. For each accepted outer row let
Psi_r^I=B_I,r-phi_r, also with nonnegative expectation there.

For every nonnegative pair of coefficient vectors u,v,

    Q=1+sum_j u_j Phi_j^I+sum_r v_r Psi_r^I

satisfies integral pQ>=1 for the same original admissible density p.
The positive-part integral is a convex function of these linear weights.
Numerical optimization on quadrature nodes is a surrogate for that
continuous objective and gives neither a rigorous bound nor optimality.

An exact return uses the existing hybrid-outer-blend-v1 grammar. Put
d=hi^2, theta=1/2, T=1/2+d*(p dot u), and w=u/T. Then

    ell=1-d*(p dot w)=(1/2)/T,
    (1/2)*w/ell=u,
    (1/2)/ell+1/2=1+d*(p dot u).

Export the mean-zero normalized hybrid with weights w, and export an
outer kernel with weights2v. Their theta=1/2 blend therefore equals Q.
Nine rational fixtures check this normalization identity exactly. Seven
finite-difference checks exercise the quadrature gradient away from nodes
where the positive part is nondifferentiable.

Actual exports round coefficient vectors and y0. They propose a rational
ell below the nominal numerator, with a1e-10 margin. That margin is not
accepted as an unproved error estimate: both existing blend compilers
recompute the true numerator from the rounded certificate and must prove
ell<=Lh(I). Once they pass, validity follows directly from the exported
certificate, irrespective of errors in the numerical return identity.
Both continuous integration organizations and complete global mean
coverage still decide any claimed original bound. The already frozen
twelve-bin scalar cover is preserved while this separate pilot runs.

This applies P09 to a shared feasible region, and P27/P24 to the rounded
return. The deciding test is an outward improvement from the exported
kernel, rather than a smaller quadrature objective or an optimizer flag.


2026-10-08T17:33:12.882234+00:00. Goal ACTIVE through Oct9 02:00 UTC; no early completion.
Promoted interval remains .380623753 < mu < .3808585738345707361812673.
Old12-bin scalar blend target .380624000: both Arb modes PASS; central3,
mapping, both182-caseoutercheckers PASS610.178s. Fullinteger LIVE46214,
8/12? Confirm controller rather than this snapshot; index8 completed2066.969s.
New prototype coordinate fit I[.00318,.00320] Arb4PASS .38062482168251525;
independentinteger LIVE89589, last piece800/1756. Arb2 pending.
Compiler controlv2 PASS76.624s, adds2784 exact affine-piece comparisons.
Auditv1 selfhash patched before anyglobalexecution; v2 explicitfork permits
different validhybridperbin, notyet fullglobalexecuted. Newpublisher and
replaytools created/pycompilePASS, no package or actualfreshreplay yet.
Names publish_blended_hybrid.py,replay_blended_in_place.py,
replay_blended_checkpoint.py. Auditv1 SHA7f59efa7a91b8b592feca808b61802c80d185e6a5414736a8e6a24e725501a10.
Auditv2 SHAc5687991426c02a536dee33529cbbf15ab328bed962a38e118011c0a14b7741a.

Coordinate asymroute: ASYMMETRIC_BIN_PROOF.md, optimizer566vars with unionseed.
Pilot gain7.69e-7 onfixedbin, notglobal. narrowfirst [.0028,.00285]
Arb4PASS .38062455965372652. Nine-bin generation v1 FAILED index1
[.00285,.0029] quadrature64 .38062447714989056 vs .380624500 target.
Preserved failure.json and allcandidates. No full9binconfig exists.
Restriction decidingtest COMPLETE: reusedsamefailedcoefficients,
lowerhalf [.00285,.002875] Arb4PASS .38062451628096391;
upperhalf [.002875,.0029] .38062447807474708 FAIL;
point [.0029,.0029] .38062447900858879 FAIL. All three complete
continuousoutward integrations, conditional scope only. Thus interval
splitting alone cannot meet this target usingthiskernel. Numericaloptimizer
stoppedftol1377calls, no optimalityclaim. Root-aware jointreweighting now
LIVE75113, 240s timebox (initialization/geometry extra). Newdiscoverymodules
asymmetric_root_oracle.py,polish_asymmetric_roots.py; no trustedcheckeredits.
Requiresrootgeometry refinement, FDcontrols, then Arb+integer ifpromising.
Consumed72444 restrictiondriver; reports runs/hybrid82-asymmetric-restriction-probe-v1.
Originalfour currentlive? Actual LIVE46214,89589,75113 only.

LatestprimaryGET17:30:07UTC allthreeUNCHANGED; sources/freshness-20261008T173007Z.json.
Nextfreshnessabout18:30. Noagents, noexternalwrites, nofinalZIPdelivery.
Privatevalidateddraft79 remainsfallback. Builder mustadd latestresearch
modules/evidence and newblendedcheckpoint beforefinal. Outputsprogress
accurate promotedinterval; no newglobalclaim. Continue independently.

