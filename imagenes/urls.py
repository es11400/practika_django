from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from imagenes.views import ImagenesModelViewSet

router = DefaultRouter()
router.register('api/1.0/img', ImagenesModelViewSet, base_name='api_imagenes_')

urlpatterns = [

    # API URLS
    url(r'', include(router.urls))
]
