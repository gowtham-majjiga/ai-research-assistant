from __future__ import annotations


def decompose_query(query: str) -> list[str]:
    """Create small retrieval-focused subqueries without requiring an LLM."""
    cleaned = " ".join(query.split())
    parts = [p.strip(" .") for p in cleaned.replace(" and ", ";").split(";") if p.strip()]
    return parts[:4] or [cleaned]


def route_sources(query: str) -> list[str]:
    academic_terms = ("paper", "research", "study", "algorithm", "benchmark", "model")
    return ["arxiv", "wikipedia"] if any(t in query.lower() for t in academic_terms) else ["wikipedia", "arxiv"]
