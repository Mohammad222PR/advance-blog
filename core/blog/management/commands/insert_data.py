from django.core.management.base import BaseCommand
from faker import Faker


class Command(BaseCommand):
    help = 'inserting dummy data'


    def handle(self, *args, **options):
        fake = Faker()
        print(fake.name())
        