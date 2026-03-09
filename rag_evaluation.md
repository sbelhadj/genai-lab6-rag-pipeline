# Lab 6 — RAG Evaluation Report

## RAG vs. No-RAG Hallucination Comparison

---

## Evaluation Table

| # | Question | RAG Accuracy | No-RAG Accuracy | RAG Grounded | No-RAG Grounded | RAG Citation | 
|---|----------|-------------|-----------------|-------------|-----------------|-------------|
| 1 | TODO | TODO/2 | TODO/2 | TODO/2 | TODO/2 | TODO/2 |
| 2 | TODO | TODO/2 | TODO/2 | TODO/2 | TODO/2 | TODO/2 |
| 3 | TODO | TODO/2 | TODO/2 | TODO/2 | TODO/2 | TODO/2 |
| 4 | TODO | TODO/2 | TODO/2 | TODO/2 | TODO/2 | TODO/2 |
| 5 | TODO | TODO/2 | TODO/2 | TODO/2 | TODO/2 | TODO/2 |
| **Total** | | TODO/10 | TODO/10 | TODO/10 | TODO/10 | TODO/10 |

## Scoring Rubric

- **Accuracy** (0-2): 0=wrong, 1=partial, 2=correct
- **Groundedness** (0-2): 0=hallucinated, 1=mixed, 2=fully grounded
- **Citation** (0-2): 0=none/wrong, 1=partial, 2=correct sources

---

## Analysis

### On how many questions did RAG improve factual accuracy?

TODO

### Where did RAG fail or underperform?

TODO (possible reasons: retrieval missed relevant chunk, model ignored context, question out of scope)

### How did the no-RAG model handle questions about TaskFlow-specific details?

TODO

### Were RAG citations accurate?

TODO

---

## Mechanistic Reflection

TODO: Explain why placing retrieved passages in the context window reduces hallucination. Use the terms "attention," "context," "token probability," and "parametric memory." Reference specific experiments from your workshop. (1 paragraph)

---

## Limitation Analysis

TODO: Describe one case where RAG failed. Explain why and propose one concrete improvement. (1 paragraph)

---

## System Design Sketch

TODO: How would you use RAG in the DevAssist capstone project? What documents would you index? How would you evaluate retrieval quality? (3-5 sentences)
