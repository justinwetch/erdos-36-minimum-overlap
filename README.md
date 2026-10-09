# Bounds for Erdős' minimum-overlap constant

Computer-assisted partial result:

$$0.380627425 < \mu < 0.3808585738345707361812673.$$

The problem remains open. These bounds have local original and complete
fresh-copy verification, with documented analytic premises; they are not
proof-assistant formalizations or externally peer-reviewed results.

## Read the argument

- [Technical note](TECHNICAL_NOTE.md): contract, lower return, full mean cover, upper witness and discrete bridge.
- [Lower checkpoint](outputs/minimum-overlap-hybrid106-radius-pypy627425-v1-checkpoint/README.md): 115 unchanged files.
- [Upper checkpoint](outputs/minimum-overlap-refined14336-upper-checkpoint-v2/README.md): 19 unchanged files.
- [Execution evidence](evidence/): actual replay reports, provenance and hashes.
- [Submission fields](SUBMISSION.md): ready-to-copy partial-result claim.
- [Timing](TIMING.md): discovery cutoff and actual verification times.

This repository focuses on the selected proofs and analytic notes.
The [v1.0.0 release](https://github.com/justinwetch/erdos-36-minimum-overlap/releases/tag/v1.0.0) contains the complete unchanged research
packet, including continuation code, research history and a launch prompt.
Some historical notes describe code and experiments available in that
full packet. Historical reports retain their original execution paths.
Checkpoint files are preserved from the verified packet. Statements in
those frozen documents about work not yet being posted describe their
pre-publication state.

## Reproduce

Use Python 3.12 in a project-local environment:

~~~powershell
python -m venv .venv
./.venv/Scripts/python.exe -m pip install -r requirements-replay.txt
./.venv/Scripts/python.exe verify_repository.py
./.venv/Scripts/python.exe reproduce.py --part all
~~~

The replay driver copies each proof into a fresh directory under work/.
The lower replay is computationally substantial. It uses Arb and separately
implemented rational/dyadic arithmetic; shared exact parsers and analytic
premises are disclosed. A compatible integer runtime is optional.

The upper replay checks an explicit 14,337-cell rational density and all
86,017 shift knots by two exact methods. Its exact peak is

$$\frac{10919977028984812147789295189227209}{28672000000000000000000000000000000}.$$

Numerical discovery scores and separate mean-zero experiments are not
additional global bounds. The claim concerns the asymptotic constant.

## Full packet

File: minimum-overlap-final-627425.zip

SHA-256: 0031f6179312299e4d5934c8ed21dbf710b92f78421fcd0190988baed763432a

The release also provides the matching continuation prompt and delivery
audit. Its ZIP is the previously verified packet, unchanged.

## Sources

The work builds on [Ethan Patrick White's formulation](https://arxiv.org/abs/2201.05704),
the [pinned lower certificate](https://github.com/Leeham06972452/erdos-36-lower-bound/tree/6bc610e40083ef61a40966dfb5d38612cabc4c5b),
the [pinned upper verification repository](https://github.com/techno-optimist/erdos-minimum-overlap-bound/tree/29b938a3998d7e87cf8067625244c5ea20f4a5b0),
and public EinsteinArena construction data. Source versions and shared
dependencies are recorded in the proofs and provenance. Existing source
notices are retained.
