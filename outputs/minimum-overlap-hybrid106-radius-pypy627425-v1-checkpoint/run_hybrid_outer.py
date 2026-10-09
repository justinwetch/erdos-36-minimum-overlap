"""Run an unchanged outer checker with input/output integrity attestation."""
import argparse,hashlib,json,os,subprocess,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('certificate',type=Path);ap.add_argument('--target',required=True);ap.add_argument('--name',required=True)
    ap.add_argument('--original',action='store_true');ap.add_argument('--only-bins',default='0-86,103-189');args=ap.parse_args();start=time.time()
    checker=ROOT/('sources/lower-bound/certificate/prove_erdos_0380554275_arb.py' if args.original else 'verify_fourth_order.py')
    paths=[args.certificate.resolve(),checker,ROOT/'sources/lower-bound/certificate/prove_erdos_0380554275_arb.py']
    before={str(p):sha(p) for p in paths};report=ROOT/f'runs/{args.name}.json';csv=ROOT/f'runs/{args.name}.csv';log=ROOT/f'runs/{args.name}.log'
    report.parent.mkdir(parents=True,exist_ok=True)
    cmd=[sys.executable,str(checker),str(args.certificate),'--target',args.target,'--only-bins',args.only_bins,'--cell-width','.00001',
        '--json-report',str(report),'--csv',str(csv)]
    env=os.environ.copy();env['PYTHONPATH']=str(ROOT/'deps')+os.pathsep+env.get('PYTHONPATH','');env['OPENBLAS_NUM_THREADS']='1'
    with log.open('w',encoding='utf-8') as stream:result=subprocess.run(cmd,stdout=stream,stderr=subprocess.STDOUT,env=env)
    after={str(p):sha(p) for p in paths};r=json.loads(report.read_text()) if report.exists() else {}
    passed=result.returncode==0 and before==after and r.get('proved_all_checked_bins') is True and not r.get('failures')
    out={'passed':passed,'returncode':result.returncode,'command':cmd,'input_hashes':before,'post_run_input_hashes':after,
        'output_hashes':{str(p):sha(p) for p in (report,csv,log) if p.exists()},'target':args.target,'original':args.original,'elapsed':time.time()-start}
    (ROOT/f'runs/{args.name}-attestation.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out,indent=2))
    if not passed:raise SystemExit(1)
if __name__=='__main__':main()
