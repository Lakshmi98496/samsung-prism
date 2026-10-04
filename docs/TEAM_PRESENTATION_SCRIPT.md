# Team presentation script

Use the same words in the PowerPoint speaker notes. Presentation roles do not claim who implemented each component. Aim for **4 minutes 45 seconds**, including the short live demo; rehearse with a timer. Speak naturally rather than reading every item on the slides.

| Presenter | Slides | Time | Focus |
| --- | --- | --- | --- |
| Vaibhavi Sharma | 1–3 | 0:00–1:05 | Introduction, problem and gap |
| Kottadi Lakshmi | 4–6 | 1:05–2:45 | Architecture, running demo and stack |
| Vivek Vaddipalli | 7–12 | 2:45–4:45 | Impact, results, limits and submission |

## Vaibhavi Sharma

### Slide 1 · Introduction · 20 seconds
“Hello everyone. We are The Semicolons from SRMIST, Chennai: Vaibhavi Sharma, Kottadi Lakshmi and Vivek Vaddipalli. Our Theme Two project is Smart Guided Troubleshooting. It converts a device complaint into structured guidance using the supplied SIIS reference and deeplink catalog.”

### Slide 2 · Problem · 25 seconds
“A customer describes a symptom, but a support agent still has to find the relevant article and organise its instructions. Our goal is to make that preparation easier. The prototype keeps the reference as the source of the steps, separates manual guidance from mapped actions, and places critical actions last.”

### Slide 3 · Existing solutions · 20 seconds
“An article gives an agent information, while a general model can generate an answer. Our approach adds explicit source selection, catalog checks and structured JSON. These are design distinctions, not measured competitor results. Lakshmi will explain how this works.”

## Kottadi Lakshmi

### Slide 4 · Architecture · 30 seconds
“The engine normalises the complaint and retrieves a reference. A valid cache hit returns the stored plan. For a model request, stage one selects source line IDs and stage two selects catalog IDs. Code reconstructs the source steps and checks mappings and the response schema. The offline baseline provides a reproducible path when a model endpoint is unavailable.”

### Slide 5 · Live demo · 45 seconds, including clicks
“Here is the actual dashboard. I select the supplied touchscreen scenario and generate a plan. We can inspect the source instructions and expand a confirmed catalog mapping. The URIs are masked evaluation placeholders; this demo does not execute phone actions. Repeating the complaint shows a cache hit. An unrelated bread-baking question returns no validated plan instead of invented troubleshooting.”

**Click sequence:** select `row_21 — Touchscreen issues on a smartphone or tablet` → **Generate plan** → expand one **Confirmed catalog mapping** → generate again → **Test an unknown issue** → generate. Show the actual execution-mode label; say **offline baseline** if that is what it shows. Switch back to slide 6. Do not wait for a cold local model request during this short demonstration.

### Slide 6 · Technology · 25 seconds
“We use Python, FastAPI, Pydantic and SQLite. Default retrieval uses TF-IDF with synonyms. The supplied dataset has twenty queries and five hundred seventy-eight catalog entries. We also tested one two-stage request with a local Qwen half-billion-parameter model through llama.cpp on CPU. Docker packaging is included but remains unverified. Vivek will cover the evidence and next steps.”

## Vivek Vaddipalli

### Slide 7 · Impact · 20 seconds
“Support agents can review an ordered plan and its mappings in one workspace. Repeated requests can reuse cached JSON without another inference call. These benefits motivate a support pilot, but we have not measured agent time savings or customer outcomes. Device integration is still needed for the masked destinations.”

### Slide 8 · Results and limits · 35 seconds
“All twenty supplied queries produced schema-valid, nonempty baseline responses, with zero web URL leaks in the steps. Cached engine P95 was zero point eight three three milliseconds; this excludes HTTP, startup and model inference. The recorded cold local model smoke request took nine point four three seconds, exceeding the eight-second target. Unseen paraphrase accuracy and exact-screen accuracy remain unmeasured. Source conditions and screen grouping also need further review.”

### Slide 9 · Roadmap · 20 seconds
“Next, we will review conditional context and screen grouping, evaluate the model across all supplied scenarios, and add unseen paraphrase tests. We then plan broader domain and scale testing. Ten thousand scenarios is a future target, not a demonstrated deployment.”

### Slide 10 · Reliability · 20 seconds
“Our distinguishing feature is the combination of source selection and code checks. The model chooses IDs rather than writing destination URIs. Invalid selections fail closed, and cache identity includes the source. Nine automated tests pass. A full model-versus-baseline ablation remains future work.”

### Slide 11 · Submission · 15 seconds
“The public repository includes the prototype, setup instructions, tests and this presentation. The video link is currently a placeholder. We will add the accessible recording link before the final release tag and complete the required disclosure signoff.”

### Slide 12 · Closing · 10 seconds
“Thank you. Our repository is linked on the slide. We welcome questions about source grounding, catalog matching and the evaluation plan.”

## Questions you may be asked

- **Is this a real LLM project?** There is a configurable two-stage model adapter and one genuine local Qwen smoke test. The default dashboard runs the tested offline baseline unless an endpoint is configured. General model quality needs more evaluation.
- **Can it open Settings on a phone?** It returns catalog destinations. The supplied URIs are masked; real device execution is outside this prototype.
- **Did you meet the latency target?** Cached offline engine latency is measured. The single cold local model request exceeded the eight-second target; cold model P95 has not been measured.
- **Is every step safe and complete?** Steps come from source text and critical actions appear last. Conditional context and one-screen grouping remain limitations, so a support/device review is needed.
- **Did you prove 80% unseen accuracy or 10k scale?** No. Those are evaluation goals, not achieved results.

Before recording, verify the current repository and slide statuses. Keep the total video under five minutes, avoid credentials on screen, and add the uploaded video URL to `submission/DEMO_LINK.md`.
