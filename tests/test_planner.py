from app.planner import decompose_query, route_sources


def test_decompose_query_returns_query_parts():
    parts = decompose_query("retrieval and ranking")
    assert parts == ["retrieval", "ranking"]


def test_academic_queries_prioritize_arxiv():
    assert route_sources("research paper on RAG")[0] == "arxiv"
