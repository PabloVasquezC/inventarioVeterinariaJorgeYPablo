# Generated by Django 5.1 on 2024-12-03 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestorProductos', '0009_producto_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.PositiveIntegerField(),
        ),
    ]