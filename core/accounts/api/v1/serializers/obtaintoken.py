from rest_framework import serializers
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
)


class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(label=_("Email"), write_only=True)
    password = serializers.CharField(
        label=_("Password"),
        style={"input_type": "password"},
        trim_whitespace=False,
        write_only=True,
    )
    token = serializers.CharField(label=_("Token"), read_only=True)

    def validate(self, attrs):
        username = attrs.get("email")
        password = attrs.get("password")

        if username and password:
            user = authenticate(
                request=self.context.get("request"),
                username=username,
                password=password,
            )
            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _("Unable to log in with provided credentials.")
                raise serializers.ValidationError(msg, code="authorization")

            if not user.is_verified:
                raise serializers.ValidationError(
                    {"detail": "User is not verified"},
                    code="authorization",
                )

        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code="authorization")

        attrs["user"] = user
        return attrs


class CustomTokenObtainPairSerializers(TokenObtainPairSerializer):
    def validate(self, attrs):
        validated_data = super().validate(attrs)

        if not self.user.is_verified:
            raise serializers.ValidationError(
                {"detail": "User is not verified"},
                code="authorization",
            )

        validated_data["message"] = str(
            "This is your JWT token dont share this key to any users"
        )
        validated_data["email"] = self.user.email
        validated_data["id"] = self.user.id
        return validated_data
