import pytest
from working import convert  

def test_valid_time_conversion():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12:00 PM to 1:00 PM") == "12:00 to 13:00"

def test_invalid_minute_value():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    
def test_invalid_format():
    with pytest.raises(ValueError):
        convert("09:00 AM - 05:00 PM")  
    
    with pytest.raises(ValueError):
        convert("25:00 AM to 5:00 PM") 
     


