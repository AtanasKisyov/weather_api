import rest_framework.views
from rest_framework.response import Response

from weather_api.main.serializers import TemperatureSerializer, CitySerializer
from weather_api.main.helpers.write_to_database import write_city_to_database, write_temperature_to_database
from weather_api.main.models import City, Temperature
from weather_api.main.tasks import get_weather_by_city_name


class GetWeather(rest_framework.views.APIView):

    @staticmethod
    def get(request, city_name):
        try:
            current_city = City.objects.get(city_name=city_name)
            temp_info = Temperature.objects.filter(city_id=current_city.id).latest()
            serializer = TemperatureSerializer(temp_info)
            return Response(serializer.data)
        except City.DoesNotExist:
            new_city_json = get_weather_by_city_name(city_name)
            current_city = write_city_to_database(new_city_json)
            write_temperature_to_database(new_city_json, current_city.id)
            temp_info = Temperature.objects.filter(city_id=current_city.id).latest()
            serializer = TemperatureSerializer(temp_info)
            return Response(serializer.data)


class GetCity(rest_framework.views.APIView):

    @staticmethod
    def get(request, city_name):
        try:
            current_city = City.objects.get(city_name=city_name)
            serializer = CitySerializer(current_city)
            return Response(serializer.data)
        except City.DoesNotExist:
            new_city_json = get_weather_by_city_name(city_name)
            write_city_to_database(new_city_json)
            current_city = City.objects.get(city_name=city_name)
            serializer = CitySerializer(current_city)
            return Response(serializer.data)


class CombinedInformationView(rest_framework.views.APIView):

    @staticmethod
    def get(request, city_name):
        try:
            current_city = City.objects.get(city_name=city_name)
            city_serializer = dict(CitySerializer(current_city).data)
            temp_info = Temperature.objects.filter(city_id=current_city.id).latest()
            temp_serializer = dict(TemperatureSerializer(temp_info).data)
            city_serializer.update(temp_serializer)
            return Response(city_serializer)
        except City.DoesNotExist:
            new_city_json = get_weather_by_city_name(city_name)
            write_city_to_database(new_city_json)
            current_city = City.objects.get(city_name=city_name)
            serializer = CitySerializer(current_city)
            return Response(serializer.data)
