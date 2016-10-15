
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from entradas.api import PostModelViewSet
from entradas.views import NewPostView

router = DefaultRouter()
router.register('api/1.0/post', PostModelViewSet, base_name='api_post_')

urlpatterns = [
    # Entradas URLS
    url(r'^newpost', NewPostView.as_view(), name='new_post'),

# API URLS
    url(r'', include(router.urls))
]