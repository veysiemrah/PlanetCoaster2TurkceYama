from pathlib import Path

import pytest

from tools.validate import validate_schema

FIXTURES = Path(__file__).parent / "fixtures"


def test_valid_translation_passes():
    errors = validate_schema(FIXTURES / "valid_translation.json")
    assert errors == []


def test_missing_source_field_fails():
    errors = validate_schema(FIXTURES / "invalid_missing_source.json")
    assert len(errors) == 1
    assert "source" in errors[0].message
    assert errors[0].key == "UI_Test_Key"


def test_missing_file_raises():
    with pytest.raises(FileNotFoundError):
        validate_schema(FIXTURES / "nonexistent.json")


def test_invalid_json_raises(tmp_path):
    bad = tmp_path / "bad.json"
    bad.write_text("{not valid json}", encoding="utf-8")
    with pytest.raises(ValueError):
        validate_schema(bad)
