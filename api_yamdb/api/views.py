from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Avg
from rest_framework import  viewsets, filters, mixins

from reviews.models import Category, Genre, Title

from .serializers import (
    CategorySerializer,
    GenreSerializer,
    TitleWriteSerializer,
    TitleReadSerializer,
)
from .filters import TitleFilter

User = get_user_model()


class CategoryViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (ReadOnlyPermission | IsAdminPermission,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('name',)
    search_fields = ('name',)
    lookup_field = 'slug'


class GenreViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (ReadOnlyPermission | IsAdminPermission,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('name',)
    search_fields = ('name',)
    lookup_field = 'slug'


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all().annotate(rating=Avg('reviews__score'))
    permission_classes = (ReadOnlyPermission | IsAdminPermission,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = (
        'category',
        'genre',
        'name',
        'year',
    )
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'list':
            return TitleReadSerializer
        return TitleWriteSerializer
