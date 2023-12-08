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
    author = serializers.StringRelatedField(read_only=True)
    snipes = serializers.ReadOnlyField(source="get_snipes")
    url_post = serializers.SerializerMethodField(
        source="get_absolute_url"
    )
    category = serializers.SlugRelatedField(
        many=False,
        slug_field="title",
        queryset=Category.objects.all(),
    )
    image = serializers.SerializerMethodField(source="get_image")

    tag = serializers.SlugRelatedField(
        many=True, slug_field="title", queryset=Tag.objects.all()
    )

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ["author"]

    def get_url_post(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.pk)

    def get_image(self, obj):
        request = self.context.get("request")
        if obj.image:
            image = obj.image.url
            return request.build_absolute_uri(image)
        return None

    def to_representation(self, instance):
        request = self.context.get("request")
        rep = super().to_representation(instance)

        if request.parser_context.get("kwargs").get("pk"):
            rep.pop("snipes", None)
            rep.pop("url_post", None)
        else:
            rep.pop("content", None)

        rep["tag"] = PostTagSerializers(instance.tag, many=True).data
        rep["category"] = PostCategorySerializers(
            instance.category
        ).data

        return rep

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["author"] = Profile.objects.get(
            user__id=request.user.id
        )
        return super().create(validated_data)
