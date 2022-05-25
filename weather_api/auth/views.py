from rest_framework import generics as rest_views
from rest_framework.permissions import AllowAny

from weather_api.auth.serializers import RegisterSerializer


class RegisterView(rest_views.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
