# Erdős #36 proof claim: form-ready draft

The supporting repository and versioned proof-packet release are linked below. Select Partial result when submitting.

## Claim title

Computer-assisted bounds for the minimum-overlap constant: 0.380627425 < μ < 0.3808585738345707361812673

## Claimed result

Select **Partial result**.

## Scope

Improved lower and upper bounds for the asymptotic minimum-overlap constant in Erdős problem #36:
$$
0.380627425 < \mu < 0.3808585738345707361812673.
$$
The lower bound applies to every admissible measurable density; the upper bound is witnessed by an explicit rational step density. The exact value of $\mu$ remains undetermined.

## Argument

Let $M_N$ be the minimum, over partitions $A\sqcup B=\{1,\ldots,2N\}$ with $|A|=|B|=N$, of $\max_k|\{(a,b)\in A\times B:a-b=k\}|$, and let $\mu=\lim_{N\to\infty}M_N/N$.

Use the equivalent continuous formulation: $0\le h\le1$ on $[0,2]$, $\int h=1$, and $g=1-h$ on that interval, with both functions extended by zero. Put $p(t)=\int h(x)g(x+t)\,dx$. Then $\mu=\inf_h\|p\|_\infty$.

**Lower bound.** Fourier and phase-averaged Gram inequalities give universal kernel inequalities $\int Kp\ge L(m)$, where $m=\int tp(t)\,dt\in[-1,1]$. Certified positive upper bounds $D\ge\int K_+$ give $\|p\|_\infty\ge L(m)/D$ on the covered cases, where $L(m)>0$. The transition cases strengthen this return using the same physical odd profile $d(t)=p(t)-p(-t)$: its boundary value, reflection identity, 1-Lipschitz bound and moment identity yield rational flow certificates with every residual and covariance error charged explicitly. The central case covers $|m|\le0.00004$ by a separate exact radius deduction from executions at $|m|\le0.00007$. Central, transition and outer intervals cover all of $[-1,1]$. Their finite collection of strict margins gives a uniform bound $\mu>0.380627425$.

The lower checkpoint passed a complete fresh-copy replay with Arb and separately implemented rational/dyadic arithmetic, exact coverage auditing, and three control suites. Its 115 frozen input files remained unchanged. Numerical optimizer output is used only to propose certificates.

**Upper bound.** An admissible rational step density on 14,337 nonuniform cells has exact overlap peak
$$
Q=\frac{10919977028984812147789295189227209}{28672000000000000000000000000000000}.
$$
Two exact arithmetic methods verified its mass, box constraints and all 86,017 shift knots. The overlap is affine between endpoint-difference knots, so these checks cover every real shift. The discrete/continuous return gives
$$
\mu\le Q<0.3808585738345707361812673.
$$

The supporting packet contains the analytic proofs, exact certificates, implementations, dependency manifests and executed original/fresh verification reports. Start with README.md and TECHNICAL_NOTE.md; run verify_packet.py and follow the replay instructions in both selected checkpoints. These are computer-assisted bounds, without proof-assistant formalization or external peer review.

## Supporting material — Link 1

- **Type:** Certificate
- **Label:** Reproducible proof packet for the minimum-overlap bounds
- **URL:** https://github.com/justinwetch/erdos-36-minimum-overlap/releases/tag/v1.0.0

The release provides the complete unchanged proof packet; the repository provides selected proof checkpoints, analytic notes and execution evidence.

Optional additional link:

- **Type:** Code
- **Label:** Verification code and exact certificates
- **URL:** https://github.com/justinwetch/erdos-36-minimum-overlap/tree/v1.0.0

## Additional details & attribution

The Fourier-analytic formulation builds on Ethan Patrick White's work. The cited public lower- and upper-bound certificate packages and public EinsteinArena construction data supply prior methods, implementations and baselines; the supporting packet records source versions and provenance.

The claim is limited to the displayed global interval. Stronger mean-zero experiments included as research history are not claimed as global bounds. Original and fresh local verification have passed; external mathematical review is requested.

Proof packet filename: minimum-overlap-final-627425.zip

SHA-256: 0031f6179312299e4d5934c8ed21dbf710b92f78421fcd0190988baed763432a

## Citations

1. Ethan Patrick White, *Erdős' minimum overlap problem*, arXiv:2201.05704. https://arxiv.org/abs/2201.05704
2. *Erdős Problem 36 Lower Bound Certificate*, pinned commit 6bc610e40083ef61a40966dfb5d38612cabc4c5b. https://github.com/Leeham06972452/erdos-36-lower-bound/tree/6bc610e40083ef61a40966dfb5d38612cabc4c5b
3. Kevin Russell, minimum-overlap upper-bound verification repository, pinned commit 29b938a3998d7e87cf8067625244c5ea20f4a5b0. https://github.com/techno-optimist/erdos-minimum-overlap-bound/tree/29b938a3998d7e87cf8067625244c5ea20f4a5b0
4. EinsteinArena, public construction data for the minimum-overlap problem. https://einsteinarena.com/

No claim has been submitted to erdosproblems.ai by this publication.
