from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class LoginSerializer(serializers.Serializer):
    name = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        name = data.get("name")
        password = data.get("password")
        user = authenticate(username=name, password=password)
        if not user:
            raise serializers.ValidationError("Błędna nazwa użytkownika lub hasło")
        return user


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "password", "email"]

    def create(self, validate_date):
        user = User.objects.create_user(
            username=validate_date["username"],
            email=validate_date["email"],
            password=validate_date["password"],
        )
        return user
