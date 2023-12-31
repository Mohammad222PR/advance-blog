from rest_framework import serializers
from ....models import Profile
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.serializers import (
)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
        read_only_fields = ["email", "user"]



