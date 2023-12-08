from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import Profile

User = get_user_model()
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=10000)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="sub",
        null=True,
        blank=True,
    )
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=10000)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=10000)
    image = models.ImageField(
        upload_to="images/posts", null=True, blank=True
    )
    content = models.TextField(max_length=1000000000)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="post"
    )
    tag = models.ManyToManyField(Tag, related_name="post")
    status = models.BooleanField(default=True)
    # Time Field.
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_day = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_snipes(self):
        return self.content[0:3] + str("...")
