
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from users.api import UserModelViewSet
from users.views import LogoutView

router = DefaultRouter()
router.register('/1.0/users', UserModelViewSet, base_name='api_users_')

urlpatterns = [
    # Web URLS
    url(r'^logout$', LogoutView.as_view(), name='users_logout'),

    # API URLS
    url(r'api', include(router.urls))
]