from django import forms

class UsuarioForm(forms.Form):
    username = forms.CharField(max_length=150, label="Usuario")
    email = forms.EmailField(label="Correo")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
