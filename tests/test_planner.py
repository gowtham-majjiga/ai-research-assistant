from app.planner import decompose_query, route_sources

def test_decompose_query():
    assert decompose_query("retrieval vs fine-tuning") == ["retrieval", "fine-tuning"]

def test_academic_routing():
    assert route_sources("research paper on RAG")[0] == "arxiv"

def test_empty_query():
    assert decompose_query("   ") == []
