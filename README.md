# Lab 6 — Building the Knowledge Brain

**Generative AI & Prompt Engineering — A Mechanistic Approach**

Module 6: RAG & Embeddings | Duration: 90 minutes

---

## Overview

DevAssist hallucinates when asked about TaskFlow-specific details. In this lab you build a **mini-RAG pipeline** that grounds generation in actual project documentation.

1. **Part 1 (20 min):** Embedding exploration — semantic similarity heatmaps, keyword vs. semantic retrieval
2. **Part 2 (45 min):** Build RAG pipeline — chunk docs → embed → index in ChromaDB → retrieve → generate with citations
3. **Part 3 (15 min):** Hallucination evaluation — compare 5 questions with/without RAG

---

## Repository Structure

```
genai-lab6-rag-pipeline/
├── lab6_rag_pipeline.ipynb           # ← YOUR MAIN WORKSPACE
├── corpus/docs/                      # TaskFlow documentation (5 files)
│   ├── project_overview.md
│   ├── api_reference.md
│   ├── getting_started.md
│   ├── faq.md
│   └── changelog.md
├── utils/
│   ├── generation_utils.py
│   ├── chunking_utils.py             # chunk_by_paragraphs, chunk_by_sections, load_and_chunk_corpus
│   ├── embedding_utils.py            # cosine_similarity, plot_similarity_heatmap
│   └── retrieval_utils.py            # format_context, query_collection
├── tests/
│   ├── test_questions.json           # 10 questions with ground-truth answers
│   └── test_deliverables.py
├── data/
│   └── precomputed_outputs.json
└── rag_evaluation.md                 # ← YOUR DELIVERABLE
```

---

*Lab 6 of 8 — DevAssist / TaskFlow Lab Series*
