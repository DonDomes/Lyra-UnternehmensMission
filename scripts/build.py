#!/usr/bin/env python3
"""Reproducible offline HTML build. Python standard library only."""
from pathlib import Path
import json,re,hashlib
ROOT=Path(__file__).resolve().parents[1]
MARKER='__LYRA_REWE1_MISSION_DATA_JSON__'
data=json.loads((ROOT/'src/rewe1-mission.json').read_text(encoding='utf-8'))
chapters=data['chapters']
tasks=[t for c in chapters for t in c['tasks']]
assert len(chapters)==9 and len(tasks)==72
assert len({t['id'] for t in tasks})==len(tasks)
assert sum(t['points'] for t in tasks)==352
assert all(t['explanation'] and t['solution'] is not None for t in tasks)
template=(ROOT/'src/mission-template.html').read_text(encoding='utf-8')
assert template.count(MARKER)==1
payload=json.dumps(data,ensure_ascii=False,indent=2).replace('</',r'<\/')
html=template.replace(MARKER,payload)
assert '<script id="mission-data" type="application/json">' in html
assert 'ProServa' not in html and 'ReWe5' not in html
out=ROOT/'dist/LYRA_UnternehmensMission_ReWe1_BueroWerk_SKR04_2026_v1.html'
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(html,encoding='utf-8')
print(json.dumps({'file':str(out.relative_to(ROOT)),'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'bytes':out.stat().st_size,'tasks':len(tasks)},ensure_ascii=False))
