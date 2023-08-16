# Generated by Django 4.2.3 on 2023-08-15 21:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_noticia_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='articulo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comentario', to='blog.articulo'),
            preserve_default=False,
        ),
    ]