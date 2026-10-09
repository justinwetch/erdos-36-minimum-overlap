# Exact compression of retained Gram premises

Status: established representation identity under the existing compiler;
one compressed candidate passed unchanged Arb4. This is not a new bound.

The full search retains many independently checked premises on the same
grid. For outer weights mu_j >= 0, combine their supported certificate
coefficients directly, without dividing by sum(mu_j). Give the resulting
premise outer multiplier one. Every compiler term is linear in its signed
functional weights, diagonal/nonnegative weights, mean multiplier and
circle/triangle multipliers. Therefore

    G_new = sum_j mu_j G_j,
    gamma_new = sum_j mu_j gamma_j,
    L_new(0) = sum_j mu_j L_j(0).

When eta_new > 0, set its mean-error constant to
sum(mu_j eta_j error_j)/eta_new. It is at least 1/12 because the old errors
are at least 1/12. When eta_new = 0 use 1/12, which contributes zero.
The mean-square coefficient is exactly the weighted old coefficient.
The restricted matrix is positive definite whenever the positive-weight
old restricted matrices are positive definite. The implementation also
checks the new matrix independently with the unchanged exact Bareiss test.

The affine hat kernel uses only gamma, so the complete hybrid Q(t), its
numerator for every allowed mean, and its positive-part integral are
unchanged. Exactly zero outer premises, zero cosine weights and all-zero
periodic families may be removed. No positive threshold or approximate
pruning is used. If a combined gamma is identically zero, retain the old
group because the existing functional compiler requires a nonzero gamma.
This fallback avoids extending the trusted grammar.

`compress_hybrid_functionals.py` checks the compiled full matrix and lower
constant against the exact weighted sum, and executes three rational toy
groups plus the zero-kernel fallback. These controls include signed gamma,
triangle/circle weights and different admissible mean-error constants.

Executed first compression: 48 retained premises -> 17 active combined
premises; 483 cosine slots -> 430 nonzero terms. All 17 restricted PSD
checks passed. Source SHA
37a06ab982cfffb2a8d7b572dbb6b893162e452667b9ca1b5fc777f6d39a07e3;
compressed SHA
79691b33a698f953c32597dc3f7b572e85c7e15d2d10e27c63a76a8b229a5ee7.
At mean radius .002919339345, unchanged Arb4 passed target .380609560
with lower ball .380609563374313499673046363967036688421662544168756367614,
matching the original displayed center. Run time 65.24 seconds. Concurrent
loads differ, so no speed comparison is inferred.

The terminal longer sparse pilot compressed from 48 premises to 10 and
483 cosine slots to 406 nonzero terms, with exact identities and PSD checks
passing in 17.61 seconds. Unchanged Arb4 passed mean-zero target .38061109
with lower ball .380611090573807134230146544577551942510273838478395299166
in 50.70 seconds on 2,810 pieces. This does not discharge global coverage.
Research warm starts should retain the uncompressed full-menu proposals:
the aggregated directions are equivalent as a certificate but give a
different optimization parameterization.

Run from the research directory using a fresh name:

    python compress_hybrid_functionals.py PATH_TO_PROPOSAL --name fresh-compression

Every proposed stronger bound still needs full outward and integer checks,
exact global mean coverage, and fresh packaged replay. The failed older
outer-source cover is unrelated to these identities and is preserved.
