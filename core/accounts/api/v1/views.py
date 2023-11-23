from rest_framework import generics
from .serialiezers import Registerationserializer
from rest_framework.response import Response


class RegistrationAPIView(generics.GenericAPIView):
    serializer_class = Registerationserializer

    def post(self, request, *args, **kwargs):
        serializer = Registerationserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            date = {
                'email':''
            }
            return Response()
