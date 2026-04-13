from pathlib import Path

from tools.validate import compute_stats

FIXTURES = Path(__file__).parent / "fixtures"


def test_stats_single_file():
    stats = compute_stats([FIXTURES / "valid_translation.json"])
    assert stats["total"] == 1
    assert stats["translated"] == 1
    assert stats["untranslated"] == 0
    assert stats["needs_review"] == 0
    assert stats["percent"] == 100.0


def test_stats_mixed(tmp_path):
    mixed = tmp_path / "mixed.json"
    mixed.write_text(
        """
{
  "meta": {"language": "tr", "source_language": "en", "content_pack": "X",
           "game_version": "1.0", "last_updated": "2026-04-13"},
  "strings": {
    "a": {"source": "A", "translation": "a", "status": "translated"},
    "b": {"source": "B", "translation": "", "status": "untranslated"},
    "c": {"source": "C", "translation": "c", "status": "needs_review"},
    "d": {"source": "D", "translation": "", "status": "untranslated"}
  }
}
""",
        encoding="utf-8",
    )
    stats = compute_stats([mixed])
    assert stats["total"] == 4
    assert stats["translated"] == 1
    assert stats["untranslated"] == 2
    assert stats["needs_review"] == 1
    assert stats["percent"] == 25.0
