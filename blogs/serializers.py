from rest_framework import serializers
from blogs.models import blogs
from cuentame.settings import API_URL
from entradas.models import post


class BlogSerializer(serializers.ModelSerializer):
    cuantosPost = serializers.SerializerMethodField('cuantos_post')

    def cuantos_post(self, foo):
        return post.objects.filter(blog=foo.id).count()

    class Meta:
        model = blogs
        fields = ["id", "nombre", "cuantosPost", "usuario", "visible", "creado_el", "modificado_el"]


class BlogListSerializer(BlogSerializer):
    verUrl = serializers.SerializerMethodField('ver_url')
    nombreUsuario = serializers.SerializerMethodField('nombre_usuario')


    def ver_url(self, foo):
        return '%s/%s/%s' % (API_URL, foo.__class__.__name__, foo.id)

    def nombre_usuario(self, foo):
        return "{0} {1}".format(foo.usuario.first_name, foo.usuario.last_name)


    class Meta(BlogSerializer.Meta):
        fields = ("id", "nombre", "cuantosPost", "usuario", "nombreUsuario", "visible", "verUrl")
