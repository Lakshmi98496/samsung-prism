# Submission review

## Original PPT

The original deck covered the required problem, architecture, tools, innovation and team details. It was a proposal rather than evidence of a completed prototype: GitHub and model placeholders, empty result cells, unresolved Y/N checklist, unmeasured latency claims, a proposed BM25/dense stack, and an unperformed ablation comparison.

## What this project demonstrates

REST API, local browser demo, supplied schema validation, catalog-only URIs, source-exact extracted steps, critical-last ordering, SQLite cache, canonical synonym retrieval, fail-closed unknown queries, automated tests, and measured baseline engine latency. A two-stage local Qwen2.5-0.5B CPU smoke test is recorded in `docs/model_smoke.json`. Optional dense query retrieval remains untested.

## Remaining requirements and risks

- A portable local model service is configured in this workspace. The two-stage pipeline has one live smoke evaluation; general model quality remains unmeasured. Variations combine model output with templates.
- Offline extraction is a baseline: it can omit conditional instructions and group several screen destinations under one heading. It is unsuitable for autonomous device execution. One-action-one-screen quality still needs manual annotation and model evaluation.
- Supplied query/article pairs sometimes contain unrelated content. Dataset lookup follows organiser pairs; nonempty plans do not prove diagnostic correctness.
- The catalog links are masked placeholders and cannot demonstrate real on-device navigation.
- Baseline P95 measures engine-only time on this Windows machine. The live model smoke test exceeds the eight-second cold target. Cold LLM P95, unseen paraphrase hit rate and screen mapping accuracy remain unmeasured.
- Docker files are included. A Docker build has not been tested because Docker is unavailable here.
- Record/upload the actual demo, complete the organiser's AI disclosure with team sign-off, update final artifact references and create the required tag on the complete final commit.
- The team reports an extension to October 4, 2026. The provided brochure still shows the tentative September 25 deadline.
