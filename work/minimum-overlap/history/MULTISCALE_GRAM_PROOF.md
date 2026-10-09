# Compatible phase grids and a positive triangle expansion

Status: analytic identity and a discovery route. This is not a new global
minimum-overlap bound and is not a premise of the hybrid21 checkpoint.

Let L=dN, fine width a=2/L, and fine phase s uniform on[-a,0]. Let r_i(s)
be fine cell averages, extended by zero to indices outside0,...,L. A coarse
phase uniform on[-da,0] can be written s-j*a, where j is uniform on0,...,d-1
and independent of s. Its coarse cell averages are

    c_i(s,j)=(1/d)*sum_(k=id-j)^((i+1)d-j-1) r_k(s).

Writing B_j for this averaging matrix, the two phase-Gram matrices obey

    X_coarse=(1/d)*sum_j B_j*X_fine*B_j^T.

This uses the same arbitrary measurable density at both scales. Coarse
matrices chosen independently in a relaxation need not satisfy that identity.
The identity itself does not assume a step representation of the density.

For an interior coarse triangle0<i<k<l<N, the three fine blocks are disjoint
and each has d valid indices. For any allowed sign pattern(s,t,v), expanding
the multilinear products gives

    s*c_i*c_k+t*c_k*c_l+v*c_i*c_l
      = (1/d^3)*sum_(u in block_i,w in block_k,z in block_l)
          (s*r_u*r_w+t*r_w*r_z+v*r_u*r_z).

Averaging over the d phase offsets gives d^4 ordinary fine triangle rows,
each with weight1/d^4. Their weights sum exactly to1. Every fine triangle
has the existing universal RHS1, so the coarse row has the same RHS1. An
optimized nonnegative multiplier can therefore be serialized as a positive
rational combination of ordinary fine triangles. The existing exact compiler
then checks the resulting matrix and constant without a new inequality type.

This is useful for discovery because one aggregated constraint can represent
many fine triangles, while preserving the current exact certification path.
Only interior triples are expanded by this implementation. Endpoint triples
involve clipped blocks and are deliberately excluded from the expansion.
Discovery solver outputs remain proposals; any gain still needs PSD repair,
exact replay, continuous integration and complete mean coverage.
