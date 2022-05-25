from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

UserModel = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ('username', 'password')

    def create(self, validated_data):

        user = UserModel.objects.create(
            username=validated_data['username'],
            password=make_password(validated_data['password']),
        )

        return {
            'username': user.username,
            'password': 'Hidden',
        }
