import pytest
from fuel import convert, gauge


def test_convert():
    # Test valid inputs
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/1") == 100

    # Test ValueError for non-integer input
    with pytest.raises(ValueError):
        convert("a/b")
    
    # Test ValueError for X > Y
    with pytest.raises(ValueError):
        convert("3/2")
    
    # Test ZeroDivisionError for Y = 0
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge():
    # Test gauge outputs
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(0) == "E"


# You can run the tests with `pytest test_fuel.py`
