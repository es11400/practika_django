from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from rest_framework.generics import get_object_or_404

from blogs.models import blogs, User
from categorias.models import categorias
from cuentame.settings import VISIBLE_SI
from entradas.models import post


class HomeView(View):

    def get(self, request):
        """
        Renderiza el home con un listado de post visibles de todos los blogs
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """
        # recupera todas los post visibles de la base de datos
        posts = post.objects.filter(visible=VISIBLE_SI).order_by('-creado_el')
        cat = categorias.objects.filter(visible=VISIBLE_SI).order_by('nombre')
        context = {'post_list': posts, 'categoria_list': cat}
        return render(request, 'entradas/inicio.html', context)

class BlogListView(ListView):

    model = blogs
    context_object_name = 'blog_list'
    template_name = 'blogs/blog_list.html'

    def get(self, request):
        result = super().get(request)
        return result

class BlogUserListView(ListView):

    model = post
    context_object_name = 'postuser_list'
    template_name = 'entradas/bloguser_list.html'

    def get_queryset(self):
        self.user = get_object_or_404(User, username=self.args[0])
        return post.objects.filter(visible=VISIBLE_SI).order_by('-creado_el')

class BlogCatListView(ListView):

    model = post
    context_object_name = 'postcategorias_list'
    template_name = 'entradas/blogcat_list.html'

    def get_queryset(self):
        self.cat = get_object_or_404(categorias, nombre=self.args[0])
        return post.objects.filter(visible=VISIBLE_SI, cat=self.cat).order_by('-creado_el')
