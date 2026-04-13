from pathlib import Path

from tools.validate import check_glossary, load_glossary

FIXTURES = Path(__file__).parent / "fixtures"


def test_glossary_loaded():
    g = load_glossary(FIXTURES / "test_glossary.json")
    assert "Coaster" in g
    assert g["Coaster"]["translation"] == "Hız Treni"


def test_glossary_term_used_correctly():
    g = load_glossary(FIXTURES / "test_glossary.json")
    warnings = check_glossary(
        key="K",
        source="The Coaster is fast",
        translation="Hız Treni hızlıdır",
        glossary=g,
    )
    assert warnings == []


def test_glossary_term_mistranslated():
    g = load_glossary(FIXTURES / "test_glossary.json")
    warnings = check_glossary(
        key="K",
        source="The Coaster is fast",
        translation="Lunapark treni hızlıdır",
        glossary=g,
    )
    assert len(warnings) == 1
    assert "Coaster" in warnings[0]
    assert "Hız Treni" in warnings[0]


def test_glossary_irrelevant_term_ignored():
    g = load_glossary(FIXTURES / "test_glossary.json")
    warnings = check_glossary(
        key="K",
        source="Hello world",
        translation="Merhaba dünya",
        glossary=g,
    )
    assert warnings == []
