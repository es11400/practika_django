from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


class LoginForm(forms.Form):

    username = forms.CharField(label=_("Nombre de usuario"))
    pwd = forms.CharField(label=_("Contraseña"), widget=forms.PasswordInput())

class SignUpForm(forms.Form):

    nombre = forms.CharField(label=_("Nombre"))
    apellidos = forms.CharField(label=_("Apellidos"))
    email = forms.EmailField(label=_("Correo electrónico"))
    username = forms.CharField(label=_("Nombre de usuario"))
    pwd = forms.CharField(label=_("Contraseña"), widget=forms.PasswordInput())
    pwd2 = forms.CharField(label=_("Repetir Contraseña"), widget=forms.PasswordInput())

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError((_("El usuario existe, pruebe otro.")))

    def clean(self):
        if 'pwd' in self.cleaned_data and 'pwd2' in self.cleaned_data:
            if self.cleaned_data['pwd'] != self.cleaned_data['pwd2']:
                raise forms.ValidationError((_("Las contraseñas deben coincidir")))
        return self.cleaned_data