# Generated by Django 4.2.3 on 2023-09-01 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
    ]