# Generated by Django 5.1 on 2024-11-29 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestorProductos', '0003_categoria_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.TextField(default=''),
        ),
    ]