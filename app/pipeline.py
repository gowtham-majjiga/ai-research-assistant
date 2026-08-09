from __future__ import annotations

from .planner import decompose_query, route_sources
from .ranking import rank_results
from .retrieval import search_arxiv, search_wikipedia


def research(query: str) -> dict:
    collected = []
    for subquery in decompose_query(query):
        for source in route_sources(subquery):
            try:
                if source == "arxiv":
                    collected.extend(search_arxiv(subquery))
                else:
                    collected.extend(search_wikipedia(subquery))
            except Exception:
                # One unavailable source should not break the complete workflow.
                continue

    ranked = rank_results(query, collected)[:8]
    if not ranked:
        return {"answer": "No sources were retrieved. Try a more specific question.", "sources": []}

    evidence = "\n".join(
        f"- {item['title']} ({item['source']}): {item.get('snippet', '')[:500]}"
        for item in ranked[:5]
    )
    answer = (
        f"Research results for: **{query}**\n\n"
        "The assistant retrieved and ranked evidence from multiple public sources. "
        "The strongest retrieved evidence is summarized below.\n\n"
        + evidence
    )
    return {"answer": answer, "sources": ranked}
