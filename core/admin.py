from django.contrib import admin
from .models import Produto, Cliente

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')
## serve para registrar na área administrativa os modelos
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)

