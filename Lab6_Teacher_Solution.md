# Lab 6 — Teacher Solution & Answer Key

## Building the Knowledge Brain — Instructor Copy

**CONFIDENTIAL**

---

## 1. Expected Embedding Results

- Auth query → auth chunk: ~0.78, token expiry chunk: ~0.65 (both relevant)
- Install query → install chunk: ~0.82
- Test query → pytest chunk: ~0.85
- "I can't log in" → auth chunk: ~0.52 (semantic match despite no keyword overlap)
- "I can't log in" → logging chunk: ~0.18 (low despite "log" keyword)

**Key insight:** Semantic retrieval handles paraphrasing; keyword matching would confuse "log in" with "logging."

---

## 2. Expected Chunk Count

- Section-based chunking: ~28 chunks across 5 docs
- Paragraph-based: ~35 chunks
- Both are acceptable strategies

---

## 3. RAG vs. No-RAG Expected Results

| Q | RAG Accuracy | No-RAG Accuracy |
|---|-------------|-----------------|
| Auth method | 2 (API key + X-API-Key) | 0-1 (generic OAuth/bearer) |
| Task states | 2 (5 exact states) | 0-1 (generic states) |
| Install | 2 (exact steps) | 0-1 (generic Python install) |
| Max body size | 2 (1MB + config) | 0 (hallucinated value) |
| Open→Done | 2 (no, must go through states) | 0-1 (may say yes) |

- RAG total: ~9-10/10 accuracy
- No-RAG total: ~1-4/10 accuracy
- No-RAG hallucinations: confident wrong answers about TaskFlow-specific details

---

## 4. Grading Notes

- **Part 1 (20%):** Heatmap quality + keyword/semantic analysis
- **Part 2 (40%):** Working pipeline (chunk → embed → index → retrieve → generate). If SBERT/ChromaDB unavailable, grade analysis of precomputed outputs.
- **Part 3 (25%):** Quality of 5-question evaluation using rubric. Students should identify specific hallucination patterns.
- **Evaluation report (15%):** Mechanistic reflection quality + limitation analysis
- Students who recognize "model may ignore context" show deep understanding
- Students who note "citations can be hallucinated even with RAG" show critical thinking

---

*CONFIDENTIAL — Lab 6 Teacher Solution*
