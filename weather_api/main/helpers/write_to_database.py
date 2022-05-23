from weather_api.main.models import Temperature, City


def write_temperature_to_database(city, city_id):

    temperature = city['main']['temp']
    minimum_temperature = city['main']['temp_min']
    maximum_temperature = city['main']['temp_max']
    pressure = city['main']['pressure']
    humidity = city['main']['humidity']
    wind_speed = city['wind']['speed']

    temperature_info = Temperature(
        temperature=temperature,
        minimum_temperature=minimum_temperature,
        maximum_temperature=maximum_temperature,
        pressure=pressure,
        humidity=humidity,
        wind_speed=wind_speed,
        city_id=city_id,
    )

    temperature_info.save()

    return temperature_info


def write_city_to_database(city_json):

    city_to_add = City(
        city_name=city_json['name'].lower(),
        country_abbreviation=city_json['sys']['country'],
        longitude=city_json['coord']['lon'],
        latitude=city_json['coord']['lat'],
    )

    city_to_add.save()

    return city_to_add
