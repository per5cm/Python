import pytest
from working import convert  

def test_valid_time_conversion():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"

def test_invalid_minute_value():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    
def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")  
    
    with pytest.raises(ValueError):
        convert("25:00 AM to 5:00 PM") 
     


