import pytest
from numb3rs import validate

def test_validate_ip():
    assert validate(r"127.0.0.1") == True
    assert validate(r"255.255.255.255") == True

def test_validate_range():
    assert validate(r"cat") == False
    assert validate(r"512.512.512.512") == False
    assert validate(r"1.2.3.1000") == False
    assert validate(r"1.512.1.1") == False


