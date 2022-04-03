from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from users.models import User


class Genre(models.Model):
    name = models.CharField(max_length=256, verbose_name='Имя')
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='Индетификатор'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Жанр'
    
    def __str__(self):
        return f'{self.name} {self.name}'

class GenreTitle(models.Model):
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    title = models.ForeignKey('Title', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} {self.genre}'

class Category(models.Model):
    name = models.CharField(max_length=256, verbose_name='Имя')
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='Идентификатор'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
    
    def __str__(self):
        return f'{self.name} {self.name}'    


class Title(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание')
    year = models.IntegerField()
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
        return f'{self.name}' 

class Review(models.Model):
    title = models.ForeignKey(
        Title,
        verbose_name='Произведение',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    text = models.TextField(
        verbose_name='Текст',
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
    )
    score = models.IntegerField(
        verbose_name='Рейтинг',
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['pub_date']
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'],
                name='unique_review'
            ),
        ]

    def __str__(self):
        return self.text


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        verbose_name='Отзыв',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField(
        verbose_name='Текст',
    )
    author = models.ForeignKey(
        User,
        verbose_name='Комментатор',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['pub_date']

    def __str__(self):
        return self.text
