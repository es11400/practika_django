from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from blogs.models import blogs
from blogs.serializers import BlogListSerializer, BlogSerializer


class BlogModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    search_fields = ('nombre',)
    order_fields = ('nombre',)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)

    def get_queryset(self):
        return blogs.objects.all()

    def get_serializer_class(self):
        return BlogSerializer if self.action != 'list' else BlogListSerializer