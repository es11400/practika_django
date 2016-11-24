from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.utils.datetime_safe import datetime
from django.views import View
from django.views.generic import ListView, DetailView
from rest_framework.generics import get_object_or_404

from blogs.includes import Inc
from blogs.models import blogs, User
from categorias.models import categorias
from cuentame.settings import POSTxPAGINAS
from cuentame.my_settings import *

from entradas.models import post
from users.forms import LoginForm, SignUpForm
from entradas.forms import CreatePostForm


class HomeView(Inc, View):

    def get(self, request):
        """
        Renderiza el home con un listado de post visibles de todos los blogs
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """
        # recupera todas los post visibles de la base de datos
        posts = post.objects.filter(visible=VISIBLE_SI, fecha__lte=datetime.now()).order_by('-fecha')
        paginator = Paginator(posts, POSTxPAGINAS)
        page = request.GET.get('page')
        try:
            posts_pag = paginator.page(page)
        except PageNotAnInteger:
            posts_pag = paginator.page(1)
        except EmptyPage:
            posts_pag = paginator.page(paginator.num_pages)

        cat = categorias.objects.filter(visible=VISIBLE_SI).order_by('nombre')
        error_message = ""
        login_form = LoginForm()
        signup_form = SignUpForm()
        context = {'post_list': posts_pag, 'categoria_list': cat, 'error': error_message, 'login_form': login_form, 'signup_form': signup_form}
        return render(request, 'entradas/inicio.html', context)

    def post(self, request):
        return Inc.formularios(self, request)

class BlogListView(ListView):
    """Renderizamos la lista de Blogs"""
    model = blogs
    context_object_name = 'blog_list'
    template_name = 'blogs/blog_list.html'
    paginate_by = POSTxPAGINAS

    def get_context_data(self, **kwargs):
        """Añadimos la categorias al contexto"""
        error_message = ""
        login_form = LoginForm()
        signup_form = SignUpForm()
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['categoria_list'] = categorias.objects.all()
        context['error'] = error_message
        context['login_form'] = login_form
        context['signup_form'] = signup_form
        return context

    def get(self, request):
        """Añadimos los blogs registrados al contexto"""
        result = super().get(request)
        return result

    def post(self, request):
        return Inc.formularios(self, request)

class BlogPostListView(ListView):
    """Renderizamos los post de un blog"""
    model = post
    context_object_name = 'postblog_list'
    template_name = 'entradas/blogpost_list.html'
    paginate_by = POSTxPAGINAS

    def get_context_data(self, **kwargs):
        """Añadimos la categorias al contexto"""
        error_message = ""
        login_form = LoginForm()
        signup_form = SignUpForm()
        context = super(BlogPostListView, self).get_context_data(**kwargs)
        context['categoria_list'] = categorias.objects.all()
        context['blog'] = get_object_or_404(blogs, id=self.kwargs.get('blogId', None))
        context['error'] = error_message
        context['login_form'] = login_form
        context['signup_form'] = signup_form
        return context

    def get_queryset(self):
        """Añadimos los post de un blog pasado por parametro blogId"""
        self.blog = get_object_or_404(blogs, id=self.kwargs.get('blogId', None))
        return post.objects.filter(visible=VISIBLE_SI, fecha__lte=datetime.now(), blog=self.blog).order_by('-fecha')

    def post(self, request):
        return Inc.formularios(self, request)

class BlogUserListView(ListView):
    """Renderizamos los post de un usuario"""
    model = post
    context_object_name = 'postuser_list'
    template_name = 'entradas/bloguser_list.html'
    paginate_by = POSTxPAGINAS

    def get_context_data(self, **kwargs):
        """Añadimos la categorias al contexto"""
        error_message = ""
        login_form = LoginForm()
        signup_form = SignUpForm()
        context = super(BlogUserListView, self).get_context_data(**kwargs)
        context['categoria_list'] = categorias.objects.all()
        context['usuario'] = get_object_or_404(User, username=self.kwargs.get('username', None))
        context['error'] = error_message
        context['login_form'] = login_form
        context['signup_form'] = signup_form
        return context

    def post(self, request):
        return Inc.formularios(self, request)

    def get_queryset(self):
        """Añadimos los post de un un usuario pasado por parametro username"""
        self.user = get_object_or_404(User, username=self.kwargs.get('username', None))
        return post.objects.filter(visible=VISIBLE_SI, fecha__lte=datetime.now(), blog__usuario=self.user).order_by('-fecha')

class BlogCatListView(ListView):
    """Renderizamos los post de una determinada categoria"""
    model = post
    context_object_name = 'postcategorias_list'
    template_name = 'entradas/blogcat_list.html'
    paginate_by = POSTxPAGINAS

    def get_context_data(self, **kwargs):
        """Añadimos la categorias al contexto"""
        error_message = ""
        login_form = LoginForm()
        signup_form = SignUpForm()
        context = super(BlogCatListView, self).get_context_data(**kwargs)
        context['categoria_list'] = categorias.objects.all()
        context['error'] = error_message
        context['login_form'] = login_form
        context['signup_form'] = signup_form
        return context

    def post(self, request):
        return Inc.formularios(self, request)

    def get_queryset(self):
        """Añadimos al contexto los posts de una determinada categoria, tomando el parametro nombre"""
        self.cat = get_object_or_404(categorias, nombre=self.kwargs.get('nombre', None))
        return post.objects.filter(visible=VISIBLE_SI, fecha__lte=datetime.now(), cat=self.cat).order_by('-fecha')

class BlogCatUserListView(ListView):
    """Renderizamos los post un usuario de una determinada categoria"""
    model = post
    context_object_name = 'postcatuseregorias_list'
    template_name = 'entradas/blogcatuser_list.html'
    paginate_by = POSTxPAGINAS

    def get_context_data(self, **kwargs):
        """Añadimos la categorias al contexto"""
        error_message = ""
        login_form = LoginForm()
        signup_form = SignUpForm()
        context = super(BlogCatUserListView, self).get_context_data(**kwargs)
        context['categoria_list'] = categorias.objects.all()
        context['error'] = error_message
        context['login_form'] = login_form
        context['signup_form'] = signup_form
        return context

    def post(self, request):
        return Inc.formularios(self, request)

    def get_queryset(self):
        """Añadimos al contexto los posts de un usuario y una categoria, tomando el parametro nombre de la categoria y username para el usuario"""
        self.cat = get_object_or_404(categorias, nombre=self.kwargs.get('nombre', None))
        self.user = get_object_or_404(User, username=self.kwargs.get('username', None))
        return post.objects.filter(visible=VISIBLE_SI, fecha__lte=datetime.now(), blog__usuario= self.user, cat=self.cat).order_by('-fecha')

class BlogUserDetailView(View):
    """ Renderizamos el detalle de un post
        parametros : categoria y usuario
    """

    def get(self, request, username, postId):
        """
        Renderiza el detalle de un post
        :param request: objeto HttpRequest con los datos de la petición
        :param pk: clave primaria de la foto a recuperar
        :return: objeto HttpResponse con los datos de la respuesta
        """
        error_message = ""
        login_form = LoginForm()
        signup_form = SignUpForm()
        possible_post = post.objects.filter(id=postId)

        if len(possible_post) == 0:
            return HttpResponseNotFound("El post que buscas no existe")
        elif len(possible_post) > 1:
            return HttpResponse("Múltiples opciones", status=300)

        post_select = possible_post[0]
        context = {'post': post_select, 'error': error_message, 'login_form': login_form, 'signup_form': signup_form}
        return render(request, 'entradas/bloguser_post.html', context)

    def post(self, request):
        return Inc.formularios(self, request)