from __future__ import annotations

import re


def _tokens(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", text.lower()))


def rank_results(query: str, results: list[dict]) -> list[dict]:
    query_terms = _tokens(query)
    scored = []
    for item in results:
        text = f"{item.get('title', '')} {item.get('snippet', '')}"
        overlap = len(query_terms & _tokens(text))
        item = dict(item)
        item["score"] = overlap
        scored.append(item)
    return sorted(scored, key=lambda x: x["score"], reverse=True)
