import pytest
from unittest.mock import patch
from project import load_api_key, get_lan_lon, get_current_weather, WeatherData

# Mock API Key
@pytest.fixture
def mock_api_key():
    return "mock_api_key"

# Mock function to simulate .env loading for API key
@patch("project.os.getenv")
def test_load_api_key(mock_getenv):
    mock_getenv.return_value = "mock_api_key"
    assert load_api_key() == "mock_api_key"

@patch("project.requests.get")
def test_get_lan_lon(mock_get, mock_api_key):
    mock_response = [
        {"lat": 37.7749, "lon": -122.4194}
    ]
    mock_get.return_value.json.return_value = mock_response

    lat, lon = get_lan_lon("San Francisco", "CA", "US", mock_api_key)
    assert lat == 37.7749
    assert lon == -122.4194

@patch("project.requests.get")
def test_get_current_weather(mock_get, mock_api_key):
    mock_response = {
        "weather": [
            {"main": "Clouds", "description": "overcast clouds", "icon": "04d"}
        ],
        "main": {"temp": 15}
    }
    mock_get.return_value.json.return_value = mock_response

    weather_data = get_current_weather(37.7749, -122.4194, mock_api_key)
    assert weather_data.main == "Clouds"
    assert weather_data.description == "overcast clouds"
    assert weather_data.icon == "04d"
    assert weather_data.temperature == 15
