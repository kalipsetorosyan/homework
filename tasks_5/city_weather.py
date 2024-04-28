import requests
import argparse


def get_city_data(city):
    try:
        api_token = "e4d6d1f0b51027b7f69dde004f4b4f31"
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': city,
            'appid': api_token,
            'units': 'metric'
        }
        # city
        responese = requests.get(url, params=params)
        data = responese.json()
    except Exception as ex:
        print(ex)
        print("check the city name")
    return data


def weather_info(data):
    print(f"Weather in {data['name']}:")
    print(f"Description: {data['weather'][0]['description']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Pressure: {data['main']['pressure']} hPa")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind Speed: {data['wind']['speed']} m/s")


def main():
    try:
        parser = argparse.ArgumentParser(description="Weather forecast program")
        parser.add_argument("city", help="Name of the city to get weather information for")
        parser.add_argument("--option", "-o", default="" ,choices=["temperature", "pressure", "humidity", "wind_speed"],
                            help="Weather information option to display")
        args = parser.parse_args()
        city = args.city
        option = args.option
        data = get_city_data(city)
        if option == "":
            print(weather_info(data))
        if option == "temperature":
            print(f"Weather in {data['name']}:")
            print(f"Temperature: {data['main']['temp']}°C")
        elif option == "pressure":
            print(f"Weather in {data['name']}:")
            print(f"Pressure: {data['main']['pressure']} hPa")
        elif option == "humidity":
            print(f"Weather in {data['name']}:")
            print(f"Humidity: {data['main']['humidity']}%")
        elif option == "wind_speed":
            print(f"Weather in {data['name']}:")
            print(f"Wind Speed: {data['wind']['speed']} m/s")
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    main()
