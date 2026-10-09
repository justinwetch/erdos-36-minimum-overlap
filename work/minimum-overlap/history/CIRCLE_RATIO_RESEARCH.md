# Rational-ratio periodic triangle discriminator

The universal periodic triangle inequalities are derived in CIRCLE_PROOF.md.
For integer positions (0,a,b), the existing certificate grammar supports

    q(bs)-q(as)-q((b-a)s)<=0,
    q(bs)+q(as)+q((b-a)s)<=2.

Averaging over any one grid cell gives an existing supported linear row.
probe_circle_ratios.py scans coprime a,b with 0<a<b/2, b<=32. On the
literal 4096-cell profile of the complete 70-row return it tested 322
families. The largest violation was about 0.0947959 for positions (0,3,7),
weights (1,-1,1), interval [2054/4096,2056/4096]. It selected this family
and (0,1,6), (0,1,26), (0,1,14), with the same weights.

Periodic prefix integration computes dilation averages; 51 independent
direct-sum fixtures passed with error below 1e-13. Eight exact binary
triangle fixtures also passed. These controls check the scanner, while
the universal inequality is the previously derived theorem.

The paired fine LP retained all 70 exact phase rows, the same Fourier
menu and the four original periodic scales. Adding the selected families
gave numerical cap 0.3806278949083227, versus 0.38062786621671774 before.
The solver returned Unknown; neither number is a certified optimum or an
original-problem upper bound. Maximum reported constraint defect was
1.82e-12. Exact extraction checked all row associations.

The raw continuous proposal had numerical mean-zero bound
0.3806246158656083; bounded sparse root polishing raised it to
0.3806265908251222 in 43.904 seconds. Its mean-square penalty was about
0.8087074996, giving only 0.380623289939211 at the promoted radius.
It does not improve the promoted global bound. The active coordinates
are retained in a union with the promoted candidate for a different
fixed-radius test. Large point violations alone did not predict a large
certificate gain. No new checker grammar or proof premise was introduced.
