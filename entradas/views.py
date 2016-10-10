from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View

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
        new_post_form = CreatePostForm()
        context = {'new_post_form': new_post_form, 'message': message}
        return render(request, 'entradas/new_post.html', context)

    @method_decorator(login_required())
    def post(self, request):
        """
        Presenta el formulario para crear una foto y, en caso de que la petición sea POST la valida
        y la crea en caso de que sea válida
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """
        message = None
        # photo_with_user = Photo(owner=request.user)
        new_post_form = CreatePostForm(request.POST, request.FILES)
        if new_post_form.is_valid():
            new_photo = new_post_form.save()
            new_post_form = CreatePostForm()
            # message = 'Foto creada satisfactoriamente. <a href="/photos/{0}">Ver foto</a>'.format(new_photo.pk)

        context = {'new_post_form': new_post_form, 'message': message}
        return render(request, 'entradas/new_post.html', context)
