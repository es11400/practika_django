from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from cuentame.settings import VISIBLE_SI
from entradas.models import post
from categorias.models import categorias
from users.forms import LoginForm, SignUpForm


class Inc():
    def formularios(self, request):
        """
        Gestiona el login de un usuario
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """
        posts = post.objects.filter(visible=VISIBLE_SI).order_by('-creado_el')
        cat = categorias.objects.filter(visible=VISIBLE_SI).order_by('nombre')
        error_message = ""
        login_form = LoginForm(request.POST)
        signup_form = SignUpForm(request.POST)

        if 'login' in request.POST:
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('pwd')
                user = authenticate(username=username, password=password)
                if user is None:
                    error_message = "Usuario o contraseña incorrecto"
                    context = {'post_list': posts, 'categoria_list': cat, 'error': error_message,
                               'login_form': login_form}
                    return render(request, 'entradas/inicio.html', context)
                else:
                    if user.is_active:
                        django_login(request, user)
                        return redirect(request.GET.get('next', '/'))
                    else:
                        error_message = "Cuenta de usuario inactiva"
                        context = {'post_list': posts, 'categoria_list': cat, 'error': error_message,
                                   'login_form': login_form}
                        return render(request, 'entradas/inicio.html', context)

            elif not login_form.is_valid():
                context = {'post_list': posts, 'categoria_list': cat, 'error': error_message, 'login_form': login_form}
                return render(request, 'entradas/inicio.html', context)

        if 'registro' in request.POST:
            if signup_form.is_valid():
                user = User.objects.create_user(
                    first_name=signup_form.cleaned_data['nombre'],
                    last_name=signup_form.cleaned_data['apellidos'],
                    email=signup_form.cleaned_data['email'],
                    username=signup_form.cleaned_data['username'],
                    password=signup_form.cleaned_data['pwd'],
                )
                django_login(request, user)
                signup_form = SignUpForm()
                context = {'post_list': posts, 'categoria_list': cat, 'error': error_message, 'login_form': login_form,
                           'signup_form': signup_form}
                return render(request, 'entradas/inicio.html', context)

            elif not signup_form.is_valid():
                context = {'post_list': posts, 'categoria_list': cat, 'error': error_message, 'login_form': login_form,
                           'signup_form': signup_form}
                return render(request, 'entradas/inicio.html', context)
