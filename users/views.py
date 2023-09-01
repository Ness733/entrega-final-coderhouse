from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

# 
from .models import Avatar
from .forms import *

# Create your views here.
def Login(request):
    return render(request, "login.html")

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
    
def ProfileView(request, username):
    user = User.objects.get(username=username)
    return render(request, 'details_profile.html', {'username':user})

    
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
