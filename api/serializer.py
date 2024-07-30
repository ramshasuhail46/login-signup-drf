from django.contrib.auth import get_user_model

from rest_framework import serializers
from django.contrib.auth.models import User

User = get_user_model()


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8)

    class Meta:
        model = User
        fields = ['email']


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, write_only=True)
    username = serializers.CharField(max_length=20)
    first_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = super().create(validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

    class Meta:
        model = User
        fields = ['email', 'password', 'username', 'first_name', 'last_name']
