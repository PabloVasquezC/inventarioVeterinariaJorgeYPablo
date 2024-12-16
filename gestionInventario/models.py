from django.db import models

from datetime import datetime

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=200)
    cantidad = models.IntegerField(default=0)
    stock = models.IntegerField()
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    ingresado_por = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=datetime.now)
    imagen = models.TextField(default='')

    def __str__(self):
        return self.nombre  

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
