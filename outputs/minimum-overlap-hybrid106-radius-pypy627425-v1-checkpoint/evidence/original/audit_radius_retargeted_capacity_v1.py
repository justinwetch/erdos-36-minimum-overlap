"""Audit an exact full mean cover using physical odd-profile capacity returns."""
import argparse,csv,hashlib,json
from decimal import Decimal,getcontext
from fractions import Fraction as F
from pathlib import Path
from hybrid_functionals import validate
from retarget_central_mean_radius import retarget, controls as radius_controls
from verify_shared_mean_return import verify as verify_shared_return
ROOT=Path(__file__).resolve().parent;getcontext().prec=120
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def need(ok,message):
    if not ok:raise ValueError(message)
def full_cover(intervals):
    end=F(-1)
    for lo,hi in sorted(intervals):
        need(lo<=hi,'reversed interval');need(lo<=end,'uncovered mean interval');end=max(end,hi)
    need(end>=1,'uncovered right endpoint')

def checked_blends(config,central,hashes,target):
    from shared_mean_numerator import coefficients,minimum
    from verify_even_odd_capacity import sqrt_upper
    path=ROOT/config['capacity_cover_config'];cover=json.loads(path.read_text());hashes[str(path)]=sha(path)
    need(F(cover['target'])==target,'capacity cover target changed')
    bp=ROOT/cover['bundle'];bundle=json.loads(bp.read_text());hashes[str(bp)]=sha(bp)
    kp=ROOT/bundle['kernel'];kernel=json.loads(kp.read_text());hashes[str(kp)]=sha(kp)
    need(bundle['schema']=='even-odd-capacity-bundle-v1' and sha(kp)==bundle['kernel_sha256'],'capacity kernel changed')
    need(kernel['hybrid']==json.loads(central.read_text()) and F(kernel['theta_outer'])==0 and kernel['outer']['active']==[],'even central wrapper changed')
    ap=ROOT/cover['adapter'];adapter=json.loads(ap.read_text());hashes[str(ap)]=sha(ap)
    need(adapter['status']=='PASS' and adapter['wrapper_sha256']==sha(kp),'capacity denominator adapter')
    need(adapter['implementation_sha256']==sha(ROOT/'adapt_even_central_reports.py'),'adapter implementation changed')
    D=F(adapter['maximum_wrapped_denominator_exact']);poly,_=coefficients(kernel)
    need(list(map(str,poly))==adapter['polynomial_exact'] and D>0,'adapter polynomial or denominator')
    bounds=list(map(F,bundle['boundaries_exact']));h=[b-a for a,b in zip(bounds,bounds[1:])]
    need(bounds[0]==0 and bounds[-1]==1 and all(x>0 for x in h),'capacity mesh')
    reports=[]
    for mode in ['arb','integer']:
        ep=ROOT/cover['energy_'+mode];energy=json.loads(ep.read_text());rp=ROOT/cover['support_'+mode];r=json.loads(rp.read_text())
        for p in [ep,rp]:hashes[str(p)]=sha(p)
        need(energy['status']=='PASS' and energy['mode']==mode and energy['seed_sha256']==sha(kp),'energy report scope')
        checker=cover.get('support_checkers',{}).get(mode,'verify_even_odd_capacity.py')
        need(checker in ['verify_even_odd_capacity.py','verify_even_odd_capacity_v2.py'] and (mode=='integer' or checker=='verify_even_odd_capacity.py'),'unsupported capacity implementation')
        need(r['status']=='PASS' and r['mode']==mode and r['implementation_sha256']==sha(ROOT/checker),'capacity execution or implementation')
        if checker=='verify_even_odd_capacity_v2.py':
            need(r['primitive_backend']=='integer-block-recurrence' and r['primitive_grid']==bundle['uniform_grid'] and r['primitive_block']==64,'block primitive scope changed')
            need(r['bindings'].get(str((ROOT/'integer_block_primitive.py').resolve()))==sha(ROOT/'integer_block_primitive.py'),'block primitive dependency changed')
        need(r['bundle_sha256']==sha(bp) and r['kernel_sha256']==sha(kp) and r['cells']==len(h) and F(r['maximum_cell_width_exact'])==max(h),'capacity support scope')
        need(r['energy_upper_exact']==energy['energy_upper_exact'] and len(r['rows'])==len(bundle['duals']),'capacity energy or dual count')
        for n,v in energy['implementation_hashes'].items():need(sha(ROOT/n)==v,'energy dependency changed');hashes[str(ROOT/n)]=v
        for n,v in r['bindings'].items():need(sha(ROOT/n)==v,'capacity dependency changed');hashes[str(ROOT/n)]=v
        E=max(h)**2*sqrt_upper(F(energy['energy_upper_exact'])/120)
        for i,(dual,row) in enumerate(zip(bundle['duals'],r['rows'])):
            k=list(map(F,dual['k']));v=list(map(F,dual['v']));tau,kap=F(dual['tau']),F(dual['kappa'])
            need(len(k)==len(h) and len(v)==len(h)-1 and all(abs(x)<=1 for x in k),'invalid rational capacity dual')
            T=sum((abs(v[j])*(h[j]+h[j+1])/2 for j in range(len(v))),F(0))+abs(kap)*h[0]/2
            want=(poly[0]-T-E,poly[1]-tau,poly[2]);need(list(map(F,row['numerator_polynomial_exact']))==list(want),'capacity numerator assembly')
            need(row['index']==i and F(row['flow_cost_exact'])==T and F(row['covariance_error_upper_exact'])==E and F(row['tau_exact'])==tau,'capacity flow assembly')
            need(F(row['residual_l1_upper_exact'])>=0 and F(row['denominator_upper_exact'])==D+F(row['residual_l1_upper_exact']),'capacity residual assembly')
        reports.append(r)
    intervals=[];summaries=[]
    for entry in cover['intervals']:
        i=entry['dual_index'];lo,hi=F(entry['lo']),F(entry['hi']);need(type(i)==int and 0<=i<len(bundle['duals']) and 0<lo<=hi<=1,'capacity interval')
        returns=[]
        for r in reports:
            row=r['rows'][i];num,x=minimum(list(map(F,row['numerator_polynomial_exact'])),lo,hi);lower=num/F(row['denominator_upper_exact'])
            need(lower>target,'capacity exact interval return failed');returns.append({'mode':r['mode'],'lower_bound_exact':str(lower),'lower_bound_display':float(lower),'minimizing_mean_exact':str(x)})
        intervals.extend([(lo,hi),(-hi,-lo)]);summaries.append({'dual_index':i,'positive_mean_bin':[str(lo),str(hi)],'reflected_mean_bin':[str(-hi),str(-lo)],'returns':returns})
    need(intervals,'empty capacity cover')
    for n,v in adapter['bindings'].items():need(sha(ROOT/n)==v,'adapter graph changed');hashes[str(ROOT/n)]=v
    for n in ['verify_even_odd_capacity.py','verify_even_kernel_energy.py','adapt_even_central_reports.py','shared_mean_numerator.py','verify_shared_mean_return.py']:hashes[str(ROOT/n)]=sha(ROOT/n)
    return intervals,summaries

