from rest_framework import serializers
from blog.models import Post


class PostSerializers(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    tag = serializers.StringRelatedField()
    author = serializers.StringRelatedField()
    class Meta:
        model = Post
        fields = "__all__"