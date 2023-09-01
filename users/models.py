from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Create your models here.
class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    descripcion = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    imagen = models.ImageField(upload_to='avatars', null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.user}"