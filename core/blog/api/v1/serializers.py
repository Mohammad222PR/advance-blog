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
    author = serializers.StringRelatedField()
    snipes = serializers.ReadOnlyField(source="get_snipes")
    url_post = serializers.SerializerMethodField(source="get_absolute_url")
    category = serializers.SlugRelatedField(
        many=False, slug_field="title", queryset=Category.objects.all()
    )
    image = serializers.SerializerMethodField()

    tag = serializers.SlugRelatedField(
        many=True, slug_field="title", queryset=Tag.objects.all()
    )

    class Meta:
        model = Post
        fields = "__all__"

    def get_url_post(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.pk)

    def get_image(self, obj):
        request = self.context.get("request")
        img = obj.image.url
        return request.build_absolute_uri(img)

    def to_representation(self, instance):
        request = self.context.get("request")
        rep = super().to_representation(instance)

        if request.parser_context.get("kwargs").get("pk"):
            rep.pop("snipes", None)
            rep.pop("url_post", None)
        else:
            rep.pop("content", None)

        rep["tag"] = PostTagSerializers(instance.tag, many=True).data
        rep["category"] = PostCategorySerializers(instance.category).data

        return rep
