from django.urls import path

from weather_api.main.views import GetWeather, GetCity, CombinedInformationView

urlpatterns = [
    path('get-weather-by-city/<str:city_name>', GetWeather.as_view(), name='get_weather_by_city'),
    path('get-city-information/<str:city_name>', GetCity.as_view(), name='get_city_information'),
    path('get-combined-data/<str:city_name>', CombinedInformationView.as_view(), name='combined_information'),
]
