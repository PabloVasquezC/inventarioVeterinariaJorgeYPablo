from django.db import models

# Create your models here.
<<<<<<< HEAD
=======

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    stock = models.IntegerField()
    descripcion = models.TextField()
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos', null=True, blank=True)
    def __str__(self):
        return self.nombre
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    def __str__(self):
        return self.nombre
>>>>>>> b7c8b65ad882801ac505324bcf6a6e51e29ecf76
