from django.contrib import admin
from .models import Produto, Cliente


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome',
                    'preco',
                    'estoque'
                    )


class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        '__str__',  # To_String que foi implementado no Model Cliente
        'email'
    )


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)
