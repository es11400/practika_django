from django.contrib.auth.models import User
from django.db import models
from cuentame.my_settings import VISIBILIDAD

# VISIBILIDAD = getattr(my_settings, 'VISIBILIDAD', None)

# Create your models here.
class blogs(models.Model):

    nombre = models.CharField(max_length=200)
    usuario = models.ForeignKey(User)
    creado_el = models.DateTimeField(auto_now_add=True)
    modificado_el = models.DateTimeField(auto_now=True)
    visible = models.CharField(max_length=2, choices=VISIBILIDAD, default='SI')

    def __str__(self):
        return self.nombre