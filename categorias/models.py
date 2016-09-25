from django.db import models
from django.conf import settings

VISIBILIDAD = getattr(settings, 'VISIBILIDAD', None)

# Create your models here.
class categorias(models.Model):

    nombre = models.CharField(max_length=50)
    creado_el = models.DateTimeField(auto_now_add=True)
    modificado_el = models.DateTimeField(auto_now=True)
    visible = models.CharField(max_length=2, choices=VISIBILIDAD, default='SI')

    def __str__(self):
        return self.nombre