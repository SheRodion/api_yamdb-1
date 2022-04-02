from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    ROLES = (
        ('user', 'USER'),
        ('moderator', 'MODERATOR'),
        ('admin', 'ADMIN')
    )

    email = models.EmailField(
        _('email'),
        max_length=256,
        unique=True,
        blank=False
    )
    password = models.CharField(
        _('password'),
        max_length=128,
        blank=True
    )
    bio = models.TextField(
        _('description'),
        max_length=512,
        blank=True
    )
    role = models.CharField(
        _('role'),
        max_length=30,
        choices=ROLES,
        default='user'
    )
    token = models.CharField(
        _('token'),
        max_length=128,
        blank=True
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return self.role == 'admin' or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == 'moderator'
