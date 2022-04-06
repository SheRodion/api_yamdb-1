from csv import DictReader
from django.core.management import BaseCommand
from reviews.models import Review


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Show this if the data already exist in the database
        if Review.objects.count() > 1:
            print('review data already loaded...exiting.')
            return
        # Show this before loading the data into the database
        print('Loading review data...')
        # Code to load the data into database
        for row in DictReader(open(
                './static/data/review.csv', encoding='utf-8')):
            review = Review(
                id=row['id'],
                title_id=row['title_id'],
                text=row['text'],
                author_id=row['author_id'],
                score=row['score'],
                pub_date=row['pub_date'])
            review.save()
        print('...done')
