from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View

from blogs.models import blogs
from entradas.forms import CreatePostForm


class NewPostView(View):

    @method_decorator(login_required())
    def get(self, request):
        """
        Presenta el formulario para crear un nuevo post de un blog
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """
        message = None
        CreatePostForm.base_fields['blog'] = forms.ModelChoiceField(queryset=blogs.objects.filter(usuario=request.user))
        new_post_form = CreatePostForm()
        context = {'new_post_form': new_post_form, 'message': message}
        return render(request, 'entradas/new_post.html', context)

    @method_decorator(login_required())
    def post(self, request):
        """
        Presenta el formulario para crear un nuevo Post y, en caso de que la petición sea POST la valida
        y la crea en caso de que sea válida
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """
        message = None
        new_post_form = CreatePostForm(request.POST, request.FILES)
        if new_post_form.is_valid():
            new_post_form = new_post_form.save()
            # message = 'Post creado satisfactoriamente. <a href="/blogs/{0}/{1}">Ver Post</a>'.format(request.user, new_post_form.pk)
            # new_post_form = CreatePostForm()
            return redirect('blogs/{0}/{1}'.format(request.user, new_post_form.pk))


        context = {'new_post_form': new_post_form, 'message': message}
        return render(request, 'entradas/new_post.html', context)
