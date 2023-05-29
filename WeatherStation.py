import requests

API_KEY = "af50c402cf620922e31f7747f5fa394a"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather_data(location):
    params = {
        "q": location,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data

def display_weather(data):
    if "name" in data:
        location = data["name"]
        country = data["sys"]["country"]
        temp_c = data["main"]["temp"]
        condition = data["weather"][0]["description"]

        print(f"Weather in {location}, {country}:")
        print(f"Temperature: {temp_c}°C")
        print(f"Condition: {condition}")
    else:
        print("Error: Unable to fetch weather data for the specified location.")

location = input("Enter a location: ")
weather_data = get_weather_data(location)
display_weather(weather_data)
