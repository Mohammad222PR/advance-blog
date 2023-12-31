from rest_framework import serializers
from ....models import User, Profile
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
)

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password2 = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs.get("new_password") != attrs.get("new_password2"):
            raise serializers.ValidationError("Password not mach")

        try:
            validate_password(attrs.get("new_password"))

        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"new_password": list(e.messages)})

        return super().validate(attrs)