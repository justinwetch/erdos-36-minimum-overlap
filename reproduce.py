"""Replay selected proofs in fresh project-local directories."""
import argparse,os,shutil,subprocess,sys
from pathlib import Path
R=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('--part',choices=['lower','upper','all'],default='all');a=ap.parse_args()
subprocess.run([sys.executable,str(R/'verify_repository.py')],check=True)
env=os.environ.copy();env['OPENBLAS_NUM_THREADS']=env['OMP_NUM_THREADS']='1'
for part,folder in [('lower','minimum-overlap-hybrid106-radius-pypy627425-v1-checkpoint'),('upper','minimum-overlap-refined14336-upper-checkpoint-v2')]:
    if a.part not in [part,'all']:continue
    dst=R/'work'/('replay-'+part)
    if dst.exists():raise SystemExit('Preserve and move '+str(dst)+' before replaying again.')
    shutil.copytree(R/'outputs'/folder,dst)
    commands=[['REPLAY.py']] if part=='lower' else [['nonuniform.py','best.json','--out','replay-direct.json'],['exact_fractional_rotation.py','baseline.json','discovery.json','--name','replay-specialized'],['exact_packed_correlations.py','baseline.json','--out','replay-baseline.json'],['check_packed_correlations.py','--out','replay-packed-controls.json'],['check_exact_fractional_rotation.py','--out','replay-fractional-controls.json']]
    for command in commands:subprocess.run([sys.executable,*command],cwd=dst,env=env,check=True)
