# Generated by Django 4.2.3 on 2023-08-31 15:03

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_avatar_descripcion_avatar_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='descripcion',
            field=ckeditor.fields.RichTextField(default=''),
        ),
    ]
