from app.cache import get, set

def test_cache_round_trip(tmp_path, monkeypatch):
    import app.cache as cache
    monkeypatch.setattr(cache, "CACHE_DIR", tmp_path)
    set("test", "key", {"ok": True})
    assert get("test", "key") == {"ok": True}
