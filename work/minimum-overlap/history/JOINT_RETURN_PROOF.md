# Returning a complete shared certificate

This is a proposal-generator correction. The trusted exact compiler,
continuous enclosures, integer verifier and promoted proof files are unchanged.

## Why an individual separation filter loses information

Each checked phase functional gives a universal linear inequality

    L_i(p) >= a_i.

A shared SDP produces a compatible collection of these inequalities at once.
An inequality can be satisfied at the old profile and become active after
the others change that profile. Its lack of individual separation is not
a reason to discard it from the returned relaxation.

A two-variable example makes this exact. Minimize x subject to x>=0,
x>=y-1 and y>=2. The old point (0,0) satisfies x>=y-1, so a filter that
retains only inequalities violated there removes it. The remaining problem
admits (0,2), while the complete problem requires x>=1. All constraints
were individually valid; the loss came from their selection.

Adding all checked inequalities cannot weaken the exact relaxation. This
statement does not guarantee monotonic numerical solver outputs or prove
optimality of a returned floating point solution.

## Actual campaign discriminator

The 43-grid functional returned with the 43/61/71 shared solve passed exact
integer PSD verification. Its SHA-256 is

    18e81c1e4af36396eeee0afeabdd453c46b2866e44b529b321eac661d6a1fe75.

At the old 59-row spectral profile its unnormalized separation gap is
negative, about -7.51994852055e-8. The earlier generator discarded it.
After adding the individually separating 61- and 71-grid functionals, the
new 61-row profile violates that discarded normalized row by the exact
positive quantity recorded in joint-return-excluded43-discriminator.json,
whose floating display is 0.0005329145732412795.

The comparison uses literal rational row coefficients and the stored
decimal profile values, not a floating sign test. It proves that the
discarded row can exclude the new proposed point. It does not by itself
prove a better objective or a global minimum-overlap bound.

The paired complete return retained all three checked inequalities and
raised the numerical cap from 0.38062673588654944 to 0.3806277785391543,
an increase of about 1.04265e-6. The same input proposals were used; the
three exact certificate hashes match the earlier separating-only return.
An unchanged continuous Arb4 mean-zero check then passed at
0.38062547852594978452320406596621004796. The actual 7168-cell witness
consistency checks also passed. A bounded root polish reached numerical
mean-zero 0.38062657283078494. The resulting global target
0.380623631 passed the original independent checks, complete mean-cover
audit and all eight fresh packaged replay commands. The 37 hash-bound
package inputs remained unchanged. This is a computer-assisted lower
bound, with no proof-assistant or global priority claim.

Five older discarded functionals were also restored and exactly rechecked.
All five already hold at the new 62-row profile. The resulting 67-row
numerical cap is 0.3806277759468096, about 2.6e-9 lower through numerical
variation. It provides no new improvement evidence. The 67-row portfolio
is preserved; the compact 62-row return remains the active research seed.

## Revised return obligation

certify_joint_phase_bundle.py now retains every exported functional that
passes the existing exact check and has nonzero lower bound. The nonzero
condition is required by the current extractor's row normalization.
--separating-only reproduces the old proposal-selection policy for a paired
comparison. The return records the policy, individual separation status,
retention status, certificate hashes and implementation hash.

Probe runs with uncompiled premises or suppressed exports are rejected.
No new premise is accepted by the trusted checker. A new global claim still
requires the continuous checks, actual-witness consistency, independent
integer integration, both outer implementations, complete mean coverage
audit and all fresh packaged replay commands.
