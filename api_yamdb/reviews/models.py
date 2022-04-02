from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


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
    name = models.CharField(max_length=30, unique=True, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание')
    year = models.IntegerField()
    genre = models.ManyToManyField(
        'жанр',
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
