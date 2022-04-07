from django.db import models

from api_yamdb.reviews.validators import validate_year


class Category(models.Model):
    name = models.CharField(max_length=256, verbose_name='Имя')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Идентификатор')
    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'


class Genre(models.Model):
    name = models.CharField(max_length=256, verbose_name='Имя')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Индетификатор')
    
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Жанр'


class Title(models.Model):
    name = models.TextField(verbose_name='Имя')
    year = models.IntegerField(
        validators=[validate_year],
        verbose_name='Год выпуска')
    description = models.TextField(
        blank=True,
        verbose_name='Описание')
    genre = models.ManyToManyField(
        Genre,
        related_name='genre'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='category',
        null=True,
        verbose_name='Категория'
    )
    
    
    class Meta:
        ordering = ('name', 'year',)
        verbose_name = 'Произведения'
        
    def __str__(self):
        return (
            f'name: {self.name}, '
            f'year: {self.year}, '
        )
