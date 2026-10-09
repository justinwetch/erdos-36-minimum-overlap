"""Outward Arb integration with a fourth-order Taylor remainder.

Uses the pinned source's analytic term parser, antiderivative, and bin checker.
The interval range proof is separate: third-order jet plus a global bound on
the fourth derivative. Every final interval is still certified, regardless of
the floating root proposals. This accelerates certification; it changes no
mathematical target, input certificate, or necessary inequality.
"""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'deps'))
sys.path.insert(0,str(ROOT/'sources/lower-bound/certificate'))
import argparse,json,time
from decimal import Decimal,getcontext
from flint import arb,ctx
import prove_erdos_0380554275_arb as reference

def q_jet(terms,x):
    q=arb(1); q1=arb(0); q2=arb(0); q3=arb(0)
    for t in terms:
        lam=t.lam
        if lam==0: continue
        k=t.kind
        if k=='t': phi,phi1,phi2,phi3=x,arb(1),arb(0),arb(0)
        elif k=='-t': phi,phi1,phi2,phi3=-x,-arb(1),arb(0),arb(0)
        elif k=='t2': phi,phi1,phi2,phi3=x*x,2*x,arb(2),arb(0)
        elif k=='-t2': phi,phi1,phi2,phi3=-x*x,-2*x,-arb(2),arb(0)
        else:
            xi=t.xi
            s,c=(xi*x).sin_cos()
            if k=='cos': phi,phi1=c,-xi*s
            elif k=='-cos': phi,phi1=-c,xi*s
            elif k=='sin': phi,phi1=s,xi*c
            elif k=='-sin': phi,phi1=-s,-xi*c
            elif k=='cos+asin': phi,phi1=c+t.alpha*s,-xi*s+t.alpha*xi*c
            else: raise ValueError(k)
            phi2=-xi*xi*phi; phi3=-xi*xi*phi1
        q+=lam*(t.B-phi); q1-=lam*phi1; q2-=lam*phi2; q3-=lam*phi3
    return q,q1,q2,q3

def fourth_derivative_bound(terms):
    bound=arb(0)
    for t in terms:
        if t.kind in {'t','-t','t2','-t2'}: continue
        amplitude=arb(1)
        if t.kind=='cos+asin': amplitude=(1+t.alpha*t.alpha).sqrt().abs_upper()
        freq=t.xi.abs_upper()
        bound+=t.lam.abs_upper()*freq**4*amplitude
    return bound.upper()

def upper_integral_bin(cert,cell_width,root_pad,samples,max_nodes,rhs_inflate):
    terms,fterms,_,adjusted=reference.prepare_bin(cert,rhs_inflate)
    M4=fourth_derivative_bound(terms)
    roots=reference.speed_roots(fterms,samples)
    stack=reference.initial_intervals(roots,root_pad)
    total=arb(0); nodes=amb=pos=neg=0
    while stack:
        a_s,b_s=stack.pop(); aD,bD=Decimal(a_s),Decimal(b_s)
        if bD<=aD: continue
        nodes+=1
        if nodes>max_nodes: raise RuntimeError('max_nodes exceeded')
        a,b=arb(a_s),arb(b_s); c,r=(a+b)/2,(b-a)/2
        q,q1,q2,q3=q_jet(terms,c)
        radius=q1.abs_upper()*r+q2.abs_upper()*r*r/2+q3.abs_upper()*r**3/6+M4*r**4/24
        lower,upper=q-radius,q+radius
        if upper<=0: neg+=1; continue
        if lower>=0:
            total+=reference.pos_upper(reference.Q(terms,b)-reference.Q(terms,a)); pos+=1; continue
        if bD-aD<=cell_width:
            total+=(b-a)*reference.pos_upper(upper); amb+=1; continue
        mid=format((aD+bD)/2,'f')
        stack.append((mid,b_s)); stack.append((a_s,mid))
    return total,{'nodes':nodes,'ambiguous_cells':amb,'positive_cells':pos,'negative_cells':neg,
                  'speed_roots':len(roots),'rhs_adjusted':adjusted,'M4':M4.str(30)}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('certificate_json',type=Path)
    ap.add_argument('--target',required=True); ap.add_argument('--prec',type=int,default=160)
    ap.add_argument('--cell-width',default='0.00001'); ap.add_argument('--root-pad',type=float,default=1e-4)
    ap.add_argument('--samples',type=int,default=120001); ap.add_argument('--max-nodes',type=int,default=50000000)
    ap.add_argument('--rhs-inflate',default='1e-14'); ap.add_argument('--only-bins')
    ap.add_argument('--csv',type=Path); ap.add_argument('--json-report',type=Path)
    args=ap.parse_args(); ctx.prec=args.prec; getcontext().prec=80
    data=json.loads(args.certificate_json.read_text(),parse_float=str,parse_int=str)
    repaired=reference.repair_tiny_bin_gaps(data)
    bins=reference.parse_bins(args.only_bins,len(data['bins']))
    # Share analytic RHS recomputation and per-bin target tests with the pinned
    # reference implementation, replacing ONLY its interval range enclosure.
    original=reference.upper_integral_bin
    reference.upper_integral_bin=upper_integral_bin
    try:
        result=reference.verify(data,args.target,bins,args.cell_width,args.root_pad,args.samples,
                                args.max_nodes,args.rhs_inflate,args.csv)
    finally: reference.upper_integral_bin=original
    result.update({'taylor_order':4,'mean_gap_repairs':repaired,
                   'interval_proof':'third-order jet and global fourth-derivative remainder',
                   'analytic_reference_commit':(ROOT/'sources/lower-bound/commit.txt').read_text()})
    if args.json_report: args.json_report.write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in {'checked_bins','failures'}},indent=2),flush=True)
    if not result['proved_all_checked_bins']: raise SystemExit(1)

if __name__=='__main__': main()
