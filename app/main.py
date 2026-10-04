from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

from app.engine import Engine


@asynccontextmanager
async def lifespan(application):
    application.state.engine = Engine()
    yield
    application.state.engine.db.close()


app = FastAPI(title='The Semicolons: Smart Guided Troubleshooting', version='1.0.0', lifespan=lifespan)


class Request(BaseModel):
    query: str = Field(min_length=3, max_length=2000)
    siis_response: str | dict[str, Any] | None = None


@app.get('/health')
def health():
    engine = app.state.engine
    return {'status':'ok', 'catalog_entries':len(engine.catalog), 'reference_queries':len(engine.rows), 'llm_configured':bool(engine.model.base), 'retrieval':'dense' if engine.dense is not None else 'tfidf-synonyms'}


@app.get('/v1/scenarios')
def scenarios():
    return [{'id':r['id'],'query':r['original_query'],'title':r['siis_response']['title']} for r in app.state.engine.rows]


@app.post('/v1/troubleshoot')
def troubleshoot(request: Request):
    if isinstance(request.siis_response,dict) and (not isinstance(request.siis_response.get('content'),str) or not isinstance(request.siis_response.get('title',''),str)):
        raise HTTPException(422,'siis_response requires string content and optional string title')
    if request.siis_response is not None and len(str(request.siis_response)) > 100000:
        raise HTTPException(413,'Source text exceeds 100000 characters')
    return app.state.engine.troubleshoot(request.query,request.siis_response)


@app.get('/',response_class=HTMLResponse)
def demo():
    return (Path(__file__).parent/'demo.html').read_text(encoding='utf-8')
