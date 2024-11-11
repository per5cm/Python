from unittest.mock import patch, MagicMock
from project import load_api_key, get_lan_lon, get_current_weather 

def test_load_api_key(monkeypatch):
    # Test successful loading of API key
    monkeypatch.setenv("API_KEY", "test_api_key")
    api_key = load_api_key()
    assert api_key == "test_api_key"

@patch("requests.get")
def test_get_lan_lon(mock_get):
    # Mock response for geolocation
    mock_response = MagicMock()
    mock_response.json.return_value = [{"lat": 34.0522, "lon": -118.2437}]
    mock_get.return_value = mock_response

    lat, lon = get_lan_lon("Los Angeles", "CA", "US", "test_api_key")
    assert lat == 34.0522
    assert lon == -118.2437
    mock_get.assert_called_once_with(
        "http://api.openweathermap.org/geo/1.0/direct?q=Los Angeles,CA,US&appid=test_api_key"
    )


@patch("requests.get")
def test_get_current_weather(mock_get):
    # Mock response for current weather
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "weather": [{"main": "Clear", "description": "clear sky", "icon": "01d"}],
        "main": {"temp": 25}
    }
    mock_get.return_value = mock_response

    weather_data = get_current_weather(34.0522, -118.2437, "test_api_key")
    assert weather_data.main == "Clear"
    assert weather_data.description == "clear sky"
    assert weather_data.icon == "01d"
    assert weather_data.temperature == 25
    mock_get.assert_called_once_with(
        "https://api.openweathermap.org/data/2.5/weather?lat=34.0522&lon=-118.2437&appid=test_api_key&units=metric"
    )


