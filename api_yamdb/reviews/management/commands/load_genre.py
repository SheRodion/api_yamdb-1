from csv import DictReader
from django.core.management import BaseCommand
from reviews.models import Genre


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Show this if the data already exist in the database
        if Genre.objects.count() > 1:
            print('genre data already loaded...exiting.')
            return
        # Show this before loading the data into the database
        print('Loading genre data...')
        # Code to load the data into database
        for row in DictReader(open(
                './static/data/genre.csv', encoding='utf-8')):
            genre = Genre(
                id=row['id'],
                name=row['name'],
                slug=row['slug'])
            genre.save()
        print('...done')
