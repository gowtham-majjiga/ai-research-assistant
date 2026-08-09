from __future__ import annotations

from typing import Any
import requests


def search_wikipedia(query: str, limit: int = 5) -> list[dict[str, Any]]:
    response = requests.get(
        "https://en.wikipedia.org/w/api.php",
        params={
            "action": "query",
            "list": "search",
            "srsearch": query,
            "srlimit": limit,
            "format": "json",
        },
        timeout=10,
    )
    response.raise_for_status()
    items = response.json().get("query", {}).get("search", [])
    return [
        {
            "title": item["title"],
            "snippet": item.get("snippet", ""),
            "url": f"https://en.wikipedia.org/wiki/{item['title'].replace(' ', '_')}",
            "source": "Wikipedia",
        }
        for item in items
    ]


def search_arxiv(query: str, limit: int = 5) -> list[dict[str, Any]]:
    response = requests.get(
        "https://export.arxiv.org/api/query",
        params={"search_query": f"all:{query}", "start": 0, "max_results": limit},
        timeout=15,
    )
    response.raise_for_status()
    import xml.etree.ElementTree as ET
    root = ET.fromstring(response.text)
    ns = {"a": "http://www.w3.org/2005/Atom"}
    results = []
    for entry in root.findall("a:entry", ns):
        title = " ".join((entry.findtext("a:title", "", ns) or "").split())
        summary = " ".join((entry.findtext("a:summary", "", ns) or "").split())
        url = entry.findtext("a:id", "", ns) or ""
        results.append({"title": title, "snippet": summary, "url": url, "source": "arXiv"})
    return results
