from app.engine import Engine

def test_two_stage_adapter_preserves_section_boundaries(tmp_path,monkeypatch):
    monkeypatch.setenv('LLM_BASE_URL','')
    engine=Engine(tmp_path/'cache.sqlite3')
    engine.model.base='http://mock.invalid/v1'
    calls=[]
    def fake(instructions,payload):
        calls.append(payload)
        if len(calls)==1:
            return {'technical_query':'Wi-Fi connection','query_variations':['wifi issue'],'groups':[{'name':'Invented title','line_ids':[1,2,4]},{'name':'Duplicate','line_ids':[1,2,4]}]}
        return {'mappings':[{'group_id':i,'catalog_id':None} for i in range(2)]}
    engine.model.complete=fake
    result=engine.troubleshoot('Wi-Fi connection',{'title':'Wi-Fi connection','content':'## Check Connection\nNavigate to Settings.\nTap Wi-Fi.\n## Restart Phone\nRestart your phone.'})
    assert len(calls)==2
    assert result['meta']['model']==engine.model.name
    actions=result['response']['contexts'][0]['actions']
    assert [a['actionName'] for a in actions]==['Check Connection','Restart Phone']
    assert len(actions)==2
    assert actions[-1]['category']=='critical'
    assert engine.troubleshoot('Wi-Fi connection',{'title':'Wi-Fi connection','content':'## Check Connection\nNavigate to Settings.\nTap Wi-Fi.\n## Restart Phone\nRestart your phone.'})['meta']['cache_hit']
    engine.db.close()
