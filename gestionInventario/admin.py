from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Producto, Categoria

admin.site.register(Categoria)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio') 
    list_filter = ('fecha',)  
    search_fields = ('nombre',)  



