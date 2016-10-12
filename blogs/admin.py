from django.contrib import admin
from blogs.models import blogs

class BlogAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'nombre_usuario', 'creado_el', 'visible')
    list_filter = ('nombre', 'usuario', 'visible')
    search_fields = ('nombre', 'nombre_usuario')

    def nombre_usuario(self, blogs):
        return "{0} {1}".format(blogs.usuario.first_name, blogs.usuario.last_name)

    nombre_usuario.admin_order_field = 'usuario'
    nombre_usuario.short_description = 'Usuario'
admin.site.register(blogs, BlogAdmin)
