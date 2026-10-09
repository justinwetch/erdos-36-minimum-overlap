# Fractional circular cuts as a finite affine minimax

Let h=2/n and let a uniform density have heights f_0,...,f_(n-1). A circular
cut at a fraction v of the first cell has heights f_0,...,f_(n-1),f_0 and
edges0,h-vh,2h-vh,...,2-vh,2. Its first and last pieces have combined width h;
mass and box constraints are preserved exactly. Empty endpoint pieces at
v=0 or1 can be removed.

Every overlap breakpoint is a difference of density edges. On the positive
axis the complete families are m*h (m=0,...,n), m*h+v*h (m=0,...,n-1), and
m*h-v*h (m=1,...,n). Include their negatives. Between breakpoints the overlap
is affine in its shift, so its supremum occurs in these finite families.

At each labelled breakpoint, literal interval-pair intersection lengths are
piecewise affine in v. Their ordering changes only when members of the three
knot families coincide: within[0,1], this happens at0,1/2,1. Therefore every
labelled overlap value is affine separately on[0,1/2] and[1/2,1]. The supremum
is the maximum of these affine functions, hence convex on either half.

The three anchors are exact uniform-grid correlations: the original vector,
the half-cell vector[f_0,f_1,f_1,...,f_(n-1),f_(n-1),f_0], and its one-cell
rotation. For heights a_i/D, all anchor knot values have a common denominator
n*D^2. Original and one-cell anchor coefficients are twice their convolution
counts; half-cell coefficients are their convolution counts without a factor2.
PACKED_ARITHMETIC_PROOF.md supplies an exact carry-free convolution method.

Exact interpolation at a rational v gives every labelled knot value and thus
the continuum supremum. The discovery LP only chooses v; its optimality is not
a proof premise. Independent checks compare the specialized formulas against
literal interval intersections on small rational examples and against the
unchanged nonuniform all-shift checker for a promoted large witness.

The research scan currently considers only the two cells adjacent to the
selected integer origin. It does not prove optimality among all circular cuts.
