from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Venta

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'total_venta', 'numero_boleta') 
    list_filter = ('fecha',)  
    search_fields = ('numero_boleta',)  


