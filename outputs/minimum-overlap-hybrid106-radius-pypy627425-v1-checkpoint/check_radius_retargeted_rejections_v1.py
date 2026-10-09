"""Execute malformed capacity witnesses and coverage controls on local copies."""
import argparse,copy,hashlib,json,os,subprocess,sys,time
from fractions import Fraction as F
from pathlib import Path
R=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('config',type=Path);ap.add_argument('--name',required=True);ap.add_argument('--out',required=True,type=Path);a=ap.parse_args();start=time.time()
    cfg=json.loads(a.config.read_text());coverpath=R/cfg['capacity_cover_config'];cover=json.loads(coverpath.read_text());bp=R/cover['bundle'];bundle=json.loads(bp.read_text());assert all(c.isalnum() or c in '-_' for c in a.name)
    root=R/'work'/('capacity-controls-'+a.name);root.mkdir(parents=True);records=[]
    inputs=[a.config,coverpath,bp,R/cover['adapter'],R/cover['energy_arb']];frozen={str(p):sha(p) for p in inputs};env=os.environ.copy();env['OPENBLAS_NUM_THREADS']='1'
    def execute(label,cmd,want,phrase=None):
        log=root/(label+'.log');out=root/(label+'.json');command=[sys.executable,*cmd,'--out',str(out)]
        with log.open('w',encoding='utf-8') as stream:p=subprocess.run(command,cwd=R,env=env,stdout=stream,stderr=subprocess.STDOUT)
        assert (p.returncode==0)==want,label
        if want:assert json.loads(out.read_text())['status']=='PASS'
        else:assert not out.exists() and phrase in log.read_text(encoding='utf-8'),label
        records.append({'label':label,'expected_pass':want,'returncode':p.returncode,'failure_gate':phrase,'command':command,'log_sha256':sha(log),'output_sha256':sha(out) if out.exists() else None});print(json.dumps(records[-1]),flush=True)
    for label in ['invalid-dual','unaligned-mesh','wrong-kernel-hash']:
        b=copy.deepcopy(bundle)
        if label=='invalid-dual':b['duals'][0]['k'][0]='1000001/1000000'
        elif label=='wrong-kernel-hash':b['kernel_sha256']='0'*64
        else:
            # Pick a true affine-kernel boundary, rather than an arbitrary grid point.
            from fractions import Fraction
            from circle_certificate import ctx
            from verify_hybrid_outer_blend import compile_blend
            ctx.prec=240;_,parts,_=compile_blend(json.loads((R/b['kernel']).read_text()));bounds=list(map(F,b['boundaries_exact']));required=set()
            for part in parts:
                for x in part[:2]:
                    for y in [x,-x,2-x,2+x]:
                        if 0<y<1:required.add(y)
            j=bounds.index(sorted(required)[len(required)//2]);del b['boundaries_exact'][j]
            for dual in b['duals']:del dual['k'][j];del dual['v'][j-1]
        p=root/(label+'-bundle.json');p.write_text(json.dumps(b,indent=2),encoding='utf-8')
        execute(label,['verify_even_odd_capacity.py',str(p),'--adapter',cover['adapter'],'--energy',cover['energy_arb'],'--mode','arb'],False,'capacity cells cross an affine-kernel breakpoint' if label=='unaligned-mesh' else 'AssertionError')
    delta=F(1,10**12);join=F(cover['intervals'][0]['hi']);assert join==F(cover['intervals'][1]['lo'])
    for label,want in [('gap-between-capacity-cases',False),('gap-after-central',False),('overlap-between-capacity-cases',True)]:
        c=copy.deepcopy(cover)
        if label=='gap-between-capacity-cases':c['intervals'][0]['hi']=str(join-delta)
        elif label=='gap-after-central':c['intervals'][0]['lo']=str(F(cfg['mean_abs_max'])+delta)
        else:c['intervals'][0]['hi']=str(join+delta)
        p=root/(label+'-cover.json');p.write_text(json.dumps(c,indent=2),encoding='utf-8');ac=dict(cfg,capacity_cover_config=str(p.relative_to(R)));q=root/(label+'-config.json');q.write_text(json.dumps(ac,indent=2),encoding='utf-8')
        execute(label,['audit_radius_retargeted_capacity_v1.py',str(q)],want,None if want else 'ValueError: uncovered mean interval')
    for label,change,phrase in [
        ('enlarged-central-return',{'mean_abs_max':str(F(cfg['central_check_mean_abs_max'])+F(1,10**8))},'invalid radius return'),
        ('wrong-executed-central-radius',{'central_check_mean_abs_max':str(F(cfg['central_check_mean_abs_max'])+F(1,10**8))},'central execution target/radius'),
        ('unproved-central-target',{'central_check_target':'1'},'central execution target/radius')]:
        ac=dict(cfg,**change);q=root/(label+'-config.json');q.write_text(json.dumps(ac,indent=2),encoding='utf-8')
        execute(label,['audit_radius_retargeted_capacity_v1.py',str(q)],False,phrase)
    assert all(sha(Path(p))==v for p,v in frozen.items())
    r={'status':'PASS','scope':'executed malformed dual, unaligned covariance mesh and changed kernel rejected; two exact coverage gaps rejected and an overlap accepted','records':records,'inputs':frozen,'implementation_hashes':{n:sha(R/n) for n in ['check_radius_retargeted_rejections_v1.py','audit_radius_retargeted_capacity_v1.py','verify_even_odd_capacity.py']},'elapsed':time.time()-start};a.out.write_text(json.dumps(r,indent=2),encoding='utf-8');print(json.dumps({'status':'PASS','controls':len(records),'elapsed':r['elapsed']}))
if __name__=='__main__':main()
