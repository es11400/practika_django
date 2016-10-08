from django.conf.urls import url

from blogs.views import HomeView, BlogListView, BlogUserListView, BlogCatListView, BlogUserDetailView

urlpatterns = [
    # url(r'^create$', PhotoCreationView.as_view(), name='photos_create'),
    url(r'^blogs$', BlogListView.as_view(), name='blogs_list'),
    url(r'^blogs/(?P<username>[\w-]+)/$', BlogUserListView.as_view(), name='blogsuser_list'),
    url(r'^blogs/(?P<username>[\w-]+)/(?P<postId>[0-9]+)$', BlogUserDetailView.as_view(), name='blogsuser_post'),
    url(r'^blogs/cat/(?P<nombre>[\w-]+)/$', BlogCatListView.as_view(), name='blogscat_list'),
    url(r'^$', HomeView.as_view(), name='blogs_home'),

]

