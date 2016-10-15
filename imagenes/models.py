from django.db import models

class Imagenes(models.Model):

    url = models.FileField(upload_to="uploads")
    nombre = models.CharField(max_length=250)
