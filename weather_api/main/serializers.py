from rest_framework import serializers
from weather_api.main.models import Temperature, City


class TemperatureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Temperature
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'
