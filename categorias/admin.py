from django.contrib import admin
from categorias.models import categorias

class CategoriasAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'creado_el', 'visible',)
    list_filter = ('nombre', 'visible',)
    search_fields = ('nombre',)

admin.site.register(categorias, CategoriasAdmin)