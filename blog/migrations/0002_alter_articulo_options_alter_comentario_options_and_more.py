# Generated by Django 4.2.3 on 2023-08-14 21:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articulo',
            options={'ordering': ['titulo', 'fecha']},
        ),
        migrations.AlterModelOptions(
            name='comentario',
            options={'ordering': ['titulo', 'fecha']},
        ),
        migrations.AddField(
            model_name='articulo',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comentario',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]