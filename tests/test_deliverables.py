"""Auto-grading: Lab 6 deliverable structure."""
import pytest, json, os

BASE = os.path.join(os.path.dirname(__file__), "..")

class TestFiles:
    def test_notebook(self):
        assert os.path.exists(os.path.join(BASE, "lab6_rag_pipeline.ipynb"))
    def test_evaluation(self):
        assert os.path.exists(os.path.join(BASE, "rag_evaluation.md"))

class TestNotebook:
    def test_valid(self):
        with open(os.path.join(BASE, "lab6_rag_pipeline.ipynb")) as f:
            nb = json.load(f)
        assert len(nb["cells"]) >= 20
    def test_executed(self):
        with open(os.path.join(BASE, "lab6_rag_pipeline.ipynb")) as f:
            nb = json.load(f)
        n = sum(1 for c in nb["cells"] if c.get("cell_type")=="code" and c.get("outputs"))
        assert n >= 5, f"Only {n} cells executed"

class TestEvaluation:
    def test_not_template(self):
        with open(os.path.join(BASE, "rag_evaluation.md")) as f:
            content = f.read()
        assert content.count("TODO") <= 5
    def test_has_mechanistic(self):
        with open(os.path.join(BASE, "rag_evaluation.md")) as f:
            content = f.read().lower()
        found = [t for t in ["attention","context","parametric","retrieval","hallucin"] if t in content]
        assert len(found) >= 2

class TestCorpus:
    def test_corpus_exists(self):
        docs = os.path.join(BASE, "corpus", "docs")
        assert os.path.isdir(docs)
        md_files = [f for f in os.listdir(docs) if f.endswith('.md')]
        assert len(md_files) >= 4

class TestChunking:
    def test_chunking_works(self):
        import sys
        sys.path.insert(0, BASE)
        from utils.chunking_utils import load_and_chunk_corpus
        chunks = load_and_chunk_corpus(os.path.join(BASE, "corpus", "docs"))
        assert len(chunks) >= 15, f"Only {len(chunks)} chunks"
