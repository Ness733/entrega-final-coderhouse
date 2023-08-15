from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, "index.html")

def articles(request):
    comentario = Comentario.objects.all()
    articulo = Articulo.objects.all()
    return render(request, "articles.html", {"articulo": articulo, "comentario": comentario})

def about(request):
    return render(request, "about.html")

def news(request):
    noticia = Noticia.objects.all()
    return render(request, "news.html", {'noticia': noticia})

def crear_Articulo(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Artículos')
    else:
        form = ArticleForm()
    return render(request, 'create_article.html', {'form': form})

def crear_Noticia(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Noticias')
    else:
        form = NewsForm()
    return render(request, 'create_news.html', {'form': form})


def crear_Comentario(request):
    if request.method == 'POST':
        form = ComentaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Artículos')
    else:
        form = ComentaryForm()
    return render(request, 'create_comment.html', {'form': form})

# buscador
def searchResults(request):
    articulo = []
    form = SearchArticle(request.GET)
    if form.is_valid():
        titulo = form.cleaned_data.get('titulo')

        if titulo:
            articulo = Articulo.objects.filter(titulo__icontains=titulo)

    return render(request, 'searchResults.html', {'form': form, 'articulo': articulo})