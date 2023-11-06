from rest_framework.views import Response
from rest_framework.views import APIView
from blog.models import Post
from .serializers import PostSerializers
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class PostList(APIView):
    serializer_class = PostSerializers
    parser_classes = (MultiPartParser,)
        
    def get(self, request):
        posts = Post.objects.all()
        ser = PostSerializers(instance=posts, many=True)
        return Response(data=ser.data)
    

    def post(self, request):
        ser = PostSerializers(data=request.data)
        if ser.is_valid():
            ser.validated_data['author'] = request.user
            ser.save()
            return Response(data=ser.data, status=status.HTTP_201_CREATED)
        return Response(data=ser.errors, status=status.HTTP_400_BAD_REQUEST)

class PostUpdateView(APIView):
    serializer_class = PostSerializers
    parser_classes = (MultiPartParser,)

    def put(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        ser = PostSerializers(instance=post, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(data=ser.data, status=status.HTTP_200_OK)
        return Response(data=ser.errors, status=status.HTTP_404_NOT_FOUND)


    def delete(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        post.delete()
        return Response("item Remove Success Fully", status=status.HTTP_202_ACCEPTED)


class PostDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    def get(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        ser = PostSerializers(instance=post)
        return Response(data=ser.data, status=status.HTTP_200_OK)


