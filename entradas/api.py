from django.db.models import Q
from django.utils.datetime_safe import datetime
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from cuentame.my_settings import *
from entradas.models import post
from entradas.permissions import PostPermission
from entradas.serializers import PostSerializer, PostListSerializer


class PostModelViewSet(ModelViewSet):
    permission_classes = (PostPermission,)
    search_fields = ('titulo', "texto_corto", "texto_largo",)
    order_fields = ('titulo', "fecha",)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, filters.DjangoFilterBackend,)
    filter_fields = ('cat__nombre',)


    def get_queryset(self):
        if self.request.user.is_superuser:
            return post.objects.filter(visible=VISIBLE_SI).order_by('-fecha')
        elif self.request.user.is_authenticated:
            return post.objects.filter(Q(visible=VISIBLE_SI) & Q(fecha__lte=datetime.now()) | Q(blog__usuario=self.request.user)).order_by('-fecha')
        else:
            return post.objects.filter(visible=VISIBLE_SI, fecha__lte=datetime.now()).order_by('-fecha')

    def get_serializer_class(self):
        return PostSerializer if self.action != 'list' else PostListSerializer
