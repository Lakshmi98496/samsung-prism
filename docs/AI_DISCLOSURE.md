# AI usage disclosure draft

Team: The Semicolons  
Project: Smart Guided Troubleshooting Engine  
Institution: SRM Institute of Science and Technology, Chennai

AI used in development: **Yes**. Codex assisted with requirements inspection, Python API and demo implementation, test generation, documentation and presentation revisions. The team's original PPT supplied the concept and team details. The source troubleshooting dataset and deeplink catalog came from the organiser's archive.

Primary request: review the hackathon documents and original deck, build the Theme 2 project, improve the presentation, and prepare a GitHub submission.

Feature origin: API, extractive baseline, retrieval/cache, guard checks, optional model integration, demo page and automated tests: AI assisted. Team members must review and understand the implementation before submitting.

The runtime model is separate from AI assistance during development. The shipped baseline uses no model inference. A portable local Qwen2.5-0.5B Q4_K_M model through llama.cpp b11388 has been configured and smoke tested on one short source. Its results and limitations are recorded in `docs/model_smoke.json`. This does not establish general troubleshooting accuracy.

This is a factual draft for the organiser's `LangAI3.0_AI_Disclosure.docx`, not a signed declaration. Representative name, signature, date and the ethical attestations require the team's own review and sign-off.
