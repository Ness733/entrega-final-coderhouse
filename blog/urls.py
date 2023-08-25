from django.urls import path
from . import views

# imagenes
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path("", views.index, name="index",),
    path("articles/", views.ArticlesView.as_view(), name="Artículos",),
    path("about/", views.about, name="Sobre Nosotros",),
    path("results/", views.searchResults, name="Resultados",),
    path("create_article/", views.ArticleCreateView.as_view(), name="Crear Artículo",),
    path("article/<int:pk>/detalle", views.ArticleDetails.as_view(), name="Detalle Artículo",),
    path("article/<int:pk>/editar", views.ArticleUpdate.as_view(), name="Editar Artículo",),
    path("article/<int:pk>/eliminar", views.ArticleDelete.as_view(), name="Eliminar Artículo",),
    path("news/", views.NewsViews.as_view(), name="Noticias",),
    path("create_comment/<int:pk>", views.CommentCreateView.as_view(), name="Crear Comentario",),
    path("news/<int:pk>/editar", views.NewsUpdate.as_view(), name="Editar Noticia",),
    path("news/<int:pk>/eliminar", views.NewsDelete.as_view(), name="Eliminar Noticia",),
    path("news/<int:pk>/detalle", views.NewsDetails.as_view(), name="Detalle Noticia",),
    path("create_news/", views.NewsCreateView.as_view(), name="Crear Noticia",),
    path("login/", views.CustomLoginView.as_view(), name="login",),
    path("register/", views.RegisterView.as_view(), name="register",),
    path("profile_edit/", views.EditProfileView, name="Editar Perfil",),
    path("logout/", views.CustomLogoutView.as_view(), name="logout",),
    
    


]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)