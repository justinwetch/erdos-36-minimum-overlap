# Exact fractional-cut upper checkpoint

The included 14337-cell nonuniform step function proves mu < 0.3808585738345707361812673 for Erdős #36. It improves the included previously checked uniform baseline by 1.64163209055589e-13. This tiny refinement does not materially close the remaining gap.

The unchanged nonuniform checker checked all 86017 shift knots, mass, box bounds, two event maps and a direct integral at the peak. A separate packed integer convolution and affine-knot calculation gives exactly the same fraction. Read PROOF.md for the continuum-to-finite return, and the two additional proof notes for the specialized method. No numerical optimizer is required for replay. The discovery file only supplies rational cut parameters; it is not a proof of optimality. No priority or proof-assistant claim is made.

With Python 3.12 and NumPy, from this directory (the legacy nonuniform
module imports NumPy; its exact verification function uses integer and
rational arithmetic). The packed and fractional checkers use only the
standard library:

```powershell
python nonuniform.py best.json --out replay-direct.json
python exact_fractional_rotation.py baseline.json discovery.json --name replay-specialized
python exact_packed_correlations.py baseline.json --out replay-baseline.json
python check_packed_correlations.py --out replay-packed-controls.json
python check_exact_fractional_rotation.py --out replay-fractional-controls.json
```

The direct and specialized replay scores must equal comparison.json's improved_exact, and the packed baseline score must equal baseline_exact. MANIFEST.json binds the delivered inputs and checkers. This directory preserves original reports; fresh replay reports are retained separately in the campaign working records.
