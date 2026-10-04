"""Local baseline benchmark: dataset coverage, contract gates, and engine latency."""
import json
import platform
import statistics
import sys
import tempfile
import os
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from app.engine import Engine,source_lines
from data.schema import ContextDeeplinkResponse

def run():
    os.environ['LLM_BASE_URL']=''
    with tempfile.TemporaryDirectory() as temp:
        engine=Engine(Path(temp)/'cache.sqlite3')
        latencies=[]
        valid=covered=0
        results=[]
        for row in engine.rows:
            result=engine.troubleshoot(row['original_query'])
            ContextDeeplinkResponse.model_validate(result['response'])
            engine.validate(result['response'],source_lines(row['siis_response']['content']))
            valid+=1
            covered+=bool(result['response']['contexts'])
            results.append({'id':row['id'],'cache_hit':result['meta']['cache_hit'],'source_id':result['meta']['source_id'],'actions':sum(len(c['actions']) for c in result['response']['contexts'])})
            for _ in range(10):
                latencies.append(engine.troubleshoot(row['original_query'])['meta']['latency_ms'])
        cold=[]
        for row in engine.rows:
            # Unique source keys force uncached extractive generation.
            content=row['siis_response']['content']+'\nBenchmark marker '+row['id']
            cold.append(engine.troubleshoot(row['original_query'],{'title':row['siis_response']['title'],'content':content})['meta']['latency_ms'])
        report={'mode':'offline-extractive','python':platform.python_version(),'platform':platform.platform(),'reference_queries':len(engine.rows),'schema_valid':valid,'nonempty_plans':covered,'url_leaks':0,'cached_engine_p95_ms':sorted(latencies)[int(.95*(len(latencies)-1))],'cached_engine_median_ms':statistics.median(latencies),'uncached_baseline_p95_ms':sorted(cold)[int(.95*(len(cold)-1))],'latency_scope':'Engine only; excludes HTTP/network, startup and model inference','llm_evaluated':False,'screen_mapping_accuracy':'Not independently annotated or measured','unseen_paraphrase_hit_rate':'Not measured','cases':results}
        engine.db.close()
    dest=Path('docs/benchmark.json')
    dest.write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='cases'},indent=2))

if __name__=='__main__':run()
