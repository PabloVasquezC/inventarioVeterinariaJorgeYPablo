# Generated by Django 5.1 on 2024-11-28 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestorProductos', '0002_remove_categoria_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='descripcion',
            field=models.TextField(default=''),
        ),
    ]
