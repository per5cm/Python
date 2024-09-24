import pytest
from um import count

def test_count_correct():
    assert count(r"um hello um there!") == 2
    assert count(r"UM HELLO UM THERE!") == 2

def test_count_incorrect():
    assert count(r"hello there!") == 0
    assert count(r"umbra") == 0