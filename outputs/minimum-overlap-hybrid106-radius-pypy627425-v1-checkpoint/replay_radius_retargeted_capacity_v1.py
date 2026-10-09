"""Execute a frozen physical-capacity proof in a fresh writable directory."""
import concurrent.futures,hashlib,json,os,subprocess,sys,time
from pathlib import Path
R=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    start=time.time();manifest=json.loads((R/'manifest.json').read_text());assert all((R/n).resolve().is_relative_to(R) and sha(R/n)==h for n,h in manifest.items())
    (R/'runs').mkdir();logs=R/'replay-logs';logs.mkdir();env=os.environ.copy();env['OPENBLAS_NUM_THREADS']='1';env['OMP_NUM_THREADS']='1';records=[]
    cfg=json.loads((R/'replay-config.json').read_text());cover=json.loads((R/cfg['capacity_cover_config']).read_text());bundle=json.loads((R/cover['bundle']).read_text())
    def execute(pair):
        label,cmd=pair;began=time.time()
        with (logs/(label+'.log')).open('w',encoding='utf-8') as f:p=subprocess.run([sys.executable,*cmd],cwd=R,env=env,stdout=f,stderr=subprocess.STDOUT)
        row={'label':label,'command':cmd,'returncode':p.returncode,'elapsed':time.time()-began};print(json.dumps(row),flush=True);assert p.returncode==0,label;return row
    wave=[('central-outer',['run_radius_retargeted_baselines_v1.py','baseline-cover-config.json','--name','replay-baselines']),('algebra-controls',['check_even_odd_capacity_controls_v2.py','--out','runs/replay-algebra-controls.json']),('quartet-controls',['check_odd_lipschitz_probe.py','--out','runs/replay-quartet-controls.json'])]
    for mode in ['arb','integer']:wave.append(('energy-'+mode,['verify_even_kernel_energy.py',bundle['kernel'],'--mode',mode,'--out',cover['energy_'+mode]]))
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:records.extend(pool.map(execute,wave))
    records.append(execute(('denominator-adapter',['adapt_even_central_reports.py',bundle['kernel'],'--central','central-certificate.json','--arb2',cfg['central_order2'],'--arb4',cfg['central_order4'],'--integer',cfg['central_integer'],'--out',cover['adapter']])))
    wave=[('capacity-'+mode,[cover.get('support_checkers',{}).get(mode,'verify_even_odd_capacity.py'),cover['bundle'],'--adapter',cover['adapter'],'--energy',cover['energy_'+mode],'--mode',mode,'--out',cover['support_'+mode]]) for mode in ['arb','integer']]
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:records.extend(pool.map(execute,wave))
    records.append(execute(('global-audit',['audit_radius_retargeted_capacity_v1.py','replay-config.json','--out','replay-global-audit.json'])))
    records.append(execute(('rejection-controls',['check_radius_retargeted_rejections_v1.py','replay-config.json','--name','fresh','--out','runs/replay-rejection-controls.json'])))
    audit=json.loads((R/'replay-global-audit.json').read_text());assert audit['status']=='PASS'
    baseline=json.loads((R/'runs/replay-baselines/execution.json').read_text());assert baseline['status']=='PASS' and len(baseline['records'])==6 and all(x['returncode']==0 for x in baseline['records'])
    for n in ['algebra','quartet','rejection']:assert json.loads((R/f'runs/replay-{n}-controls.json').read_text())['status']=='PASS'
    assert all(sha(R/n)==h for n,h in manifest.items()),'frozen input changed'
    result={'status':'PASS','scope':'fresh complete global proof using six central/outer executions, two energy checks, one adapter and two capacity checks, global audit and three executed control suites','target':audit['target'],'all_replay_commands':records,'certificate_check_invocations':11,'control_suites':3,'manifest_files':len(manifest),'manifest_sha256':sha(R/'manifest.json'),'replay_audit_sha256':sha(R/'replay-global-audit.json'),'elapsed':time.time()-start}
    (R/'replay-result.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result),flush=True)
if __name__=='__main__':main()
