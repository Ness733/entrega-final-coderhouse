from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path("login/", views.CustomLoginView.as_view(), name="login",),
    path("register/", views.RegisterView.as_view(), name="register",),
    path("profile_edit/", views.EditProfileView, name="Editar Perfil",),
    path("change_password/", views.change_password, name="Cambiar Contraseña",),
    path("profile/<slug:username>", views.ProfileView, name="Perfil",),
    path("logout/", views.CustomLogoutView.as_view(), name="logout",),

]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)