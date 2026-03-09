# Lab 6 — GitHub Classroom Guide

## Building the Knowledge Brain — Setup & Grading

---

## Template Repository

Name: `genai-lab6-rag-pipeline`

**Note:** sentence-transformers and ChromaDB are heavy (~2GB). The devcontainer installs them automatically. If students have issues, precomputed outputs are provided.

## Auto-Grading Tests (25 points)

| Test | Points |
|------|--------|
| Notebook + evaluation file exist | 5 |
| Notebook executed (≥5 cells) | 5 |
| Evaluation report not template | 5 |
| Corpus exists (≥4 md files) | 5 |
| Chunking produces ≥15 chunks | 5 |

## Manual Grading (75 points)

| Component | Points |
|-----------|--------|
| Embedding exploration + analysis | 15 |
| Working RAG pipeline | 20 |
| 5-question evaluation with rubric | 20 |
| rag_evaluation.md quality | 20 |

### Feedback Template

```markdown
## Lab 6 Feedback

**Auto-grading:** X/25
**Manual grading:** X/75

### Embeddings (Part 1)
- [ ] Similarity heatmap generated
- [ ] Keyword vs. semantic analysis insightful

### RAG Pipeline (Part 2)
- [ ] Chunking produces reasonable chunks
- [ ] ChromaDB indexed correctly
- [ ] RAG prompt uses contract framework
- [ ] Citations in generated answers

### Evaluation (Part 3)
- [ ] 5 questions scored with rubric
- [ ] Clear RAG vs. no-RAG comparison
- [ ] Mechanistic reflection references attention/context
```

---

*GitHub Classroom Guide — Lab 6 of 8*
