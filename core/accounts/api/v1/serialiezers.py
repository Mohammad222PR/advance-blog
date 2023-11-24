from rest_framework import serializers
from accounts.models import User


class Registerationserializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)

    """
    for registration user.
    """

    class Meta:
        model = User
        fields = ["email", "password", "password1"]

    def validate(self, attrs):
        if attrs.get("password") != attrs.get("password1"):
            raise serializers.ValidationError(
                {"detail": "password dose not math try again!"}
            )
        else:
            return super().validate(attrs)

    def create(self, validated_data):
        
        return super().create(validated_data)
