"""validate.py yasaklı terim ve argo kontrolleri için testler."""
from tools.validate import check_forbidden_terms, check_colloquial_terms


def test_forbidden_term_cekici_detected():
    errors = check_forbidden_terms("ride_title", "Bu çekici çok hızlı")
    assert len(errors) == 1
    assert "çekici" in errors[0]
    assert "Eğlence Birimi" in errors[0]


def test_forbidden_term_case_insensitive():
    errors = check_forbidden_terms("ride_title", "Bu Çekici açıldığında")
    assert len(errors) == 1


def test_forbidden_term_clean_translation():
    errors = check_forbidden_terms("ride_title", "Bu eğlence birimi çok hızlı")
    assert errors == []


def test_forbidden_misafir_detected():
    errors = check_forbidden_terms("guest_label", "Misafir sayısı: 5")
    assert len(errors) == 1
    assert "misafir" in errors[0].lower()
    assert "Ziyaretçi" in errors[0]


def test_colloquial_valla_detected():
    warnings = check_colloquial_terms("guest_thought_1", "Valla harika bir gün!")
    assert len(warnings) == 1
    assert "valla" in warnings[0]


def test_colloquial_yahu_detected():
    warnings = check_colloquial_terms("guest_thought_2", "Yahu ne oluyor bu parkta!")
    assert len(warnings) == 1
    assert "yahu" in warnings[0]


def test_colloquial_clean():
    warnings = check_colloquial_terms("guest_thought_3", "Harika bir gün geçirdim!")
    assert warnings == []


def test_colloquial_multiple_terms():
    warnings = check_colloquial_terms("x", "Valla yahu çok güzel!")
    assert len(warnings) == 2
