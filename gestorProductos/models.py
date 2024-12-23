from django.db import models

# Create your models 


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.PositiveIntegerField()
    stock = models.IntegerField(default=0)
    descripcion = models.TextField()
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, default=1)
    imagen = models.TextField(default='')
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.nombre
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(default='')

    def __str__(self):
        return self.nombre
    
