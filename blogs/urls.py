from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from blogs.api import BlogModelViewSet
from blogs.views import HomeView, BlogListView, BlogUserListView, BlogCatListView, BlogUserDetailView, BlogPostListView, BlogCatUserListView

router = DefaultRouter()
router.register('api/1.0/blogs', BlogModelViewSet, base_name='api_blogs_')

urlpatterns = [
    # url(r'^create$', PhotoCreationView.as_view(), name='photos_create'),
    url(r'^blogs$', BlogListView.as_view(), name='blogs_list'),
    url(r'^blogs/(?P<blogId>[0-9]+)$', BlogPostListView.as_view(), name='blogspost_list'),
    url(r'^blogs/(?P<username>[\w-]+)/$', BlogUserListView.as_view(), name='blogsuser_list'),
    url(r'^blogs/(?P<username>[\w-]+)/(?P<postId>[0-9]+)$', BlogUserDetailView.as_view(), name='blogsuser_post'),
    url(r'^blogs/cat/(?P<nombre>[\w-]+)/$', BlogCatListView.as_view(), name='blogscat_list'),
    url(r'^blogs/cat/(?P<nombre>[\w-]+)/(?P<username>[\w-]+)$', BlogCatUserListView.as_view(), name='blogscatuser_list'),
    url(r'^$', HomeView.as_view(), name='blogs_home'),

    # API URLS
    url(r'', include(router.urls))
]

