from django.conf.urls import url

from blogs.views import HomeView

urlpatterns = [
    # url(r'^create$', PhotoCreationView.as_view(), name='photos_create'),
    # url(r'^photos/$', PhotoListView.as_view(), name='photos_my_photos'),
    # url(r'^photos/(?P<pk>[0-9]+)$', PhotoDetailView.as_view(), name='photos_detail'),
    url(r'^$', HomeView.as_view(), name='blogs_home'),
]

