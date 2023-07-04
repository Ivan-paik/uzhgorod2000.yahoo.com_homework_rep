import requests

GEOCODING_API = "https://geocoding-api.open-meteo.com/v1/search"
METEO_API = "https://api.open-meteo.com/v1/forecast"

# city_name = "uzhhorod" # for test
city_name = input("Input city name here and press Enter: ")
res = requests.get(f"{GEOCODING_API}?name={city_name}&count=1&language=en&format=json")

if res.ok and res.json().get("results"):
    for item in res.json().get("results"):
        city_latitude = item.get('latitude')
        city_longitude = item.get('longitude')

    weather_resp = requests.get(
        url=METEO_API,
        params={
            "latitude": city_latitude,
            "longitude": city_longitude,
            "forecast_days": 0,
            "current_weather": True
            }
        )
    print(f"In {city_name} {weather_resp.json().get('current_weather').get('temperature')} °C")
else:
    print(f"{city_name} not found")
