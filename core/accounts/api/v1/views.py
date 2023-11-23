from rest_framework import generics
from .serialiezers import Registerationserializer

class RegistrationAPIView(generics.GenericAPIView):
    serializer_class = Registerationserializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class()
        
        return 