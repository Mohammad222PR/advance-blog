from django.test import TestCase
from django.urls import reverse, resolve
from ..forms import PostCreateForm
from datetime import datetime
# Create your tests here.


class TestFormPost(TestCase):
    def test_post_form_which_valid_data(self):
        form = PostCreateForm(
            data={
                "title": "Test Title",
                "image": "",
                "content": "Test content",
                "category": '1',
                "tags":'1',
                "created_date":datetime.now(),
                "updated_date":datetime.now(),
                "published_day":datetime.now()
            }
        )
        self.assertTrue(form.is_valid())
        
