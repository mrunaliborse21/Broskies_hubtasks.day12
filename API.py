import requests
import json

def get_weather(api_key, city):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    weather_data = response.json()

    if weather_data['cod'] == '404':
        print("City not found")
    else:
        main = weather_data['main']
        temperature = main['temp']
        humidity = main['humidity']
        weather_description = weather_data['weather'][0]['description']

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather_description}")

def main():
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"  # replace with your API key
    city = input("Enter the city name: ")
    get_weather(api_key, city)

if __name__ == "_main_":
    main()
