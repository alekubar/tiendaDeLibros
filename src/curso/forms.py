from django import forms

from .models import *
from django.contrib.auth.models import User
class CursoForm(forms.ModelForm):
    class Meta:
        model=Curso
        fields = "__all__"

class ComisionForm(forms.ModelForm):
    class Meta:
        model=Comision
        fields = "__all__"
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}), 
            }


class AlumnoForm(forms.ModelForm):
    class Meta:
        model=Alumno
        fields = "__all__"
 
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirmar Contraseña")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "Las contraseñas no coinciden")
    def save(self, commit=True):
        user = super().save(commit=False)  # Crear el objeto User pero sin guardarlo aún
        user.set_password(self.cleaned_data["password"])  # Establecer la contraseña de manera segura
        if commit:
            user.save()  # Guardar el usuario en la base de datos
        return user