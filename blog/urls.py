from django.urls import path
from . import views


urlpatterns = [

    path("", views.index, name="index",),
    path("articles/", views.articles, name="Artículos",),
    path("about/", views.about, name="Sobre Nosotros",),
    path("results/", views.searchResults, name="Resultados",),
    path("create_article/", views.crear_Articulo, name="Crear Artículo",),
    


]