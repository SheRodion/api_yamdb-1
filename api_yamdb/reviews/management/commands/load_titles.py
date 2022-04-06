from csv import DictReader
from django.core.management import BaseCommand
from reviews.models import Title


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Show this if the data already exist in the database
        if Title.objects.count() > 1:
            print('titles data already loaded...exiting.')
            return
        # Show this before loading the data into the database
        print('Loading titles data...')
        # Code to load the data into database
        for row in DictReader(open(
                './static/data/titles.csv', encoding='utf-8')):
            titles = Title(
                id=row['id'],
                name=row['name'],
                year=row['year'],
                category_id=row['category_id'])
            titles.save()
        print('...done')
