from django.contrib import admin
from .models import Cliente, Produto

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email']

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['preco', 'imagem', 'titulo', 'cliente']