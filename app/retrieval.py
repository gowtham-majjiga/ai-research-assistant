from __future__ import annotations
import html
import re
import xml.etree.ElementTree as ET
from typing import Any
import requests
from .cache import get, set

WIKI_URL = "https://en.wikipedia.org/w/api.php"
ARXIV_URL = "https://export.arxiv.org/api/query"
HEADERS = {"User-Agent": "AIResearchAssistant/1.0 (portfolio project)"}

def _clean(text: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(text or "")).strip()

def search_wikipedia(query: str, limit: int = 5) -> list[dict[str, Any]]:
    key = f"{query}|{limit}"
    cached = get("wikipedia", key)
    if cached is not None:
        return cached

    response = requests.get(
        WIKI_URL,
        params={
            "action": "query", "list": "search", "srsearch": query,
            "srlimit": limit, "format": "json", "utf8": 1,
        },
        headers=HEADERS,
        timeout=10,
    )
    response.raise_for_status()
    items = response.json().get("query", {}).get("search", [])
    results = [
        {
            "title": item["title"],
            "snippet": _clean(item.get("snippet", "")),
            "url": "https://en.wikipedia.org/wiki/" + item["title"].replace(" ", "_"),
            "source": "Wikipedia",
        }
        for item in items
    ]
    set("wikipedia", key, results)
    return results

def search_arxiv(query: str, limit: int = 5) -> list[dict[str, Any]]:
    key = f"{query}|{limit}"
    cached = get("arxiv", key)
    if cached is not None:
        return cached

    response = requests.get(
        ARXIV_URL,
        params={"search_query": f"all:{query}", "start": 0, "max_results": limit},
        headers=HEADERS,
        timeout=15,
    )
    response.raise_for_status()

    root = ET.fromstring(response.text)
    ns = {"a": "http://www.w3.org/2005/Atom"}
    results = []
    for entry in root.findall("a:entry", ns):
        title = _clean(entry.findtext("a:title", "", ns))
        summary = _clean(entry.findtext("a:summary", "", ns))
        url = entry.findtext("a:id", "", ns) or ""
        results.append({
            "title": title,
            "snippet": summary,
            "url": url,
            "source": "arXiv",
        })
    set("arxiv", key, results)
    return results
