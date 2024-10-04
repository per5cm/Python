import pytest
from datetime import date
from seasons import Date

def test_calculate_minutes():
    test_date = Date(2000, 1, 1)
    current_date = date.today()
    delta = current_date - date(2000, 1, 1)
    expected_minutes = delta.days * 1440
    p = test_date.p
    expected_output = p.number_to_words(expected_minutes, andword="").capitalize()
    assert test_date.calculate_minutes() == expected_output



