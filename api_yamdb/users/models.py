from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserRole:
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'


class User(AbstractUser):
    ROLES = (
        (UserRole.USER, 'USER'),
        (UserRole.MODERATOR, 'MODERATOR'),
        (UserRole.ADMIN, 'ADMIN')
    )

    email = models.EmailField(
        _('email'),
        max_length=256,
        unique=True,
    )
    bio = models.TextField(
        _('description'),
        blank=True
    )
    role = models.CharField(
        _('role'),
        max_length=9,
        choices=ROLES,
        default=UserRole.USER
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)
        constraints = [
            models.UniqueConstraint(
                fields=['username', 'email'],
                name='unique_name'
            ),
        ]

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return (self.role == UserRole.ADMIN
                or self.is_staff
                or self.is_superuser)

    @property
    def is_user(self):
        return self.role == UserRole.USER

    @property
    def is_moderator(self):
        return self.role == UserRole.MODERATOR
