from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):

    username = forms.CharField(label="Nombre de usuario")
    pwd = forms.CharField(label="Contraseña", widget=forms.PasswordInput())

class SignUpForm(forms.Form):

    nombre = forms.CharField(label="Nombre")
    apellidos = forms.CharField(label="Apellidos")
    email = forms.EmailField(label="Correo electrónico")
    username = forms.CharField(label="Nombre de usuario")
    pwd = forms.CharField(label="Contraseña", widget=forms.PasswordInput())
    pwd2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput())

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(("El usuario existe, pruebe otro."))

    def clean(self):
        if 'pwd' in self.cleaned_data and 'pwd2' in self.cleaned_data:
            if self.cleaned_data['pwd'] != self.cleaned_data['pwd2']:
                raise forms.ValidationError(("Las contraseñas deben coincidir"))
        return self.cleaned_data