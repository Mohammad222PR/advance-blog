from django.core.management.base import BaseCommand
from faker import Faker
from accounts.models import User, Profile
from blog.models import Post, Category, Tag
import random
from datetime import datetime

# category list
category_list = [
    "IT",
    "Design",
    "Programming",
    "db",
    "AI",
]

# tag list
tag_list = [
    "new",
]


class Command(BaseCommand):
    help = "inserting dummy data"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker()

    def handle(self, *args, **options):
        user = User.objects.create(email=self.fake.email(), password="Test@12345")
        profile = Profile.objects.get(user=user)
        # Update data profile
        profile.first_name = self.fake.first_name()
        profile.last_name = self.fake.last_name()
        profile.bio = self.fake.paragraph(nb_sentences=10)
        profile.save()

        # create categories or gey
        for name in category_list:
            Category.objects.get_or_create(title=name)

        # create tag or gey
        for name in tag_list:
            Tag.objects.get_or_create(title=name)

        for _ in range(10):
            Post.objects.create(
                author=profile,
                title=self.fake.paragraph(nb_sentences=1),
                image="media/images/3d-web-developer-working-on-project-illustration-png.webp",
                content=self.fake.paragraph(nb_sentences=10),
                category=Category.objects.get(title=random.choice(category_list)),
                status=True,
                created_date=datetime.now(),
                updated_date=datetime.now(),
                published_day=datetime.now(),
            )
