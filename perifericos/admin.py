from django.contrib import admin
from .models import Cliente, Produtos, Categoria


admin.site.register(Cliente)
admin.site.register(Produtos)
admin.site.register(Categoria)