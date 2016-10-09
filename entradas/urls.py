
from django.conf.urls import url


from entradas.views import NewPostView

urlpatterns = [
    # Entradas URLS
    url(r'^newpost', NewPostView.as_view(), name='new_post'),
]