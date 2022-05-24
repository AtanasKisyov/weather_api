from weather_api.main.models import Temperature


def serialize_temperature_information(city):
    latest_temperature = Temperature.objects.filter(city_id=city.id).latest()
    result = {
        'city_name': city.city_name.capitalize(),
        'country_code': city.country_abbreviation,
        'longitude': city.longitude,
        'latitude': city.latitude,
        'current_temperature': latest_temperature.temperature,
        'minimum_temperature': latest_temperature.minimum_temperature,
        'maximum_temperature': latest_temperature.maximum_temperature,
        'pressure': latest_temperature.pressure,
        'humidity': latest_temperature.humidity,
        'wind_speed': latest_temperature.wind_speed,
        'updated_at': latest_temperature.time,
    }
    return result
