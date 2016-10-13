from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

class UserListSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ("id", "first_name", "last_name", "email")


