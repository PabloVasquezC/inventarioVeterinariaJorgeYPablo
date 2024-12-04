from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Producto, Categoria

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock')  # Campos visibles en el admin
    list_filter = ('nombre',)  # Filtros laterales
    search_fields = ('nombre', 'descripcion')  # Campos buscables
    
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')