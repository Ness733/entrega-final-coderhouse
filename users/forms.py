from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from ckeditor.fields import RichTextFormField
from django.contrib.auth.models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']
        

class UserEditForm(UserChangeForm):
    password = None
    email = forms.EmailField(label="Ingrese su email:")
    last_name = forms.CharField(label="Apellido")
    first_name = forms.CharField(label="Nombre")
    imagen = forms.ImageField(widget=forms.FileInput, required=False)
    descripcion = forms.CharField(widget=forms.Textarea, required=False, max_length=255)
    link = forms.URLField(required=False)

    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name', 'imagen', 'link']