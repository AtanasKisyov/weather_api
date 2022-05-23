from django.urls import path

from weather_api.main.views import test_view

urlpatterns = [
    path('', test_view, name='test'),
]
