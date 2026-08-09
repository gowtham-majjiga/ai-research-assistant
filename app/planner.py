from __future__ import annotations
import re

ACADEMIC_TERMS = {
    "paper", "papers", "research", "study", "studies", "algorithm",
    "benchmark", "dataset", "model", "architecture", "survey"
}

def normalize_query(query: str) -> str:
    return " ".join(query.split()).strip()

def decompose_query(query: str) -> list[str]:
    cleaned = normalize_query(query)
    if not cleaned:
        return []
    # Explicit conjunctions become focused retrieval units.
    parts = re.split(r"\s+(?:and|vs\.?|versus|compared with|compare)\s+", cleaned, flags=re.I)
    parts = [p.strip(" .,;?") for p in parts if p.strip(" .,;?")]
    return parts[:4] or [cleaned]

def route_sources(query: str) -> list[str]:
    q = query.lower()
    if any(term in q for term in ACADEMIC_TERMS):
        return ["arxiv", "wikipedia"]
    return ["wikipedia", "arxiv"]
