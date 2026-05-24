import requests
from datetime import datetime

def weather_data(city):
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=fc8e03f0fed905b6415e95c302ebe553&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        # Extracting data
        city_name = data['name']
        country = data['sys']['country']

        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']

        weather = data['weather'][0]['main']
        description = data['weather'][0]['description']

        wind_speed = data['wind']['speed']

        sunrise = datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.fromtimestamp(data['sys']['sunset'])

        # Display data
        print("\n------ Weather Report ------")
        print(f"City        : {city_name}, {country}")
        print(f"Temperature : {temperature}°C")
        print(f"Feels Like  : {feels_like}°C")
        print(f"Condition   : {weather}")
        print(f"Description : {description}")
        print(f"Humidity    : {humidity}%")
        print(f"Pressure    : {pressure} hPa")
        print(f"Wind Speed  : {wind_speed} m/s")
        print(f"Sunrise     : {sunrise.strftime('%I:%M:%S %p')}")
        print(f"Sunset      : {sunset.strftime('%I:%M:%S %p')}")
        print("-----------------------------")

    except requests.exceptions.HTTPError:
        print("City not found!")
    
    except requests.exceptions.RequestException as e:
        print("Error:", e)

# User input
city = input("Enter city name: ")
weather_data(city)