from django.contrib import admin
from blog import models
# Register your models here.
admin.site.register(models.Articulo)
admin.site.register(models.Comentario)
admin.site.register(models.Noticia)

