from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin



# Create your views here.
def index(request):
    return render(request, "index.html")

class ArticlesView(LoginRequiredMixin, ListView):
    model = Articulo
    context_object_name = "articulo"
    template_name = "articles.html"

def about(request):
    return render(request, "about.html")

class NewsDetails(LoginRequiredMixin, DetailView):
    model = Noticia
    context_object_name = "noticia"
    template_name = "details_news.html"

class NewsViews(LoginRequiredMixin, ListView):
    model = Noticia
    context_object_name = "noticia"
    template_name = "news.html"

class NewsUpdate(UserPassesTestMixin, UpdateView):
    model = Noticia
    template_name = "update_news.html"
    success_url = reverse_lazy("Noticias")
    fields = ["titulo", "cuerpo"]

    def test_func(self) -> bool | None:
        return self.request.user.is_superuser

class NewsDelete(UserPassesTestMixin, DeleteView):
    model = Noticia
    template_name = "delete_news.html"
    success_url = reverse_lazy("Noticias")

    def test_func(self) -> bool | None:
        return self.request.user.is_superuser

class ArticleCreateView(UserPassesTestMixin, CreateView):
    model = Articulo
    template_name = 'create_article.html'
    fields = ["titulo", "subtitulo", "cuerpo", 'imagen']
    success_url = reverse_lazy("Artículos")

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    
    def test_func(self) -> bool | None:
        return self.request.user.is_superuser

class ArticleUpdate(UserPassesTestMixin, UpdateView):
    model = Articulo
    template_name = "update_article.html"
    success_url = reverse_lazy("Artículos")
    fields = ["titulo", "subtitulo", "cuerpo", "imagen"]

    def test_func(self) -> bool | None:
        return self.request.user.is_superuser

class ArticleDelete(UserPassesTestMixin, DeleteView):
    model = Articulo
    template_name = "delete_article.html"
    success_url = reverse_lazy("Artículos")

    def test_func(self) -> bool | None:
        return self.request.user.is_superuser

class ArticleDetails(LoginRequiredMixin, DetailView):
    model = Articulo
    context_object_name = "articulo"
    template_name = "details_article.html"

class NewsCreateView(UserPassesTestMixin, CreateView):
    model = Noticia
    template_name = 'create_news.html'
    fields = ["titulo", "cuerpo"]
    success_url = reverse_lazy("Noticias")

    def test_func(self) -> bool | None:
        return self.request.user.is_superuser

class CommentDelete(LoginRequiredMixin, DeleteView):
    model = Comentario
    template_name = 'delete_comment.html'

    
    def get_success_url(self) -> str:
        return reverse('Detalle Artículo', kwargs={'pk': self.object.comment_id})

class CommentUpdate(LoginRequiredMixin, UpdateView):
    model = Comentario
    template_name = 'update_comment.html'
    fields = ['titulo', 'cuerpo']

    def get_object(self, *args, **kwargs):
        obj = super().get_object(*args, **kwargs)
        if obj.user != self.request.user:
            raise PermissionError("No tiene permisos para editar este elemento!")
        return obj
    
    def get_success_url(self) -> str:
        return reverse('Detalle Artículo', kwargs={'pk': self.object.comment_id})


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comentario
    template_name = 'create_comment.html'
    fields = ["titulo", "cuerpo"]

    def form_valid(self, form):
        form.instance.comment_id = self.kwargs['pk']
        self.pk = form.instance.comment_id
        form.instance.user = self.request.user
        return super(CommentCreateView, self).form_valid(form)
    
    def get_success_url(self) -> str:
        return reverse('Detalle Artículo', kwargs={'pk': self.pk})

# buscador
@login_required
def searchResults(request):
    articulo = []
    form = SearchArticle(request.GET)
    if form.is_valid():
        titulo = form.cleaned_data.get('titulo')

        if titulo:
            articulo = Articulo.objects.filter(titulo__icontains=titulo)

    return render(request, 'searchResults.html', {'form': form, 'articulo': articulo})

