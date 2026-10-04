"""Live two-stage local model smoke evaluation (not a quality benchmark)."""
import json
import os
import tempfile
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from app.engine import Engine

os.environ['LLM_BASE_URL']='http://127.0.0.1:8081/v1'
os.environ['LLM_MODEL']='qwen2.5-0.5b'
os.environ['LLM_TIMEOUT_SECONDS']='60'
with tempfile.TemporaryDirectory() as temp:
    e=Engine(Path(temp)/'cache.sqlite3')
    query='My phone cannot connect to Wi-Fi. How do I check it?'
    source={'title':'Wi-Fi connection','content':'## Check Wi-Fi\nNavigate to Settings.\nTap Connections.\nTap Wi-Fi.\n## Restart Phone\nRestart your phone.'}
    result=e.troubleshoot(query,source)
    repeat=e.troubleshoot(query,source)
    report={'evaluation':'Live two-stage smoke test on one synthetic SIIS snippet, not device accuracy','runtime':'llama.cpp b11388 CPU','model':'Qwen2.5-0.5B-Instruct Q4_K_M','revision':'9217f5db79a29953eb74d5343926648285ec7e67','cold':result,'repeat':repeat}
    Path('docs/model_smoke.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(report,indent=2))
    e.db.close()
