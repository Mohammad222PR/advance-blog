from accounts.models import *
from rest_framework.validators import ValidationError
from rest_framework.views import APIView


class IsOwnerOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return Profile.user == request.user


class IsVerified(APIView):
    def get(self, request, view, obj):
        user = request.user
        if not user.is_verified:
            raise ValidationError("you are not verified")
        else:
            pass
