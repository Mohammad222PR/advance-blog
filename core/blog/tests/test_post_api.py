import pytest
from rest_framework.test import APIClient
from django.urls import reverse, resolve
from datetime import datetime

@pytest.mark.django_db
class TestPostApi:
    client = APIClient()

    def test_get_post_response_200_status(self):
        url = reverse("blog:api-v1:post-list")
        response = self.client.get(url)
        assert response.status_code == 200

    def test_create_post_response_200_status(self):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "Test Title",  # input title
            "content": "Test content",  # input content
            "created_date": datetime.now(),  # input created
        }
        self.client.force_authenticate(user={})
        response = self.client.post(url, data)
        assert response.status_code == 403
