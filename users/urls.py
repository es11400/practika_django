
from django.conf.urls import url


from users.views import LogoutView

urlpatterns = [
    # Web URLS
    url(r'^logout$', LogoutView.as_view(), name='users_logout'),
]