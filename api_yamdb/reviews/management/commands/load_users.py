from csv import DictReader
from django.core.management import BaseCommand
from reviews.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Show this if the data already exist in the database
        if User.objects.count() > 1:
            print('user data already loaded...exiting.')
            return
        # Show this before loading the data into the database
        print('Loading user data...')
        # Code to load the data into database
        for row in DictReader(open(
                './static/data/users.csv', encoding='utf-8')):
            user = User(
                id=row['id'],
                username=row['username'],
                email=row['email'],
                first_name=row['first_name'],
                last_name=row['last_name'],
                bio=row['bio'],
                role=row['role'])
            user.save()
        print('...done')
