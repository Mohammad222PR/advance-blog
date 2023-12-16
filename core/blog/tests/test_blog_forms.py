# from django.test import TestCase
# from django.urls import reverse, resolve
# from ..forms import PostCreateForm
# from ..models import Category, Tag
# from datetime import datetime

# # Create your tests here.

# # test form models


# class TestFormPost(TestCase):
#     # testing form (PostCreateForm)

#     def test_post_form_which_valid_data(self):
#         category_obj = Category.objects.create(title="test category")
#         tag_obj = Tag.objects.create(title="test tag")

#         form = PostCreateForm(
#             data={
#                 "title": "Test Title",  # input title
#                 "image": None,  # input image
#                 "content": "Test content",  # input content
#                 "category": category_obj,  # input category
#                 "tag": [tag_obj],  # input tag
#                 "created_date": datetime.now(),  # input created
#             }
#         )

#         if not form.is_valid():
#             print(form.errors)

#         self.assertTrue(form.is_valid())

#     def test_post_form_which_no_data(self):
#         form = PostCreateForm(data={})

#         self.assertFalse(form.is_valid())
