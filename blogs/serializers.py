from rest_framework import serializers
from blogs.models import blogs
from cuentame.settings import API_URL


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = blogs


class BlogListSerializer(BlogSerializer):
    verUrl = serializers.SerializerMethodField('ver_url')
    nombreUsuario = serializers.SerializerMethodField('nombre_usuario')

    def ver_url(self, foo):
        return '%s/%s/%s' % (API_URL, foo.__class__.__name__, foo.id)

    def nombre_usuario(self, foo):
        return "{0} {1}".format(foo.usuario.first_name, foo.usuario.last_name)

    class Meta(BlogSerializer.Meta):
        fields = ("id", "nombre", "usuario", "nombreUsuario", "visible", "verUrl")
