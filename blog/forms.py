from django import forms
from .models import Articulo, Comentario, Noticia
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from ckeditor.fields import RichTextFormField


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = "__all__"

class ComentaryForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = "__all__"

class NewsForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = "__all__"

class UserEditForm(UserChangeForm):
    password = None
    email = forms.EmailField(label="Ingrese su email:")
    last_name = forms.CharField(label="Apellido")
    first_name = forms.CharField(label="Nombre")
    imagen = forms.ImageField(widget=forms.FileInput, required=False)
    descripcion = RichTextFormField()
    link = forms.URLField(required=False)

    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name', 'imagen', 'descripcion', 'link']

class SearchArticle(forms.Form):
    titulo = forms.CharField(required=False)

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']
        
