from django.test import TestCase
from ..models import Post, Category, Tag
from datetime import datetime
from django.contrib.auth import get_user_model
from accounts.models import User, Profile


class TestPostModels(TestCase):
    def setUp(self):
        self.tag_obj = Tag.objects.create(title="test tag")
        self.category_obj = Category.objects.create(
            title="test category"
        )

        self.user = User.objects.create_user(
            email="email@example.com", password="DAWqwdqfgawfqs"
        )

        self.profile = Profile.objects.create(
            user=self.user,
            first_name="John",
            last_name="mike",
            email=self.user.email,
            avatar=None,
            bio="hi",
            created_date=datetime.now(),
            update_date=datetime.now(),
        )

    def test_create_post_which_valid_data(self):
        post = Post.objects.create(
            author=self.profile,
            title="test",  # input title
            image=None,  # input image
            content="Test content",  # input content
            status=True,
            category=self.category_obj,  # input category
            created_date=datetime.now(),  # input created
            updated_date=datetime.now(),
            published_day=datetime.now(),
        )
        post.tag.set([self.tag_obj])

        self.assertTrue(Post.objects.filter(pk=post.id).exists())

    def test_create_category_which_valid_data(self):
        category = Category.objects.create(
            title="test",
            parent=None,
            created_date=datetime.now(),
        )

        self.assertTrue(
            Category.objects.filter(pk=category.id).exists()
        )

    def test_tag_category_which_valid_data(self):
        tag = Tag.objects.create(
            title="test",
            created_date=datetime.now(),
        )

        self.assertTrue(Tag.objects.filter(pk=tag.id).exists())
