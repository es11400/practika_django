from rest_framework import serializers
from blogs.models import blogs


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = blogs


class BlogListSerializer(BlogSerializer):
    class Meta(BlogSerializer.Meta):
        fields = ("id", "nombre", "usuario", "visible")

        # def nombre_usuario(self, blogs):
        #     return "{0} {1}".format(blogs.usuario.first_name, blogs.usuario.last_name)