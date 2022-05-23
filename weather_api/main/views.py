from django.http import JsonResponse

from weather_api.main.helpers.serializers import serialize_temperature_information
from weather_api.main.helpers.write_to_database import write_city_to_database, write_temperature_to_database
from weather_api.main.models import City
from weather_api.main.tasks import get_weather_by_city_name


def get_weather_by_city_view(request, city_name):
    try:
        current_city = City.objects.get(city_name=city_name)
        return JsonResponse(serialize_temperature_information(current_city))
    except City.DoesNotExist:
        new_city_json = get_weather_by_city_name(city_name)
        current_city = write_city_to_database(new_city_json)
        temp_info = write_temperature_to_database(new_city_json, current_city.id)
        print(temp_info)
        return JsonResponse(serialize_temperature_information(current_city))
