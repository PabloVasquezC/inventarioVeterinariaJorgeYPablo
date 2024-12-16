from django.db import models

# Create your models 


class Venta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion
    
