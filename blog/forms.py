from django import forms
from .models import Articulo, Comentario, Usuario, Noticia

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