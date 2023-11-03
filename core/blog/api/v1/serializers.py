from rest_framework import serializers
from blog.models import Post


class PostSerializers(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    tag = serializers.SlugRelatedField(slug_field='title', many=True, read_only=True)
    author = serializers.StringRelatedField()
    class Meta:
        model = Post
        fields = "__all__"