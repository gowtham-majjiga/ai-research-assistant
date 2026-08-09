from app.ranking import deduplicate, rank_results

def test_deduplicate():
    items = [{"url": "a", "title": "A"}, {"url": "a", "title": "A duplicate"}]
    assert len(deduplicate(items)) == 1

def test_relevant_title_ranks_higher():
    items = [
        {"title": "Database systems", "snippet": "storage engines"},
        {"title": "Retrieval augmented generation", "snippet": "retrieval systems"},
    ]
    ranked = rank_results("retrieval generation", items)
    assert ranked[0]["title"] == "Retrieval augmented generation"
