from django.shortcuts import render
from django.views import View

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
        posts = post.objects.filter(visible=VISIBLE_SI).order_by('-created_at')
        context = {'posts_list': posts}
        return render(request, 'entradas/inicio.html', context)
