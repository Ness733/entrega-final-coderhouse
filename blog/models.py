from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class Articulo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=30)
    cuerpo = RichTextField()
    fecha = models.DateTimeField(auto_now_add=True, editable=False)
    imagen = models.ImageField(upload_to='post_imgs', null=True, blank=True)
    

    def __str__(self) -> str:
        return self.titulo + " - " + self.subtitulo
    
    class Meta:
        ordering = ["titulo", "fecha"]

    
    
class Comentario(models.Model):
    user = models.ForeignKey(User, editable=False, null=True, on_delete=models.SET_NULL)
    comment = models.ForeignKey(Articulo, related_name="comentarios", on_delete=models.CASCADE, null=True)
    titulo = models.CharField(max_length=20)
    cuerpo = RichTextField()
    fecha = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ['-fecha']

    def __str__(self):
        return '%s - %s - %s' % (self.titulo, self.cuerpo, self.user)
    

    def __str__(self) -> str:
        return '%s - %s' % (self.user, self.titulo)
    
    class Meta:
        ordering = ["titulo", "fecha"]
    
class Noticia(models.Model):
    titulo = models.CharField(max_length=30)
    cuerpo = RichTextField()
    fecha = models.DateTimeField(auto_now_add=True, editable=False)
    

    def __str__(self) -> str:
        return self.titulo
    
class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    descripcion = RichTextField()
    link = models.URLField(null=True, blank=True)
    imagen = models.ImageField(upload_to='avatars', null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.user}"