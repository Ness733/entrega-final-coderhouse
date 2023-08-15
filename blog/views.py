from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, "index.html")

def articles(request):
    articulo = Articulo.objects.all()
    return render(request, "articles.html", {"articulo": articulo})

def about(request):
    return render(request, "about.html")

# def searchResults(request):
#     return render(request, "searchResults.html")

def crear_Articulo(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Artículos')
    else:
        form = ArticleForm()
    return render(request, 'create_article.html', {'form': form})

# buscador
def searchResults(request):
    articulo = []
    form = SearchArticle(request.GET)
    if form.is_valid():
        titulo = form.cleaned_data.get('titulo')

        if titulo:
            articulo = Articulo.objects.filter(titulo__icontains=titulo)

    return render(request, 'searchResults.html', {'form': form, 'articulo': articulo})