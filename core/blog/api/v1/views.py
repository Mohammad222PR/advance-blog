from rest_framework.views import Response
from rest_framework.views import APIView
from blog.models import Post
from .serializers import PostSerializers
from rest_framework import status
from django.shortcuts import get_object_or_404
data = {
    "id":1,
    "title":"hi"
}

class PostList(APIView):
    def get(self, request):
        posts = Post.objects.all()
        ser = PostSerializers(instance=posts, many=True)
        return Response(data=ser.data)
    
    
class PostDetail(APIView):
    def get(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        ser = PostSerializers(instance=post)
        return Response(data=ser.data, status=status.HTTP_200_OK)
        