"""Run existing central and outer checkers for a proposed blend cover."""
import argparse,concurrent.futures,hashlib,json,os,subprocess,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('cover',type=Path);ap.add_argument('--name',required=True);args=ap.parse_args();start=time.time()
    cfg=json.loads(args.cover.read_text());run=ROOT/'runs'/args.name;run.mkdir();target=cfg['target'];outer_target=cfg.get('outer_target',target);mean=cfg['central_mean_abs_max'];h=ROOT/cfg['hybrid_certificate'];o=ROOT/cfg['outer_certificate']
    commands=[('central2',['hybrid_certificate.py',str(h),'--mean-max',mean,'--target',target,'--order','2','--report',str(run/'central2.json')]),
              ('central4',['hybrid_certificate.py',str(h),'--mean-max',mean,'--target',target,'--order','4','--report',str(run/'central4.json')]),
              ('integer',['verify_integer_hybrid.py',str(h),'--mean',mean,'--target',target,'--out',str(run/'integer.json')]),
              ('mapping',['check_hybrid_mapping.py','--certificate',str(h),'--report',str(run/'mapping.json')]),
              ('outer4',['run_hybrid_outer.py',str(o),'--target',outer_target,'--name',args.name+'-outer-fourth','--only-bins',cfg['outer_bins_cli']]),
              ('outer2',['run_hybrid_outer.py',str(o),'--target',outer_target,'--name',args.name+'-outer-original','--original','--only-bins',cfg['outer_bins_cli']])]
    modulehashes={name:sha(ROOT/name) for name in ['hybrid_certificate.py','verify_integer_hybrid.py','check_hybrid_mapping.py','run_hybrid_outer.py','verify_fourth_order.py']}
    env=os.environ.copy();env['OPENBLAS_NUM_THREADS']='1';env['OMP_NUM_THREADS']='1'
    def execute(pair):
        label,cmd=pair;integer_python=os.environ.get('MINIMUM_OVERLAP_INTEGER_PYTHON',sys.executable)
        with (run/(label+'.log')).open('w',encoding='utf-8') as stream:r=subprocess.run([integer_python if label=='integer' else sys.executable,*cmd],cwd=ROOT,env=env,stdout=stream,stderr=subprocess.STDOUT)
        record={'label':label,'command':cmd,'returncode':r.returncode,'elapsed':time.time()-start,'interpreter':integer_python if label=='integer' else sys.executable,'interpreter_sha256':sha(Path(integer_python if label=='integer' else sys.executable))};print(json.dumps(record),flush=True);return record
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:records=list(pool.map(execute,commands))
    assert all(r['returncode']==0 for r in records),'baseline checker failed'
    assert all(sha(ROOT/n)==v for n,v in modulehashes.items()),'checker changed'
    result={'status':'PASS','scope':'central and outer cases only; transition-bin checks and exact global audit still required',
            'name':args.name,'cover_config_sha256':sha(args.cover),'hybrid_sha256':sha(h),'outer_sha256':sha(o),
            'checker_hashes':modulehashes,'records':records,'elapsed':time.time()-start}
    (run/'execution.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result),flush=True)
if __name__=='__main__':main()
