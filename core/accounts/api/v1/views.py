from rest_framework import generics
from .serialiezers import Registerationserializer
from rest_framework.response import Response
from rest_framework import status


class RegistrationAPIView(generics.GenericAPIView):
    serializer_class = Registerationserializer

    def post(self, request, *args, **kwargs):
        serializer = Registerationserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "email": serializer.validated_data["email"],
            }
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_404_NOT_FOUND)
