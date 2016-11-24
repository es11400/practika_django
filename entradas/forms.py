from django.conf import settings
from django.forms.widgets import DateInput, FileInput, DateTimeInput
from django.forms import ModelForm, ChoiceField, ModelChoiceField
from django.forms.widgets import Select
from django.forms.widgets import SelectMultiple
from django.forms.widgets import TextInput
from django.forms.widgets import Textarea
from rest_framework import request
from cuentame.my_settings import *
from blogs.models import blogs
from entradas.models import post

# VISIBILIDAD = getattr(settings, 'VISIBILIDAD', None)

class CreatePostForm(ModelForm):


    class Meta:

        model = post
        fields = ['blog', 'titulo', 'texto_corto', 'texto_largo', 'fecha', 'imagen', 'visible', 'cat']
        labels = {
                    'blog': 'Elija un Blog',
                    'titulo': 'Título',
                    'texto_corto': 'Texto descriptivo',
                    'texto_largo': 'Texto completo',
                    'fecha': 'Fecha de publicación',
                    'imagen': 'Seleccione una imagen',
                    'visible': '¿Visible?',
                    'cat': 'Categorías',
                }
        exclude = ['creado_el', 'modificado_el']
        widgets = {
            'blog': Select,
            'texto_corto': TextInput(),
            'texto_largo': Textarea(attrs={'class': 'materialize-textarea', 'cols': '80', 'rows': '16'}),
            'fecha': DateInput(format='d/m/Y h:i:s'),
            # 'fecha': DateTimeInput(attrs={'class': 'datepicker', 'placeholder': 'dd/mm/aaaa HH:MM:SS'}),
            'imagen': FileInput(),
            'visible': Select(attrs={'label': '¿Visible?', 'class': 'input-field'}),
            'cat': SelectMultiple(attrs={'label': 'Categorías', 'class': 'multiple'}),
        }
