import threading
import requests
import time

weather_result = {}
city_medium = {}


def multi_thread():
    # result = [] # print response

    def weather_request(city, latitude, longitude):
        # print(f"Start of {city}")
        weather_resp = requests.get(
            url="https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": latitude,
                "longitude": longitude,
                "hourly": "temperature_2m",
                "forecast_days": 1
            }
        )
        temperature_list = weather_resp.json()["hourly"]["temperature_2m"]
        city_result = {city: temperature_list}
        weather_result.update(city_result)

        # result.append(weather_resp)  # print response

# ==== Main program
    start = time.time()
    threads = []
    cities = {
        "Kyiv": ["50.45", "30.52"],
        "New York": ["40.71", "-74.01"],
        "London": ["51.51", "-0.13"],
        "Paris": ["48.85", "2.35"],
        "Tokyo": ["35.69", "139.69"],
    }

    for item in cities.items():
        threads.append(threading.Thread(target=weather_request, args=(item[0], item[1][0], item[1][1])))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    # for item in result:  # print response
    #     print(item)

    end = time.time()
    print(f"Multi thread time is {end - start: .3f}")


if __name__ == "__main__":
    multi_thread()

for key, value in weather_result.items():
    print(f"Temperature in {key}: {value}")

for key, value in weather_result.items():  # medium temperature for each cities
    weather_medium = {key: sum(value)/len(value)}
    city_medium.update(weather_medium)

hottest_city = list(sorted(city_medium.items(), key=lambda x: x[1], reverse=True))

print(f"The hottest city is {hottest_city[0][0]}")
