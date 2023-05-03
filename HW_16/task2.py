from multiprocessing import Process, Queue
import requests
import time


def weather_request(city, latitude, longitude, queue):
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

    for key, value in weather_result.items():
        print(f"Temperature in {key}: {value}")

    city_medium_in_process = {}
    for key, value in weather_result.items():  # medium temperature for each cities
        weather_medium = {key: sum(value) / len(value)}
        city_medium_in_process.update(weather_medium)

    queue.put(city_medium_in_process)

# ==== Main program


weather_result = {}
city_medium = {}

cities = {
    "Kyiv": ["50.45", "30.52"],
    "New York": ["40.71", "-74.01"],
    "London": ["51.51", "-0.13"],
    "Paris": ["48.85", "2.35"],
    "Tokyo": ["35.69", "139.69"],
}


def multiproc():
    processes = []
    q = Queue()
    for item in cities.items():
        p = Process(target=weather_request, args=(item[0], item[1][0], item[1][1], q))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    for _ in range(len(cities)):
        city_medium.update(q.get())

    hottest_city = list(sorted(city_medium.items(), key=lambda x: x[1], reverse=True))
    print(f"The hottest city is {hottest_city[0][0]}")


if __name__ == "__main__":
    start = time.time()
    multiproc()
    print(f"Program ended in {time.time() - start: .3f}")
