# from django.test import TestCase
# from django.urls import reverse, resolve
# from ..views import IndexView, PostView, PostDetailView

# # Create your tests here.


# class TestUrl(TestCase):
#     def test_blog_index_resolve(self):
#         url = reverse("blog:index")
#         self.assertEqual(resolve(url).func.view_class, IndexView)

#     def test_blog_post_list_url_resolve(self):
#         url = reverse("blog:blog")
#         self.assertEqual(resolve(url).func.view_class, PostView)

#     def test_blog_post_detail_url_resolve(self):
#         url = reverse("blog:post-detail", kwargs={"pk": 15})
#         self.assertEqual(resolve(url).func.view_class, PostDetailView)
