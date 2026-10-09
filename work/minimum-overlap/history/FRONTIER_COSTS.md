# Observed frontier costs

observed computational costs on this shared machine; arithmetic gates are central-only until complete global promotion; no forecast or optimality claim.

| Kernel | Periodic cells | Original central integer seconds | Fresh global replay seconds | Promoted lower |
|---|---:|---:|---:|---:|
| hybrid87-capacity627060-v1 | 8192 | 1237.6 | 1643.0 | .380627060 |
| hybrid88-capacity627240-v1 | 16384 | 1472.1 | 1835.3 | .380627240 |
| hybrid89-capacity627340-v1 | 32768 | 1833.9 | 2331.7 | .380627340 |
| hybrid90-capacity627380-v1 | 65536 | 2557.2 | 2673.4 | .380627380 |
| hybrid91-capacity627410-v1 | 131072 | 3508.9 | 3709.8 | .380627410 |
| hybrid98-capacity627416-v1 | 131072 | 3178.4 | 3927.0 | .380627416 |
| hybrid99-capacity627417-v1 | 131072 | 2971.1 | 3972.2 | .380627417 |
| hybrid97-newrow-capacity627424-v1 | 131072 | 3108.5 | 4199.8 | .380627423 |

The source JSON records the precise central interval bounds, nodes,
piece counts and hashes. Timings share a machine with concurrent jobs;
they are measurements of these runs rather than controlled benchmarks.
The cell count alone does not predict cost: nearly flat regions require
many interval subdivisions. A new kernel must pay for both its original
checks and its full fresh replay before it can replace the incumbent.

H98 and H99 retest the same H91 131072-cell kernel with tighter targets
or a smaller central radius. H97 adds a new checked functional inequality
and changes the kernel. A transition-cover improvement alone cannot
exceed its same-kernel central return; further substantial gains need a
stronger kernel or a new valid realizability restriction.
