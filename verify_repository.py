"""Verify publication hashes and both unchanged checkpoint manifests."""
import hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((R/'MANIFEST.json').read_text())
for name,h in m.items():
    p=(R/name).resolve()
    assert p.is_relative_to(R) and p.is_file() and sha(p)==h,name
counts=[]
for folder,mf in [('minimum-overlap-hybrid106-radius-pypy627425-v1-checkpoint','manifest.json'),('minimum-overlap-refined14336-upper-checkpoint-v2','MANIFEST.json')]:
    d=R/'outputs'/folder;inner=json.loads((d/mf).read_text())
    for name,h in inner.items():assert sha(d/name)==h,(folder,name)
    counts.append(len(inner))
print(json.dumps({'status':'PASS','publication_files':len(m),'unchanged_checkpoint_files':counts,'scope':'file integrity; run reproduce.py for mathematical replays'}))
