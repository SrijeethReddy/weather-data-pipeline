import requests
import json
import os
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def load_config(config_path="configs/config.json"):
    """Load configuration from JSON file."""
    try:
        with open(config_path, "r") as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Failed to load config file: {e}")
        raise

def fetch_weather_data(base_url, city):
    """Fetch weather data for a given city from Open-Meteo API."""
    params = {
        "latitude": city["latitude"],
        "longitude": city["longitude"],
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m"
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        data["city"] = city["name"]  # Add city name to data for reference
        data["ingestion_time"] = datetime.utcnow().isoformat()  # Add ingestion timestamp
        logger.info(f"Successfully fetched data for {city['name']}")
        return data
    except requests.RequestException as e:
        logger.error(f"Failed to fetch data for {city['name']}: {e}")
        return None

def save_to_data_lake(data, output_path):
    """Save raw data to data lake (local file system)."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs(output_path, exist_ok=True)
    file_path = os.path.join(output_path, f"weather_raw_{timestamp}.json")
    
    try:
        with open(file_path, "w") as f:
            json.dump(data, f, indent=2)
        logger.info(f"Saved data to {file_path}")
    except Exception as e:
        logger.error(f"Failed to save data: {e}")

def ingest_weather_data():
    """Main function to ingest weather data for all cities."""
    config = load_config()
    base_url = config["api"]["base_url"]
    cities = config["cities"]
    output_path = config["data"]["raw_data_path"]
    
    all_data = []
    for city in cities:
        data = fetch_weather_data(base_url, city)
        if data:
            all_data.append(data)
    
    if all_data:
        save_to_data_lake(all_data, output_path)
    else:
        logger.warning("No data was fetched. Skipping save.")

if __name__ == "__main__":
    ingest_weather_data()