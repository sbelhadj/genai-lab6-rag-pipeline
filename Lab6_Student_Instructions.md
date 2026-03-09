# Lab 6 — Building the Knowledge Brain

## Student Instructions

**Module:** 6 — RAG & Embeddings | **Duration:** 90 min | **Pair programming**

---

## Context

DevAssist confidently answers questions about TaskFlow — but much of what it says is hallucinated. It was never trained on TaskFlow's documentation. In this lab you fix that by building a Retrieval-Augmented Generation pipeline that grounds answers in actual project docs.

---

## Lab Structure

| Phase | Time | Activity |
|-------|------|----------|
| Part 1: Embedding exploration | 20 min | Similarity heatmaps, keyword vs. semantic |
| Part 2: Build RAG pipeline | 45 min | Chunk → embed → index → retrieve → generate |
| Part 3: Hallucination evaluation | 15 min | 5 questions RAG vs. no-RAG |
| Wrap-up | 10 min | rag_evaluation.md |

---

## Deliverables

| # | What | Where |
|---|------|-------|
| 1 | Completed notebook | `lab6_rag_pipeline.ipynb` |
| 2 | RAG evaluation report | `rag_evaluation.md` |

---

## Evaluation Criteria

| Criterion | Weight |
|-----------|--------|
| Mechanistic understanding (parametric vs. non-parametric, attention over context) | 25% |
| Prompt quality (RAG prompt with contract framework + citations) | 25% |
| Evaluation & verification (5-question comparison, scoring rubric applied) | 20% |
| Software engineering (pipeline modularity, chunking strategy) | 20% |
| Responsibility & security (limitation awareness, hallucination analysis) | 10% |

---

*Lab 6 of 8 — DevAssist / TaskFlow Lab Series*
