from django.urls import path

from weather_api.main.views import get_weather_by_city_view

urlpatterns = [
    path('get-weather-by-city/<str:city_name>', get_weather_by_city_view, name='get_weather_by_city')
]
