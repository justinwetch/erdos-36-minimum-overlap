# Minimum-overlap campaign

Deadline: 2026-10-08 19:00 Alaska daylight time (UTC-8), or 2026-10-09 03:00 UTC, extended by the user's latest instruction. Research stops at that deadline; delivery assembly and verification may finish afterward. Results need not settle the full problem.

Final verification policy: no new discovery or proof inputs after the
research cutoff. The already frozen .380627425 global candidate may finish
its running delivery verification until 03:10 UTC. Its original full-mean
audit passed before the cutoff. Record a late fresh confirmation as late;
do not count it as a pre-cutoff receipt. Other unfinished research checks
are preserved as partial. Packet transport validation may finish later.

## Exact target

Latest fully promoted checkpoint: **.380627425 < mu < 0.3808585738345707361812673**. The lower package is outputs/minimum-overlap-hybrid106-radius-pypy627425-v1-checkpoint; its complete fresh replay, controls and exact global coverage audit passed. The upper package is outputs/minimum-overlap-refined14336-upper-checkpoint-v2; all five fresh replay commands passed. The open problem remains unresolved. Current promotion records and outputs/minimum-overlap-progress.md supersede dated claims below.
The earlier bounds below are preserved as campaign history.

For each positive integer N, partition {1,...,2N} into A and B of size N. Let M(N) be the minimum, over such partitions, of max_k |{(a,b): a in A, b in B, a-b=k}|. The open problem is to determine mu = lim M(N)/N. Our attack targets a strict certified improvement of either bound for mu. The initial upper-construction route has been supplemented by the more productive universal lower-certificate route. This changes the method, not the mathematical target. Exact determination requires matching universal lower and constructive upper bounds.

Use the standard continuous formulation: f:[0,2]->[0,1], integral f=1; g=1-f on [0,2], with BOTH functions extended by zero outside [0,2]. Define C_f(s)=integral f(t)g(t+s)dt. An admissible f gives mu <= sup_s C_f(s). PROOF.md derives the probabilistic return, the balancing loss, and the known continuum equivalence. LOWER_PROOF.md records the universal lower reduction and outward integration argument.

Fixed: support, box constraints, mass, original overlap objective, deadline, and exact certification requirements. Free: number and location of steps, their heights, search and proof methods. No submission or public posting is authorized by this research request.

## Selection decision

Broadened beyond the previous repository to recognized open mathematical problems. Compared minimum overlap, small Ramsey constructions, and the union-closed conjecture as routes to verifiable progress within the research window (extended by the user to October 8 at 18:00 AKDT). Minimum overlap is preferable because an explicit density can certify a new infinite-problem bound through a finite exact calculation, while numerical improvement is meaningful without solving the whole conjecture. This is a tractability choice, not a ranking among a supposed canonical top 500.

## Bounds and evidence status

White's peer-reviewed lower bound is 0.379005; a June 2026 preprint reports 0.37912, and a September preprint reports 0.380552. These literature results remain source-reported. A later public lower certificate at commit 6bc610e40083ef61a40966dfb5d38612cabc4c5b claims 0.38055470; its central source bins were executed and analytic reduction reviewed. The present campaign has verified **0.380565779** using periodic triangle constraints at four scales on the central mean interval, both second- and fourth-order continuous Arb replays, 174 executed Fourier outer cases, and a combined coverage/hash audit. CIRCLE_PROOF.md records the additional analytic inequalities and trusted extension. The earlier full 0.38055650 Fourier certificate passed both unchanged original and fourth-order checkers. The live 3584-step public upper witness was acquired and exactly checked: Q < 0.3808585748578583091444424. The campaign now also has an exactly checked7168-step construction below0.3808585738368000599384507, improving the previously checked baseline by about1.02e-9. This remains a tiny upper improvement. The independent integer central replay, both Arb central orders, both outer replays and both combined audits are published in outputs/minimum-overlap-integer-fourier-checkpoint; the exact upper witness is in outputs/minimum-overlap-projected-upper-checkpoint. No global priority claim is made from a web search or a comparison with one source.

## Obstruction and routes

The step-function representation makes the continuum objective a finite maximum of quadratic correlations. A solver's lower floating score is insufficient because exact mass repair, box feasibility, or an unchecked shift can erase the gain. After baseline execution, diagnose the active optimization obstruction separately.

At most three active routes, updated after executed failures:
1. Lower dual certificate: adapt mean bins, jointly optimize multipliers, compress repeated phase rows, and add frequencies identified by reduced costs. Falsifier: the claimed gain disappears in full outward verification or exposes an analytic gap.
2. Upper construction: retain the executed uniform/nonuniform checkers and completed searches. Dense 3584-step LPs timed out twice; small smooth coordinate warps failed. Projected mass/box searches and cell-splitting charts now give tiny exact improvements; retain the best witness and test materially different moves.
3. Structural constraints beyond the current Fourier menu: investigate phase-averaged Gram matrices and a checkable obstruction to the relaxation. Falsifier: a proposed inequality is redundant, or a valid admissible function violates it. No new inequality is admitted into the trusted certificate without a proof and verifier extension.

## Skill obligations

P37: bounds concern the same mu, universal lower and constructive upper separately. P28: every local gain is net of box and mass repairs and exact evaluation. P30: provide the return map from density to equal-size finite partitions, with uniform concentration and balancing loss. P23: attack shift coverage and mass normalization. P24: independent exact checker and executed logs, with the scope of every check explicit.

Status words: proposed; derived_under_assumptions; established_in_this_work; refuted. Finite local optimality, failed search, and numerical stability are not lower bounds on mu. No priority claim over uninspected live results.
