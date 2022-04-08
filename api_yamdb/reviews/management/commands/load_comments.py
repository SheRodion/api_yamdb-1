from csv import DictReader
from django.core.management import BaseCommand
from reviews.models import Comment


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Show this if the data already exist in the database
        if Comment.objects.count() > 1:
            print('comments data already loaded...exiting.')
            return
        # Show this before loading the data into the database
        print('Loading comments data...')
        # Code to load the data into database
        for row in DictReader(open(
                './static/data/comments.csv', encoding='utf-8')):
            comm = Comment(
                id=row['id'],
                review_id=row['review_id'],
                text=row['text'],
                author_id=row['author_id'],
                pub_date=row['pub_date'])
            comm.save()
        print('...done')
