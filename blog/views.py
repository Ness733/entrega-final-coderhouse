from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from .models import Avatar

# Create your views here.
def index(request):
    return render(request, "index.html")

class ArticlesView(LoginRequiredMixin, ListView):
    model = Articulo
    context_object_name = "articulo"
    template_name = "articles.html"

def about(request):
    return render(request, "about.html")

def Login(request):
    return render(request, "login.html")

class NewsDetails(DetailView):
    model = Noticia
    context_object_name = "noticia"
    template_name = "details_news.html"

class NewsViews(LoginRequiredMixin, ListView):
    model = Noticia
    context_object_name = "noticia"
    template_name = "news.html"

class NewsUpdate(UpdateView):
    model = Noticia
    template_name = "update_news.html"
    success_url = reverse_lazy("Noticias")
    fields = ["titulo", "cuerpo"]

class NewsDelete(DeleteView):
    model = Noticia
    template_name = "delete_news.html"
    success_url = reverse_lazy("Noticias")

class ArticleCreateView(UserPassesTestMixin, CreateView):
    model = Articulo
    template_name = 'create_article.html'
    fields = ["titulo", "subtitulo", "cuerpo", 'imagen']
    success_url = reverse_lazy("Artículos")

    def form_valid(self, form):
        form.instance.imagen = self.request.FILES['imagen'].name if 'imagen' in self.request.FILES else None
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

class ArticleDetails(DetailView):
    model = Articulo
    context_object_name = "articulo"
    template_name = "details_article.html"

class NewsCreateView(CreateView):
    model = Noticia
    template_name = 'create_news.html'
    fields = ["titulo", "cuerpo"]
    success_url = reverse_lazy("Noticias")

class CommentDelete(DeleteView):
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


class CommentCreateView(CreateView):
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
def searchResults(request):
    articulo = []
    form = SearchArticle(request.GET)
    if form.is_valid():
        titulo = form.cleaned_data.get('titulo')

        if titulo:
            articulo = Articulo.objects.filter(titulo__icontains=titulo)

    return render(request, 'searchResults.html', {'form': form, 'articulo': articulo})

class RegisterView(CreateView):
    template_name = "register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    

class CustomLoginView(LoginView):
    template_name = "login.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        obj, created = Avatar.objects.get_or_create(user=self.request.user)
        if self.request.user.is_authenticated:
            return redirect("index")
        return response
    
def ProfileView(request):
    return render(request, 'details_profile.html')

    
def EditProfileView(request):
    usuario = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            datos_perfil = form.cleaned_data

            usuario.email = datos_perfil['email']
            usuario.first_name = datos_perfil['first_name']
            usuario.last_name = datos_perfil['last_name']
            usuario.avatar.descripcion = datos_perfil['descripcion']
            usuario.avatar.link = datos_perfil['link']

            if datos_perfil['imagen'] == False:
                usuario.avatar.imagen = None
            elif datos_perfil['imagen'] != None:
                usuario.avatar.imagen = datos_perfil['imagen']
            
            usuario.avatar.save()
            form.save()
            return render(request, 'details_profile.html')
    else:
        form = UserEditForm(initial={'email': usuario.email, 'first_name': usuario.first_name, 'last_name': usuario.last_name, 'imagen': usuario.avatar.imagen, 'descripcion': usuario.avatar.descripcion, 'link': usuario.avatar.link}, instance=request.user)
    return render(request, 'update_profile.html', {'form': form, 'usuario': usuario})
    
class CustomLogoutView(LogoutView):
    template_name = 'logout.html'
