from django.db import models

class DetalleVenta(models.Model):
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    id_producto = models.ForeignKey('gestionInventario.Producto', on_delete=models.CASCADE)
    id_venta = models.ForeignKey('registroVentas.Venta', on_delete=models.CASCADE)

    def __str__(self):
        return str([self.cantidad, self.precio, self.producto, self.venta])