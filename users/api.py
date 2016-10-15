from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from users.permissions import UserPermission
from users.serializers import UserSerializer, UserListSerializer

class UserModelViewSet(ModelViewSet):
    permission_classes = (UserPermission,)
    search_fields = ('nombre',)
    order_fields = ('nombre',)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)

    def get_queryset(self):
        return User.objects.all()

    def get_serializer_class(self):
        return UserSerializer if self.action != 'list' else UserListSerializer

    def perform_create(self, UserSerializer):
        password = make_password(self.request.data['password'])
        UserSerializer.save(password=password)

    def perform_update(self, UserSerializer):
        password = make_password(self.request.data['password'])
        UserSerializer.save(password=password)
