import json
import pytest
from app.engine import Engine, WEB, source_lines
from data.schema import ContextDeeplinkResponse

@pytest.fixture
def engine(tmp_path,monkeypatch):
    monkeypatch.setenv('LLM_BASE_URL','')
    e=Engine(tmp_path/'cache.sqlite3')
    yield e
    e.db.close()

def test_all_supplied_queries_are_grounded(engine):
    for row in engine.rows:
        result=engine.troubleshoot(row['original_query'])
        ContextDeeplinkResponse.model_validate(result['response'])
        assert result['meta']['cache_hit']
        assert result['response']['contexts'], row['id']
        engine.validate(result['response'],source_lines(row['siis_response']['content']))

def test_unknown_is_not_given_a_device_plan(engine):
    result=engine.troubleshoot('How do I make sourdough bread in my oven?')
    assert result['response']['contexts']==[]
    assert result['meta']['fallback']=='no_match'

def test_source_urls_removed_and_cache_is_source_specific(engine):
    query='Wi-Fi trouble'
    a=engine.troubleshoot(query,'## Wi-Fi\nGo to Settings.\nTap Wi-Fi.\nVisit https://example.com/support for more.')
    b=engine.troubleshoot(query,'## Wi-Fi\nPress the Power button for 20 seconds.')
    assert a['response']!=b['response']
    assert not WEB.search(json.dumps(a['response']))

def test_critical_steps_last_and_manual_has_no_link(engine):
    result=engine.troubleshoot('Fix screen','## Restart\nRestart your phone.\n## Connection\nTap Wi-Fi.\n## Service\nContact the service center.')
    actions=result['response']['contexts'][0]['actions']
    assert actions[-1]['category']=='critical'
    manual=next(a for a in actions if a['actionName']=='Service')
    assert manual['stepGroups'][0]['actionableDeeplink'] is None

def test_invalid_llm_source_ids_fail_closed(engine):
    engine.model.base='http://mock.invalid/v1'
    engine.model.complete=lambda *a: {'groups':[{'name':'Fabricated','line_ids':[999999]}]}
    result=engine.troubleshoot('custom query','Tap Display.\nTap Brightness.')
    assert result['response']['contexts']==[]
    assert result['meta']['fallback']=='generation_failed'

def test_cache_returns_independent_objects(engine):
    row=engine.rows[0]
    result=engine.troubleshoot(row['original_query'])
    result['response']['contexts'].clear()
    assert engine.troubleshoot(row['original_query'])['response']['contexts']

def test_mapping_does_not_confuse_buttons_and_highlight_buttons(engine):
    link,_=engine.map_link('Full screen gestures',['Go to Settings, tap Display, and then tap Navigation bar.','Select Buttons to turn off full screen gestures.'])
    assert link['deeplink']==next(d['deeplink'] for d in engine.catalog if d['id']=='DL-0169')
    wifi,_=engine.map_link('Wi-Fi',['Tap Wi-Fi.'])
    assert wifi['deeplink']==next(d['deeplink'] for d in engine.catalog if d['id']=='DL-0313')
