from django.contrib.auth.models import User
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from users.serializers import UserSerializer, UserListSerializer

class UserModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    search_fields = ('nombre',)
    order_fields = ('nombre',)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)

    def get_queryset(self):
        return User.objects.all()

    def get_serializer_class(self):
        return UserSerializer if self.action != 'list' else UserListSerializer