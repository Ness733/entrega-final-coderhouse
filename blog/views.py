from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.
def index(request):
    return render(request, "index.html")

class ArticlesView(ListView):
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

class NewsViews(ListView):
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

class ArticleCreateView(CreateView):
    model = Articulo
    template_name = 'create_article.html'
    fields = ["titulo", "subtitulo", "cuerpo", 'imagen']
    success_url = reverse_lazy("Artículos")

    def form_valid(self, form):
        form.instance.imagen = self.request.FILES['imagen'].name if 'imagen' in self.request.FILES else None
        return super().form_valid(form)

class ArticleUpdate(UpdateView):
    model = Articulo
    template_name = "update_article.html"
    success_url = reverse_lazy("Artículos")
    fields = ["titulo", "subtitulo", "cuerpo", "imagen"]

class ArticleDelete(DeleteView):
    model = Articulo
    template_name = "delete_article.html"
    success_url = reverse_lazy("Artículos")

class ArticleDetails(DetailView):
    model = Articulo
    context_object_name = "articulo"
    template_name = "details_article.html"

class NewsCreateView(CreateView):
    model = Noticia
    template_name = 'create_news.html'
    fields = ["titulo", "cuerpo"]
    success_url = reverse_lazy("Noticias")

class CommentCreateView(CreateView):
    model = Comentario
    template_name = 'create_comment.html'
    fields = ["titulo", "cuerpo"]
    success_url = reverse_lazy("Artículos")

    def form_valid(self, form):
        form.instance.comment_id = self.kwargs['pk']
        return super(CommentCreateView, self).form_valid(form)

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
        if self.request.user.is_authenticated:
            return redirect("index")
        return response
    
def EditProfileView(request):
    usuario = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            if form.cleaned_data.get('imagen'):
                usuario.avatar.imagen = form.cleaned_data.get('imagen')
                usuario.avatar.save()
            
            form.save()
            return render(request, 'index.html')
    else:
        form = UserEditForm(initial={'imagen': usuario.avatar.imagen},instance=request.user)
    return render(request, 'update_profile.html', {'form': form, 'usuario': usuario})
    
class CustomLogoutView(LogoutView):
    template_name = 'logout.html'

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=password)

            login(request, user)

            return render(request, 'index.html', {"mensaje": f"Bienvenido {user.username}"})