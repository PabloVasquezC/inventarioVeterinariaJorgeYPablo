from django.db import models

# Create your models 


class Venta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    total_venta = models.DecimalField(max_digits=10, decimal_places=2)
    numero_boleta = models.IntegerField(default=None)

    def __str__(self):
        return str([self.fecha, self.total_venta, self.numero_boleta])
