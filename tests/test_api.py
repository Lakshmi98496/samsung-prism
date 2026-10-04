from fastapi.testclient import TestClient
from app.main import app

def test_http_contract(monkeypatch,tmp_path):
    monkeypatch.setenv('LLM_BASE_URL','')
    monkeypatch.setenv('CACHE_PATH',str(tmp_path/'cache.sqlite3'))
    with TestClient(app) as client:
        assert client.get('/health').json()['status']=='ok'
        assert client.get('/').status_code==200
        scenarios=client.get('/v1/scenarios').json()
        response=client.post('/v1/troubleshoot',json={'query':scenarios[0]['query']})
        assert response.status_code==200
        assert response.headers['content-type'].startswith('application/json')
        assert response.json()['response']['contexts']
        assert client.post('/v1/troubleshoot',json={'query':'x'}).status_code==422
        assert client.post('/v1/troubleshoot',json={'query':'Wi-Fi issue','siis_response':{'content':3}}).status_code==422
