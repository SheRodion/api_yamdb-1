import uuid

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
    confirmation_code = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
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
        return self.role == 'admin' or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == 'moderator'

    def check_code(self, code):
        return self.confirmation_code == code
