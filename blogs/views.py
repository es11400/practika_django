from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
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
    """Renderizamos la lista de Blogs"""
    model = blogs
    context_object_name = 'blog_list'
    template_name = 'blogs/blog_list.html'

    def get_context_data(self, **kwargs):
        """Añadimos la categorias al contexto"""
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['categoria_list'] = categorias.objects.all()
        return context

    def get(self, request):
        """Añadimos los blogs registrados al contexto"""
        result = super().get(request)
        return result

class BlogUserListView(ListView):
    """Renderizamos los post de un usuario"""
    model = post
    context_object_name = 'postuser_list'
    template_name = 'entradas/bloguser_list.html'

    def get_context_data(self, **kwargs):
        """Añadimos la categorias al contexto"""
        context = super(BlogUserListView, self).get_context_data(**kwargs)
        context['categoria_list'] = categorias.objects.all()
        context['usuario'] = get_object_or_404(User, username=self.kwargs.get('username', None))
        return context

    def get_queryset(self):
        """Añadimos los post de un un usuario pasado por parametro username"""
        self.user = get_object_or_404(User, username=self.kwargs.get('username', None))
        return post.objects.filter(visible=VISIBLE_SI, blog__usuario=self.user).order_by('-creado_el')

class BlogCatListView(ListView):
    """Renderizamos los post de una determinada categoria"""
    model = post
    context_object_name = 'postcategorias_list'
    template_name = 'entradas/blogcat_list.html'

    def get_context_data(self, **kwargs):
        """Añadimos la categorias al contexto"""
        context = super(BlogCatListView, self).get_context_data(**kwargs)
        context['categoria_list'] = categorias.objects.all()
        return context

    def get_queryset(self):
        """Añadimos al contexto los posts de una determinada categoria, tomando el parametro nombre"""
        self.cat = get_object_or_404(categorias, nombre=self.kwargs.get('nombre', None))
        return post.objects.filter(visible=VISIBLE_SI, cat=self.cat).order_by('-creado_el')

class BlogUserDetailView(View):
    """ Renderizamos el detalle de un post
        parametros : categoria y usuario
    """
    # model = post
    # context_object_name = 'post'
    # template_name = 'entradas/blogcat_list.html'
    #
    # def get_context_data(self, **kwargs):
    #     """Añadimos la categorias al contexto"""
    #     context = super(BlogUserDetailView, self).get_context_data(**kwargs)
    #     context['categoria_list'] = categorias.objects.all()
    #     return context
    #
    # def get_queryset(self):
    #     # self.cat = get_object_or_404(categorias, nombre=self.kwargs.get('nombre', None))
    #     return post.objects.filter(visible=VISIBLE_SI, id=self.kwargs.get('postId', None))

    def get(self, request, username, postId):
        """
        Renderiza el detalle de una imagen
        :param request: objeto HttpRequest con los datos de la petición
        :param pk: clave primaria de la foto a recuperar
        :return: objeto HttpResponse con los datos de la respuesta
        """
        possible_post = post.objects.filter(id=postId)

        if len(possible_post) == 0:
            return HttpResponseNotFound("La imagen que buscas no existe")
        elif len(possible_post) > 1:
            return HttpResponse("Múltiples opciones", status=300)

        post_select = possible_post[0]
        context = {'post': post_select}
        return render(request, 'entradas/bloguser_post.html', context)