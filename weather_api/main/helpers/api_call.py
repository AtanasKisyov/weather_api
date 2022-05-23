import requests


def get_weather_by_city_name(city_name):
    api_key = '391a353531319595c2deec6d7186de5d'  # This does not feel right...
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
    return requests.get(url).json()
