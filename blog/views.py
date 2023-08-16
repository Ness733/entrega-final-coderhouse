from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.
@login_required
def index(request):
    return render(request, "index.html")

class ArticlesView(TemplateView):
    template_name = "articles.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["articulo"] = Articulo.objects.all()
        context["comentario"] = Comentario.objects.all()
        return context

# def articles(request):
#     comentario = Comentario.objects.all()
#     articulo = Articulo.objects.all()
#     return render(request, "articles.html", {"articulo": articulo, "comentario": comentario})
@login_required
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

# def news(request):
#     noticia = Noticia.objects.all()
#     return render(request, "news.html", {'noticia': noticia})

class ArticleCreateView(CreateView):
    model = Articulo
    template_name = 'create_article.html'
    fields = ["titulo", "subtitulo", "cuerpo"]
    success_url = reverse_lazy("Artículos")

class ArticleUpdate(UpdateView):
    model = Articulo
    template_name = "update_article.html"
    success_url = reverse_lazy("Artículos")
    fields = ["titulo", "subtitulo", "cuerpo"]

class ArticleDelete(DeleteView):
    model = Articulo
    template_name = "delete_article.html"
    success_url = reverse_lazy("Artículos")

class ArticleDetails(DetailView):
    model = Articulo
    context_object_name = "articulo"
    template_name = "details_article.html"
    


# def crear_Articulo(request):
#     if request.method == 'POST':
#         form = ArticleForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('Artículos')
#     else:
#         form = ArticleForm()
#     return render(request, 'create_article.html', {'form': form})

class NewsCreateView(CreateView):
    model = Noticia
    template_name = 'create_news.html'
    fields = ["titulo", "cuerpo"]
    success_url = reverse_lazy("Noticias")

# def crear_Noticia(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('Noticias')
#     else:
#         form = NewsForm()
#     return render(request, 'create_news.html', {'form': form})

class CommentCreateView(CreateView):
    model = Comentario
    template_name = 'create_comment.html'
    fields = ["titulo", "cuerpo"]
    success_url = reverse_lazy("Artículos")

# def crear_Comentario(request):
#     if request.method == 'POST':
#         form = ComentaryForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('Artículos')
#     else:
#         form = ComentaryForm()
#     return render(request, 'create_comment.html', {'form': form})

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
    
class CustomLogoutView(LogoutView):
    next_page = 'login'

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=password)

            login(request, user)

            return render(request, 'index.html', {"mensaje": f"Bienvenido {user.username}"})