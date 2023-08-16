from django.urls import path
from . import views


urlpatterns = [

    path("", views.index, name="index",),
    path("articles/", views.ArticlesView.as_view(), name="Artículos",),
    path("about/", views.about, name="Sobre Nosotros",),
    path("results/", views.searchResults, name="Resultados",),
    path("create_article/", views.ArticleCreateView.as_view(), name="Crear Artículo",),
    path("article/<pk>/detalle", views.ArticleDetails.as_view(), name="Detalle Artículo",),
    path("article/<pk>/editar", views.ArticleUpdate.as_view(), name="Editar Artículo",),
    path("article/<pk>/eliminar", views.ArticleDelete.as_view(), name="Eliminar Artículo",),
    path("create_comment/", views.CommentCreateView.as_view(), name="Crear Comentario",),
    path("news/", views.NewsViews.as_view(), name="Noticias",),
    path("news/<pk>/editar", views.NewsUpdate.as_view(), name="Editar Noticia",),
    path("news/<pk>/eliminar", views.NewsDelete.as_view(), name="Eliminar Noticia",),
    path("news/<pk>/detalle", views.NewsDetails.as_view(), name="Detalle Noticia",),
    path("create_news/", views.NewsCreateView.as_view(), name="Crear Noticia",),
    path("login/", views.CustomLoginView.as_view(), name="login",),
    path("register/", views.RegisterView.as_view(), name="register",),
    path("logout/", views.LogoutView.as_view(), name="logout",),
    


]