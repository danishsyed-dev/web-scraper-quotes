import requests

def get_weather(city_name):
    API_KEY = 'your_api_key'  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city_name + "&appid=" + API_KEY

    # Get the response
    response = requests.get(complete_url)
    data = response.json()

    # Check the response status code
    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        temperature = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        weather_description = weather["description"]

        weather_info = (
            f"City: {city_name}\n"
            f"Temperature: {temperature} K\n"
            f"Pressure: {pressure} hPa\n"
            f"Humidity: {humidity}%\n"
            f"Description: {weather_description}"
        )
    else:
        weather_info = f"City {city_name} not found."

    return weather_info

city = input("Enter city name: ")
print(get_weather(city))
