import datetime as dt

from django.core.exceptions import ValidationError


def validate_year(value):
    if 0 > value > dt.datetime.now().year:
        raise ValidationError(
            'Некорректный год выпуска!')
    return value
