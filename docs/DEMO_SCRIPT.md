# Demo recording plan (under five minutes)

Start the API with `python -m uvicorn app.main:app --port 8000`. Open http://127.0.0.1:8000.

1. **0:00–0:35** Introduce The Semicolons, Theme 2 and the customer support problem. Explain that SIIS is the only source of instructions and the catalog contains masked evaluation URIs.
2. **0:35–1:35** Select a supplied touchscreen issue and generate its plan. Show source steps, categories, JSON, model mode and cache metadata. Explain the limitations of extractive grouping.
3. **1:35–2:05** Repeat the query. Show the cache hit and engine latency. Do not call this network latency.
4. **2:05–2:40** Ask an unrelated question, such as bread baking. Show the empty contexts and `no_match` fallback.
5. **2:40–3:20** Paste `## Connection\nTap Wi-Fi.\n## Restart\nRestart your phone.` as real multiline source text for a custom complaint. Show the source-grounded plan, then repeat it to show a hit. These are demo instructions, not verified advice for any specific device.
6. **3:20–4:10** Show `pytest -q` and `python scripts/benchmark.py`. State that this benchmark checks contract compliance and baseline latency, not clinical/device correctness or unseen paraphrase performance.
7. **4:10–4:50** Show the GitHub repository and explain the optional LLM configuration and remaining evaluation. If a model has been configured, include a genuine cold model request and identify the exact model. Never present offline results as LLM results.

Record the actual running application with your screen recorder. Upload to YouTube or Drive and ensure judges can access it. Put the final link in `submission/DEMO_LINK.md`, update the deck checklist, commit, and only then create the final release tag.
