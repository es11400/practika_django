from django.contrib import admin
from django.utils.safestring import mark_safe

from entradas.models import post

class PostAdmin(admin.ModelAdmin):

    list_display = ('blog', 'ver_categorias', 'nombre_usuario', 'titulo', 'fecha', 'visible',)
    list_filter = ('blog', 'visible', 'cat',)
    ordering = ('blog',)
    search_fields = ('blog__nombre', 'titulo',)
    readonly_fields = ('ver_imagen',)

    fieldsets = (
        ("Blog y fecha", {
            'fields': ('blog', 'fecha',)
        }),
        ("Título y contenido", {
            'fields' : ('titulo', 'texto_corto', 'texto_largo')
        }),
        ("Imagen destacada", {
            'fields': ('imagen', 'ver_imagen'),
        }),
        ("Categorías y Visibilidad", {
            'fields': ('cat', 'visible')
        }),
    )

    def nombre_usuario(self, post):
        return "{0} {1}".format(post.blog.usuario.first_name, post.blog.usuario.last_name)

    def ver_imagen(self, post):
        if post.imagen != "":
            return mark_safe("<img style='width:100%;' src='/uploads/{0}'>".format(post.imagen))
        else:
            return mark_safe("<img style='width:50%;' src='/static/img/noFoto.png'>")

    def ver_categorias(self, obj):
        return "\n".join([a.nombre for a in obj.cat.all()])

    nombre_usuario.short_description = 'Usuario'
    ver_categorias.short_description = 'Categorías'

admin.site.register(post, PostAdmin)