import datetime as dt
from xml.dom import ValidationErr


def validate_year(value):
    if value > dt.datetime.now().year:
        raise ValidationErr(
            'Год выпуска превышает текущий!')
    return value
