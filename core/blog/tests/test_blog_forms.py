from django.test import TestCase
from django.urls import reverse, resolve
from ..forms import PostCreateForm
from ..models import Category, Tag
from datetime import datetime

# Create your tests here.


class TestFormPost(TestCase):

    def test_post_form_which_valid_data(self):
        category_obj = Category.objects.create(title='test category')
        tag_obj = Tag.objects.create(title='test tag')

        form = PostCreateForm(
            data={
                "title": "Test Title",
                "image": None,
                "content": "Test content",
                "category": category_obj,
                "tag": tag_obj,
                "created_date": datetime.now(),
            }
        )
        self.assertTrue(form.is_valid())
