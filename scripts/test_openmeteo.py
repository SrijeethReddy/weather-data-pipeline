import requests
import json
from datetime import datetime, timedelta

def test_openmeteo_api():
    """
    Test the OpenMeteo API by fetching weather data for a specific location.
    """
    # API endpoint
    base_url = "https://api.open-meteo.com/v1/forecast"
    
    # Test parameters (New York City coordinates)
    params = {
        "latitude": 40.7128,
        "longitude": -74.0060,
        "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "timezone": "auto",
        "forecast_days": 1
    }
    
    try:
        # Make the API request
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse the response
        data = response.json()
        
        # Print some basic information
        print("API Test Successful!")
        print(f"Location: {data.get('latitude')}°N, {data.get('longitude')}°E")
        print(f"Timezone: {data.get('timezone')}")
        print("\nHourly data available for:")
        for key in data.get('hourly', {}).keys():
            print(f"- {key}")
            
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"Error testing OpenMeteo API: {e}")
        return False

if __name__ == "__main__":
    test_openmeteo_api() 