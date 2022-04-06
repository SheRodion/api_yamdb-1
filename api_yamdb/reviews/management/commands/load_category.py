from csv import DictReader
from django.core.management import BaseCommand
from reviews.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Show this if the data already exist in the database
        if Category.objects.count() > 1:
            print('category data already loaded...exiting.')
            return
        # Show this before loading the data into the database
        print('Loading category data...')
        # Code to load the data into database
        for row in DictReader(open(
                './static/data/category.csv', encoding='utf-8')):
            cat = Category(
                id=row['id'],
                name=row['name'],
                slug=row['slug'])
            cat.save()
        print('...done')
