from django import forms
from .models import Articulo, Comentario, Usuario, Noticia
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

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

class UserForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"

class SearchArticle(forms.Form):
    titulo = forms.CharField(required=False)

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields
