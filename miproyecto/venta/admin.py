from django.contrib import admin
from .models import Categoria_prod, Producto, Boleta, Usuario

# Register your models here.

admin.site.register(Categoria_prod)
admin.site.register(Producto)
admin.site.register(Boleta)
admin.site.register(Usuario)
