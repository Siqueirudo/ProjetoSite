from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Categoria, Produto, Carrinho, Pedido, ItemPedido

admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Carrinho)
admin.site.register(Pedido)
admin.site.register(ItemPedido)
