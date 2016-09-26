from django.conf.urls import url

from blogs.views import HomeView, BlogListView, BlogUserListView, BlogCatListView

urlpatterns = [
    # url(r'^create$', PhotoCreationView.as_view(), name='photos_create'),
    url(r'^blogs$', BlogListView.as_view(), name='blogs_list'),
    url(r'^blogs/([\w-]+)/$', BlogUserListView.as_view(), name='blogsuser_list'),
    url(r'^blogs/cat/(?P<pk>[\w-]+)/$', BlogCatListView.as_view(), name='blogscat_list'),
    url(r'^$', HomeView.as_view(), name='blogs_home'),

]

