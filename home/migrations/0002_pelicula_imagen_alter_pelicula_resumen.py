# Generated by Django 4.1.2 on 2022-10-31 13:54

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='peliculas'),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='resumen',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
