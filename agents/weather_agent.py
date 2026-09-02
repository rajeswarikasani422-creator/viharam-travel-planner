import requests

def get_weather(destination, num_days):
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    geo_params = {"name": destination, "count": 1}

    try:
        geo_response = requests.get(geo_url, params=geo_params, timeout=10)
        geo_response.raise_for_status()
        geo_data = geo_response.json()

        if not geo_data.get("results"):
            return {
                "forecast": None,
                "source": "api",
                "error": f"Could not find location: {destination}"
            }

        lat = geo_data["results"][0]["latitude"]
        lon = geo_data["results"][0]["longitude"]

        weather_url = "https://api.open-meteo.com/v1/forecast"
        weather_params = {
            "latitude": lat,
            "longitude": lon,
            "daily": "temperature_2m_max,precipitation_probability_max",
            "timezone": "auto",
            "forecast_days": num_days
        }

        weather_response = requests.get(weather_url, params=weather_params, timeout=10)
        weather_response.raise_for_status()
        weather_data = weather_response.json()

        forecast = []
        for i in range(num_days):
            forecast.append({
                "day": i + 1,
                "temp_c": weather_data["daily"]["temperature_2m_max"][i],
                "rain_chance": weather_data["daily"]["precipitation_probability_max"][i]
            })

        return {
            "forecast": forecast,
            "source": "api"
        }

    except requests.exceptions.RequestException as e:
        return {
            "forecast": None,
            "source": "api",
            "error": f"Weather API request failed: {str(e)}"
        }