from __future__ import annotations
from .planner import decompose_query, route_sources
from .ranking import deduplicate, rank_results
from .retrieval import search_arxiv, search_wikipedia

def _retrieve(subquery: str, provider: str) -> list[dict]:
    if provider == "arxiv":
        return search_arxiv(subquery)
    return search_wikipedia(subquery)

def _build_summary(query: str, ranked: list[dict]) -> str:
    top = ranked[:5]
    if not top:
        return "No reliable public-source evidence was retrieved."
    lines = [
        f"Research question: **{query}**",
        "",
        "The system searched multiple public sources, removed duplicate results, "
        "and ranked documents by lexical relevance, title relevance, coverage, "
        "and source quality signals.",
        "",
        "**Top evidence:**",
    ]
    for item in top:
        snippet = item.get("snippet", "").strip()
        lines.append(f"- **{item['title']}** ({item['source']}): {snippet[:450]}")
    return "\n".join(lines)

def research(query: str, max_sources: int = 8) -> dict:
    subqueries = decompose_query(query)
    collected = []
    errors = []

    for subquery in subqueries:
        for provider in route_sources(subquery):
            try:
                collected.extend(_retrieve(subquery, provider))
            except Exception as exc:
                errors.append(f"{provider}: {type(exc).__name__}")

    ranked = rank_results(query, deduplicate(collected))[:max_sources]
    return {
        "query": query,
        "subqueries": subqueries,
        "sources": ranked,
        "errors": errors,
        "answer": _build_summary(query, ranked),
    }
