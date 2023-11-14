from rest_framework import serializers
from blog.models import *
class PostCategorySerializers(serializers.ModelSerializer):
   
    class Meta:
        model = Category
        fields = "__all__"

class PostTagSerializers(serializers.ModelSerializer):
   
    class Meta:
        model = Tag
        fields = "__all__"

class PostSerializers(serializers.ModelSerializer):
    snipes = serializers.ReadOnlyField(source='get_snipes')
    url_post = serializers.SerializerMethodField(method_name='url_post')
    category = serializers.SlugRelatedField(many=False,slug_field='title')
    class Meta:
        model = Post
        fields = "__all__"

    def get_url_post(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)

