import requests

def get_weather(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def fetch_weather(city_name):
    api_key = 'hbuigbiuhuibbuhb'  # Replace this with your OpenWeatherMap API key
    weather_data = get_weather(city_name, api_key)
    if weather_data["cod"] == "404":
        return "City not found. Please check the city name and try again."
    else:
        weather_description = weather_data["weather"][0]["description"]
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        return f"{city_name}: {weather_description}, {temperature}°C, Humidity: {humidity}%"

def main():
    city_name = input("Enter the city name: ")  # Prompt the user for the city name
    print("Fetching current weather for", city_name)
    weather_info = fetch_weather(city_name)
    print(weather_info)

if __name__ == "__main__":
    main()
