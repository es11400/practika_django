from django.conf import settings
from django.db import models

from cuentame.my_settings import *
from blogs.models import blogs
from categorias.models import categorias

# VISIBILIDAD = getattr(settings, 'VISIBILIDAD', None)

def media_url(instance, nombrefichero):

    return "%s/%s" %(instance.blog.id, nombrefichero)

class post(models.Model):

    blog = models.ForeignKey(blogs)
    titulo = models.CharField(max_length=150, blank=True)
    texto_corto = models.CharField(max_length=255)
    texto_largo = models.TextField(null=True, blank=True)
    fecha = models.DateTimeField()
    imagen = models.ImageField(upload_to=media_url, null=True, blank=True)
    creado_el = models.DateTimeField(auto_now_add=True)
    modificado_el = models.DateTimeField(auto_now=True)
    visible = models.CharField(max_length=2, choices=VISIBILIDAD, default='SI')
    cat = models.ManyToManyField(categorias)

    def __str__(self):
        return self.titulo