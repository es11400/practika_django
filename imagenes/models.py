from django.db import models

from cuentame.settings import MEDIA_URL

class Imagenes(models.Model):

    url = models.FileField(upload_to=MEDIA_URL)
    nombre = models.CharField(max_length=250)
