# from django.test import TestCase, Client
# from django.urls import reverse
# from accounts.models import User, Profile
# from datetime import datetime
# from ..models import Post, Category, Tag
# from django.core.files.uploadedfile import SimpleUploadedFile


# class TestPostViews(TestCase):
#     def setUp(self):
#         self.client = Client()

#         self.user = User.objects.create_user(
#             email="email@example.com", password="DAWqwdqfgawfqs"
#         )

#         self.profile = Profile.objects.create(
#             user=self.user,
#             first_name="John",
#             last_name="mike",
#             email=self.user.email,
#             avatar=None,
#             bio="hi",
#             created_date=datetime.now(),
#             update_date=datetime.now(),
#         )

#         self.category_obj = Category.objects.create(title="test category")
#         self.tag_obj = Tag.objects.create(title="test tag")
#         image = SimpleUploadedFile(
#             "photo1697911298.jpeg", content=b"file_content", content_type="image/jpeg"
#         )

#         self.post = Post.objects.create(
#             author=self.profile,
#             title="test",  # input title
#             image=image,  # input image
#             content="Test content",  # input content
#             status=True,
#             category=self.category_obj,  # input category
#             created_date=datetime.now(),  # input created
#             updated_date=datetime.now(),
#             published_day=datetime.now(),
#         )
#         self.post.tag.set([self.tag_obj])

#     def test_blog_index_url_successful_response(self):
#         url = reverse("blog:index")
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, 200)
#         self.assertTrue(str(response.content).find("index"))
#         self.assertTemplateUsed(response, template_name="blog/index.html")

#     def test_post_detail_is_logged_in_response(self):
#         self.client.force_login(self.user)
#         url = reverse("blog:post-detail", kwargs={"pk": self.post.id})
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, template_name="blog/detail.html")

#     def test_post_detail_is_anonymous_response(self):
#         url = reverse("blog:post-detail", kwargs={"pk": self.post.id})
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, 302)
