from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from rest_framework.generics import get_object_or_404

from blogs.models import blogs, User
from categorias.models import categorias
from cuentame.settings import VISIBLE_SI
from entradas.models import post
from users.forms import LoginForm

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
        error_message = ""
        login_form = LoginForm()

        context = {'post_list': posts, 'categoria_list': cat, 'error': error_message, 'login_form': login_form}
        return render(request, 'entradas/inicio.html', context)

    def post(self, request):
        """
        Gestiona el login de un usuario
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """
        error_message = ""
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('pwd')
            user = authenticate(username=username, password=password)
            if user is None:
                error_message = "Usuario o contraseña incorrecto"
            else:
                if user.is_active:
                    django_login(request, user)
                    return redirect(request.GET.get('next', '/'))
                else:
                    error_message = "Cuenta de usuario inactiva"
        context = {'error': error_message, 'form': login_form}
        return render(request, 'users/login.html', context)

class BlogListView(ListView):
    """Renderizamos la lista de Blogs"""
    model = blogs
    context_object_name = 'blog_list'
    template_name = 'blogs/blog_list.html'

    def get_context_data(self, **kwargs):
        """Añadimos la categorias al contexto"""
        error_message = ""
        login_form = LoginForm()
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['categoria_list'] = categorias.objects.all()
        context['error'] = error_message
        context['login_form'] = login_form
        return context

    def get(self, request):
        """Añadimos los blogs registrados al contexto"""
        result = super().get(request)
        return result

class BlogPostListView(ListView):
    """Renderizamos los post de un blog"""
    model = post
    context_object_name = 'postblog_list'
    template_name = 'entradas/blogpost_list.html'

    def get_context_data(self, **kwargs):
        """Añadimos la categorias al contexto"""
        error_message = ""
        login_form = LoginForm()
        context = super(BlogPostListView, self).get_context_data(**kwargs)
        context['categoria_list'] = categorias.objects.all()
        context['blog'] = get_object_or_404(blogs, id=self.kwargs.get('blogId', None))
        context['error'] = error_message
        context['login_form'] = login_form
        return context

    def get_queryset(self):
        """Añadimos los post de un blog pasado por parametro blogId"""
        self.blog = get_object_or_404(blogs, id=self.kwargs.get('blogId', None))
        return post.objects.filter(visible=VISIBLE_SI, blog=self.blog).order_by('-creado_el')

class BlogUserListView(ListView):
    """Renderizamos los post de un usuario"""
    model = post
    context_object_name = 'postuser_list'
    template_name = 'entradas/bloguser_list.html'

    def get_context_data(self, **kwargs):
        """Añadimos la categorias al contexto"""
        error_message = ""
        login_form = LoginForm()
        context = super(BlogUserListView, self).get_context_data(**kwargs)
        context['categoria_list'] = categorias.objects.all()
        context['usuario'] = get_object_or_404(User, username=self.kwargs.get('username', None))
        context['error'] = error_message
        context['login_form'] = login_form
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
        error_message = ""
        login_form = LoginForm()
        context = super(BlogCatListView, self).get_context_data(**kwargs)
        context['categoria_list'] = categorias.objects.all()
        context['error'] = error_message
        context['login_form'] = login_form
        return context

    def get_queryset(self):
        """Añadimos al contexto los posts de una determinada categoria, tomando el parametro nombre"""
        self.cat = get_object_or_404(categorias, nombre=self.kwargs.get('nombre', None))
        return post.objects.filter(visible=VISIBLE_SI, cat=self.cat).order_by('-creado_el')

class BlogCatUserListView(ListView):
    """Renderizamos los post un usuario de una determinada categoria"""
    model = post
    context_object_name = 'postcatuseregorias_list'
    template_name = 'entradas/blogcatuser_list.html'

    def get_context_data(self, **kwargs):
        """Añadimos la categorias al contexto"""
        error_message = ""
        login_form = LoginForm()
        context = super(BlogCatUserListView, self).get_context_data(**kwargs)
        context['categoria_list'] = categorias.objects.all()
        context['error'] = error_message
        context['login_form'] = login_form
        return context

    def get_queryset(self):
        """Añadimos al contexto los posts de un usuario y una categoria, tomando el parametro nombre de la categoria y username para el usuario"""
        self.cat = get_object_or_404(categorias, nombre=self.kwargs.get('nombre', None))
        self.user = get_object_or_404(User, username=self.kwargs.get('username', None))
        return post.objects.filter(visible=VISIBLE_SI, blog__usuario= self.user, cat=self.cat).order_by('-creado_el')

class BlogUserDetailView(View):
    """ Renderizamos el detalle de un post
        parametros : categoria y usuario
    """

    def get(self, request, username, postId):
        """
        Renderiza el detalle de una imagen
        :param request: objeto HttpRequest con los datos de la petición
        :param pk: clave primaria de la foto a recuperar
        :return: objeto HttpResponse con los datos de la respuesta
        """
        error_message = ""
        login_form = LoginForm()
        possible_post = post.objects.filter(id=postId)

        if len(possible_post) == 0:
            return HttpResponseNotFound("La imagen que buscas no existe")
        elif len(possible_post) > 1:
            return HttpResponse("Múltiples opciones", status=300)

        post_select = possible_post[0]
        context = {'post': post_select, 'error': error_message, 'login_form': login_form}
        return render(request, 'entradas/bloguser_post.html', context)