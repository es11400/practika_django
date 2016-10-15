from rest_framework.serializers import ModelSerializer

from imagenes.models import Imagenes


class ImagenesSerializer(ModelSerializer):

    class Meta:
        model = Imagenes