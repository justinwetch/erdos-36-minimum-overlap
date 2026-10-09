# Exact convolution with nonnegative polynomial coefficients

Let a_i,b_j be nonnegative integers. Every coefficient of their polynomial
product is at most H=min(len(a),len(b))*max(a)*max(b). Choose a byte width w
with2^(8w)>H. Evaluating both polynomials at B=2^(8w) and multiplying the two
integers gives their convolution coefficients as base-B digits. No carry is
possible because every product coefficient lies in[0,H]. Encoding and decoding
use explicit fixed-width little-endian byte chunks. Integer arithmetic is exact.

For a uniform density with heights a_i/D, convolving D-a_i with reversed a_i
gives every integer-lag overlap numerator. Multiplication by2/(n*D^2) supplies
the exact continuum knot values. Piecewise linearity between grid shifts and
zero support outside[-2,2] prove that their maximum is the continuum supremum.
Mass and box checks are separate prerequisites, checked before multiplication.

The implementation is a distinct exact summation method; it is not a new
mathematical inequality or an optimization guarantee. Small adversarial
coefficients and balanced witnesses are compared with direct summation. The
unchanged direct checker remains available for independent final replay.
