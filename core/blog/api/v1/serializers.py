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
    
    class Meta:
        model = Post
        fields = "__all__"

