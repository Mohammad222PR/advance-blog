import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from datetime import datetime
from accounts.models import User
from ..models import Category, Tag
from django.core.files.uploadedfile import SimpleUploadedFile


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def common_user():
    user_obj = User.objects.create_user(
        email="ad@example.com", password="Adwqd2edsd", is_verified=True
    )
    return user_obj


@pytest.fixture
def category():
    category_obj = Category.objects.create(title="test category")
    return category_obj


@pytest.fixture
def tag():
    tag_obj = Tag.objects.create(title="test tag")
    return tag_obj


@pytest.fixture
def image():
    image = SimpleUploadedFile(
        "photo1697911298.jpeg", content=b"file_content", content_type="image/jpeg"
    )
    return image


@pytest.mark.django_db
class TestPostApi:
    def test_get_post_response_200_status(self, api_client):
        url = reverse("blog:api-v1:post-list")
        response = api_client.get(url)
        assert response.status_code == 200

    def test_create_post_response_401_status(self, api_client, category, tag, image):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "Test Title",  # input title
            "image": image,  # input image
            "content": "Test content",  # input content
            "category": category,  # input category
            "tag": [tag],  # input tag
            "created_date": datetime.now(),  # input created
        }
        response = api_client.post(url, data)
        assert response.status_code == 401

    def test_create_post_response_201_status(
        self, api_client, common_user, category, tag, image
    ):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "Test Title",  # input title
            "image": image,  # input image
            "content": "Test content",  # input content
            "category": category,  # input category
            "tag": [tag],  # input tag
            "created_date": datetime.now(),  # input created
        }
        user = common_user
        api_client.force_login(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 201

    def test_create_post_invalid_response_400_status(self, api_client, common_user):
        url = reverse("blog:api-v1:post-list")
        data = {}
        user = common_user
        api_client.force_login(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 400
