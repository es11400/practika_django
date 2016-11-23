from django.core.serializers import json
from rest_framework import validators

from blogs.models import blogs
from cuentame.settings import API_URL, MEDIA_ROOT
from entradas.models import post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):

    idUsuario = serializers.SerializerMethodField('id_usuario')
    nombreUsuario = serializers.SerializerMethodField('nombre_usuario')
    nombreBlog = serializers.SerializerMethodField('nombre_blog')
    urlImagen = serializers.SerializerMethodField('url_imagen')

    def id_usuario(self, foo):
        return "{0}".format(foo.blog.usuario.id)

    def nombre_usuario(self, foo):
        return "{0} {1}".format(foo.blog.usuario.first_name, foo.blog.usuario.last_name)

    def nombre_blog(self, foo):
        return "{0}".format(foo.blog.nombre)

    def url_imagen(self, foo):
        return '%s%s' % (MEDIA_ROOT, foo.imagen)

    def validate_blog(self, foo):
        if foo.usuario.id != self.context['request'].user.id:
            raise serializers.ValidationError("Este blog no pertenece al usuario")
        return foo


    class Meta:
        model = post
        fields = ("id", "blog", "nombreBlog", "idUsuario", "nombreUsuario", "fecha", "cat", "titulo", "texto_corto", "texto_largo", "imagen", "urlImagen", "visible", "creado_el", "modificado_el",)


class PostListSerializer(PostSerializer):

    verUrl = serializers.SerializerMethodField('ver_url')

    def ver_url(self, foo):
        return '%s/%s/%s' % (API_URL, foo.__class__.__name__, foo.id)


    class Meta(PostSerializer.Meta):
        fields = ("id", "blog", "cat", "nombreUsuario", "titulo", "texto_corto", "urlImagen", "fecha", "verUrl",)
