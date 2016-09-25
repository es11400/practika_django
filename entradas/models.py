from django.conf import settings
from django.db import models


from blogs.models import blogs

VISIBILIDAD = getattr(settings, 'VISIBILIDAD', None)

def media_url(instance, nombrefichero):

    return "%s/%s/%s" %(instance.blog.id, str(instance.id), nombrefichero)

class post(models.Model):

    blog = models.ForeignKey(blogs)
    titulo = models.CharField(max_length=150, blank=True)
    texto_corto = models.CharField(max_length=255)
    texto_largo = models.TextField(null=True, blank=True)
    fecha = models.DateTimeField(auto_now=True)
    imagen = models.ImageField(upload_to=media_url, null=True, blank=True)
    creado_el = models.DateTimeField(auto_now_add=True)
    modificado_el = models.DateTimeField(auto_now=True)
    visible = models.CharField(max_length=2, choices=VISIBILIDAD, default='SI')

    def __str__(self):
        return self.titulo