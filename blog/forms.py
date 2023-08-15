from django import forms
from .models import Articulo, Comentario, Usuario

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = "__all__"

class ComentaryForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = "__all__"

class UserForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"

class SearchArticle(forms.Form):
    titulo = forms.CharField(required=False)