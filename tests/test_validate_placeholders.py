from tools.validate import check_placeholders


def test_placeholder_preserved():
    errors = check_placeholders(
        key="UI_Score",
        source="Your score is {0}",
        translation="Puanın: {0}",
    )
    assert errors == []


def test_placeholder_missing_in_translation():
    errors = check_placeholders(
        key="UI_Score",
        source="Your score is {0}",
        translation="Puanın: ",
    )
    assert len(errors) == 1
    assert "{0}" in errors[0]


def test_extra_placeholder_in_translation():
    errors = check_placeholders(
        key="UI_Score",
        source="Your score",
        translation="Puanın: {0}",
    )
    assert len(errors) == 1


def test_printf_style_preserved():
    errors = check_placeholders(
        key="K",
        source="Got %d items",
        translation="%d öğe alındı",
    )
    assert errors == []


def test_printf_style_missing():
    errors = check_placeholders(
        key="K",
        source="Got %d items",
        translation="öğe alındı",
    )
    assert len(errors) == 1
    assert "%d" in errors[0]
