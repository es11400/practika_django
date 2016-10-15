from rest_framework.viewsets import ModelViewSet

from imagenes.models import Imagenes
from imagenes.serializers import ImagenesSerializer


class ImagenesModelViewSet(ModelViewSet):

    queryset = Imagenes.objects.all()
    serializer_class = ImagenesSerializer
