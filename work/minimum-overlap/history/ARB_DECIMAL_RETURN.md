# Decimal endpoints used by the exact mean return

The return checker parses the displayed midpoint and radius as exact
rational decimals, then uses midpoint plus radius as an upper endpoint.
It rejects malformed, nonfinite and unsupported representations. It does
not interpret the midpoint alone as a rigorous bound.

The reports call `arb.str(70)` with its default radius and formatting
options. In the pinned [python-flint 0.9.0 implementation](https://github.com/flintlib/python-flint/blob/0.9.0/src/flint/types/arb.pyx#L379),
those defaults pass zero flags to `arb_get_str`. The
[Arb string-conversion contract](https://arblib.org/arb.html#c.arb_get_str)
guarantees that default output can be read back as an enclosure containing
the original ball. Decimal conversion can enlarge the interval; the
printed radius accounts for that conversion. The corresponding
[FLINT discussion of binary and decimal output](https://flintlib.org/doc/using.html#binary-and-decimal)
distinguishes this enclosure format from approximate diagnostic printing.

The independent integer path supplies an exact rational denominator and
does not use this decimal serialization. Every promoted polynomial return
must pass that path as well as both Arb integration orders. These are
computer-assisted arithmetic dependencies, not proof-assistant validation.
