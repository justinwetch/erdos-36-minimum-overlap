# Five-variable Gram constraints: a bounded diagnostic

For any five real numbers r_i in[-1,1] and any signs b_i in{-1,1},

    -sum_(i<j) b_i b_j r_i r_j <= 2.

The expression is multilinear, so a maximum over the cube occurs at a
vertex. There it equals(5-(sum_i b_i r_i)^2)/2. The signed sum is odd and
has absolute value at least1, proving the inequality. Averaging over the
common grid phase gives the same inequality for the five off-diagonal
entries of the cell-average Gram matrix. This derivation is independent
of whether the relaxed matrix is realizable by an admissible density.

The deep43-cell fit on the38-row adversarial profile retained522 ordinary
triangle constraints. Its final numerical unadded triangle violation was
1.043e-5. A scan of17,376,128 signed five-variable facets in the44-dimensional
matrix found598 violations above1e-7, the largest0.0016932618369507324.
This is a numerical separation diagnostic, not a certificate.

A paired comparison kept the same522 triangles and profile. The control
minimum mismatch was0.0008700703751763212; adding the100 largest scanned
five-variable constraints gave0.0008709804217475729. The independently
displayed actual mismatch increased by9.100486678369213e-7. Both solver
statuses were optimal_inaccurate; minimum numerical eigenvalues were
approximately-6.39e-10 and-5.72e-9. No SDP optimality or exact gain follows
from these outputs, and the mismatch gain is not a global bound gain.

This modest diagnostic gain does not yet warrant a new exact certificate
grammar and corresponding continuous compilers. The probe exports an
explicitly uncompiled schema. extend_phase_fit.py rejects this schema;
none of these five-variable rows is a premise of any published checkpoint.
The unchanged ordinary deep43 separator separately passed exact PSD repair
and raised the39-row numerical cap to0.38061089350855515.

The deciding test was improvement of the fitted obstruction, rather than
the largest isolated violation. Existing trusted proof checkers are unchanged.

The new33-cell scan on the43-row profile found82 violated facets among4,452,096, max0.019298442268194993. A paired324-triangle SDP test increased actual mismatch from0.0007790304390793146 to0.0007805284697900705, gain1.4980307107559376e-6. Both statuses were optimal_inaccurate. This second small fitted gain defers the five-variable exact grammar and motivates the distinct active convex-profile experiment in CONVEX_RESPONSE_PLAN.md. The ordinary33 separator was exactly checked against the updated44-row profile, with gap0.00038302299710018655; the45-row LP cap0.3806113797136458 is an unfinished numerical value, not an optimum or a monotone bound improvement.
