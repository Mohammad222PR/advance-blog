from blog.models import *
from .serializers import *
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .paginations import PaginationClass

# class PostList(APIView):
#     serializer_class = PostSerializers
#     parser_classes = (MultiPartParser,)
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         """This View For view post and add Post"""

#         posts = Post.objects.filter(status=True)
#         ser = PostSerializers(instance=posts, many=True)
#         return Response(data=ser.data)

#     def post(self, request):
#         ser = PostSerializers(data=request.data)
#         if ser.is_valid():
#             ser.validated_data["author"] = request.user
#             ser.save()
#             return Response(data=ser.data, status=status.HTTP_201_CREATED)
#         return Response(data=ser.errors, status=status.HTTP_400_BAD_REQUEST)




# class PostDetail(APIView):
#     serializer_class = PostSerializers
#     parser_classes = (MultiPartParser,)
#     permission_classes = [IsAuthenticated]

#     def get(self, request, pk):
#         post = get_object_or_404(Post, id=pk)
#         ser = PostSerializers(instance=post)
#         return Response(data=ser.data, status=status.HTTP_200_OK)

#     def put(self, request, pk):
#         post = get_object_or_404(Post, id=pk)
#         ser = PostSerializers(instance=post, data=request.data, partial=True)
#         if ser.is_valid():
#             ser.save()
#             return Response(data=ser.data, status=status.HTTP_200_OK)
#         return Response(data=ser.errors, status=status.HTTP_404_NOT_FOUND)

#     def delete(self, request, pk):
#         post = get_object_or_404(Post, id=pk)
#         post.delete()
#         return Response("item Remove Success Fully", status=status.HTTP_202_ACCEPTED)


@method_decorator(cache_page(60, key_prefix="cache-view"), name="get")
class PostListGeneric(ModelViewSet):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    ]
    queryset = Post.objects.filter(status=True)
    serializer_class = PostSerializers
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    filterset_fields = ["category", "status", "author", "tag"]
    search_fields = ["content", "title"]
    ordering_fields = ["created_date", "status"]
    pagination_class = PaginationClass


@method_decorator(cache_page(60, key_prefix="cache-view"), name="get")
class PostCategoryListGeneric(ModelViewSet):
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser,)
    queryset = Category.objects.all()
    serializer_class = PostCategorySerializers
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    search_fields = ["title"]
    ordering_fields = ["created_date"]
    pagination_class = PaginationClass


@method_decorator(cache_page(60, key_prefix="cache-view"), name="get")
class PostTagListGeneric(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    parser_classes = (MultiPartParser,)
    queryset = Tag.objects.all()
    serializer_class = PostTagSerializers
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    search_fields = ["title"]
    ordering_fields = ["created_date"]
    pagination_class = PaginationClass