def main():
    ap=argparse.ArgumentParser();ap.add_argument('config',type=Path);ap.add_argument('--out',required=True,type=Path);args=ap.parse_args()
    config=json.loads(args.config.read_text());target=F(config['target']);central=Path(config['central_certificate']);outer=Path(config['outer_certificate'])
    data=json.loads(central.read_text());mean=F(config['mean_abs_max']);executed_mean=F(config['central_check_mean_abs_max']);base_target=F(config['central_check_target']);need(0<=mean<=executed_mean<=1,'invalid radius return');functions,premises=validate(data,executed_mean);radius_control=radius_controls();retargeted=[]
    outerdata=json.loads(outer.read_text(),parse_float=str)
    expected_indices=config.get('outer_indices',list(range(87))+list(range(103,190)))
    need(expected_indices==sorted(set(expected_indices)) and all(type(i)==int and 0<=i<len(outerdata['bins']) for i in expected_indices),'expected case indices')
    hashes={str(p):sha(p) for p in (central,outer,args.config)};orders=[]
    if 'cover_diagnostics' in config:
        cp=Path(config['cover_diagnostics']);cr=json.loads(cp.read_text())
        need(cr['status']=='PASS' and cr['checker_sha256']==sha(ROOT/'check_hybrid_cover.py') and cr['audit_checker_sha256']==sha(Path(__file__)),'coverage diagnostic changed')
        hashes[str(cp)]=sha(cp);hashes[str(ROOT/'check_hybrid_cover.py')]=cr['checker_sha256'];hashes[str(Path(__file__))]=cr['audit_checker_sha256']
    mapping=Path(config['mapping_report']);mr=json.loads(mapping.read_text())
    need(mr['status']=='PASS' and mr['certificate_sha256']==sha(central),'mapping fixtures failed or wrong input')
    need(mr['checker_sha256']==sha(ROOT/'check_hybrid_mapping.py'),'mapping checker changed');hashes[str(mapping)]=sha(mapping)
    hashes[str(ROOT/'check_hybrid_mapping.py')]=mr['checker_sha256']
    for name,h in mr['implementation_hashes'].items():need(sha(ROOT/name)==h,'mapping dependency changed');hashes[str(ROOT/name)]=h
    c=F(data['y2'])/2+sum((f['mu']*f['mean_coefficient'] for f in functions),F(0))
    for key,checker in [('central_order2','hybrid_certificate.py'),('central_order4','hybrid_certificate.py'),('central_integer','verify_integer_hybrid.py')]:
        p=Path(config[key]);r=json.loads(p.read_text());hashes[str(p)]=sha(p)
        need(r['passed'] and F(r['target'])>=base_target and F(r['mean_abs_max'])==executed_mean,'central execution target/radius')
        need(r['certificate_sha256']==sha(central) and r['checker_sha256']==sha(ROOT/checker),'central input or checker changed')
        need(F(r['mean_square_coefficient_exact'])==c and r['functional_premises']==premises,'functional assembly changed')
        for name,h in r['implementation_hashes'].items():need(sha(ROOT/name)==h,'central dependency changed: '+name);hashes[str(ROOT/name)]=h
        hashes[str(ROOT/checker)]=sha(ROOT/checker)
        mode='integer' if key=='central_integer' else 'arb'+str(r['order'])
        returned=retarget(r,mode,mean);need(F(returned['lower_bound_exact'])>target,'retargeted central return failed');retargeted.append(returned)
        if key!='central_integer':orders.append(r['order'])
    need(sorted(orders)==[2,4],'both Arb Taylor orders required')
    transition,blend_summaries=checked_blends(config,central,hashes,target)
    coverage=[];outer_counts=[]
    for key in ('outer_fourth','outer_original'):
        attpath=Path(config[key]);att=json.loads(attpath.read_text());hashes[str(attpath)]=sha(attpath)
        need(att['passed'] and att['returncode']==0 and F(att['target'])>=target,'outer execution failed')
        need(att['input_hashes']==att['post_run_input_hashes'],'input changed during outer execution')
        need(att['input_hashes'].get(str(outer.resolve()))==sha(outer),'outer certificate changed')
        need(att['original']==(key=='outer_original'),'outer implementation flag')
        for name,h in {**att['input_hashes'],**att['output_hashes']}.items():need(sha(Path(name))==h,'outer dependency or output changed');hashes[name]=h
        cmd=att['command'];report=Path(cmd[cmd.index('--json-report')+1]);csvpath=Path(cmd[cmd.index('--csv')+1])
        expected=ROOT/('sources/lower-bound/certificate/prove_erdos_0380554275_arb.py' if key=='outer_original' else 'verify_fourth_order.py')
        need(Path(cmd[1]).resolve()==expected.resolve(),'wrong outer checker command')
        r=json.loads(report.read_text());rows=list(csv.DictReader(csvpath.open()));indices=r['checked_bins']
        if key=='outer_fourth':need(r.get('taylor_order')==4,'fourth-order outer report required')
        need(r['proved_all_checked_bins'] and not r['failures'] and F(r['target'])>=target,'outer report failed')
        need(indices==expected_indices and len(rows)==len(expected_indices),'outer indices')
        need([int(row['bin_index']) for row in rows]==indices and all(row['proved']=='True' for row in rows),'outer CSV results')
        previous=Decimal('-1');intervals=[]
        for i,b in enumerate(outerdata['bins']):
            lo,hi=Decimal(str(b['lo'])),Decimal(str(b['hi']))
            if lo>previous and lo-previous<=Decimal('1e-12'):lo=previous
            previous=max(previous,hi)
            if i not in indices:continue
            row=rows[indices.index(i)];need(Decimal(row['lo'])==lo and Decimal(row['hi'])==hi,'outer endpoints differ')
            need(lo.is_finite() and hi.is_finite() and lo<=hi,'invalid endpoints');intervals.append((F(lo),F(hi)))
        intervals.append((-mean,mean));intervals.extend(transition);full_cover(intervals);coverage.append(intervals);outer_counts.append(len(indices))
    need(coverage[0]==coverage[1],'outer covers differ')
    hashes[str(Path(__file__))]=sha(Path(__file__));hashes[str(ROOT/'retarget_central_mean_radius.py')]=sha(ROOT/'retarget_central_mean_radius.py')
    result={'status':'PASS','target':config['target'],'full_mean_cover':'[-1,1]','central_mean_abs_max':str(mean),'central_orders':orders,
        'outer_bins_each':outer_counts,'outer_indices':expected_indices,'embedded_functionals':len(functions),'mean_square_coefficient_exact':str(c),
        'scope':'global exact mean cover with a narrower-radius deduction from executed fixed-kernel central enclosures and independently checked physical capacity; all integral checkers unchanged','retargeted_central_returns':retargeted,'radius_return_controls':radius_control,'executed_central_mean_abs_max':str(executed_mean),
        'blend_bins_each_side':len(blend_summaries),'blend_summaries':blend_summaries,
        'reflection_premise':'h_ref(x)=h(2-x) is admissible and has p_ref(t)=p(-t), preserving the peak and reversing the mean',
        'checker_sha256':sha(Path(__file__)),'hashes':hashes}
    args.out.write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
