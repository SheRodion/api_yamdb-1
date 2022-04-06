from csv import DictReader
from django.core.management import BaseCommand
from reviews.models import GenreTitle


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Show this if the data already exist in the database
        if GenreTitle.objects.count() > 1:
            print('genre_titles data already loaded...exiting.')
            return
        # Show this before loading the data into the database
        print('Loading genre_titles data...')
        # Code to load the data into database
        for row in DictReader(open(
                './static/data/genre_title.csv', encoding='utf-8')):
            title_genre = GenreTitle(
                id=row['id'],
                title_id=row['title_id'],
                genre_id=row['genre_id'])
            title_genre.save()
        print('...done')
