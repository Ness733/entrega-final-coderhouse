from django.db import models


# Create your models here.
class Articulo(models.Model):
    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=30)
    cuerpo = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self) -> str:
        return self.titulo + " - " + self.subtitulo
    
    class Meta:
        ordering = ["titulo", "fecha"]

    
    
class Comentario(models.Model):
    # articulo = models.ForeignKey(Articulo, related_name="comentario", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=20)
    cuerpo = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self) -> str:
        return self.titulo
    
    class Meta:
        ordering = ["titulo", "fecha"]
    

class Usuario(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    
    def __str__(self) -> str:
        return self.username
    
class Noticia(models.Model):
    titulo = models.CharField(max_length=30)
    cuerpo = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self) -> str:
        return self.titulo