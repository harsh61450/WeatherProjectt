import requests

def get_weather(city):
    api_key = "3ecf1ccb6ce11dc58ac571db04afaf1e"  # replace with your actual API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        if data["cod"] != "404":
            main = data["main"]
            weather_desc = data["weather"][0]["description"]
            temp = main["temp"]
            humidity = main["humidity"]
            wind_speed = data["wind"]["speed"]

            return (f"City: {city}\n"
                    f"Temperature: {temp}°C\n"
                    f"Weather: {weather_desc}\n"
                    f"Humidity: {humidity}%\n"
                    f"Wind Speed: {wind_speed} m/s")
        else:
            return "City not found."
    except Exception as e:
        return "Error retrieving weather data."

if __name__ == "__main__":
    city = input("Enter city name: ")
    weather_info = get_weather(city)
    print(weather_info)
