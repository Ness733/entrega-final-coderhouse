# Generated by Django 4.2.3 on 2023-08-25 01:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0017_avatar_delete_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='post_imgs'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='user',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
