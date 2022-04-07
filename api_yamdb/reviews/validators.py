import datetime as dt

from django.core.exceptions import ValidationError


def validate_year(value):
    if value > dt.datetime.now().year:
        raise ValidationError(
            'Год выпуска превышает текущий!')
    return value
