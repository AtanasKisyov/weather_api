from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from weather_api.auth.views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', obtain_auth_token, name='obtain_auth_token'),
]
