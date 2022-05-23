import celery

from weather_api.main.helpers.api_call import get_weather_by_city_name
from weather_api.main.helpers.write_to_database import write_temperature_to_database
from weather_api.main.models import City


@celery.shared_task
def get_available_cities_current_weather():
    cities = City.objects.all()

    for city in cities:
        current_city = get_weather_by_city_name(city.city_name)
        write_temperature_to_database(current_city, city.id)
