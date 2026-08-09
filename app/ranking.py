from __future__ import annotations
import math
import re

STOPWORDS = {
    "the", "a", "an", "and", "or", "of", "to", "in", "for", "with",
    "on", "is", "are", "what", "how", "why", "from", "vs", "versus"
}

def _tokens(text: str) -> set[str]:
    return {
        token for token in re.findall(r"[a-z0-9]{2,}", text.lower())
        if token not in STOPWORDS
    }

def rank_results(query: str, results: list[dict]) -> list[dict]:
    query_terms = _tokens(query)
    scored = []

    for item in results:
        title_terms = _tokens(item.get("title", ""))
        body_terms = _tokens(item.get("snippet", ""))
        overlap = len(query_terms & (title_terms | body_terms))
        title_overlap = len(query_terms & title_terms)
        coverage = overlap / max(len(query_terms), 1)
        title_bonus = title_overlap * 1.5
        length_bonus = min(math.log1p(len(item.get("snippet", ""))) / 10, 0.5)
        source_bonus = 0.25 if item.get("source") == "arXiv" else 0.0

        score = round(coverage * 10 + title_bonus + length_bonus + source_bonus, 3)
        enriched = dict(item)
        enriched["score"] = score
        scored.append(enriched)

    return sorted(scored, key=lambda x: x["score"], reverse=True)

def deduplicate(results: list[dict]) -> list[dict]:
    seen = set()
    unique = []
    for item in results:
        key = item.get("url") or item.get("title", "").lower()
        if key not in seen:
            seen.add(key)
            unique.append(item)
    return unique
