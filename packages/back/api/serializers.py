from django.contrib.auth.models import User
from .models import AI
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user


class AISerializer(serializers.ModelSerializer):
    class Meta:
        model = AI
        fields = ["id", "name", "back_story", "created_at", "creator"]
        extra_kwargs = {"author": {"read_only": True}}
