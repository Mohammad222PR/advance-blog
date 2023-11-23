from rest_framework import serializers
from accounts.models import User

class Registerationserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','password']