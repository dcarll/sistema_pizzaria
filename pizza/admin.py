'''
from django.contrib import admin

from .models import Pedido, Pizza, Comentario, Ingredientes, Avaliacao

# Register your models here.

#admin.site.register(Pedido)
#admin.site.register(Pizza)
admin.site.register(Comentario)
admin.site.register(Ingredientes)
admin.site.register(Avaliacao)

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'get_ingredientes', 'descricao_pizza')
    
    def get_ingredientes(self, obj):

        return ", ".join([p.nome for p in obj.ingredientes.all()])
    
    get_ingredientes.short_description = 'Ingredientes'

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'usuario', 'get_pizza', 'preco_total')

    preco_total = 0

    def get_preco_total(self, obj):
        for p in obj.pizza.preco:
            self.preco_total += int(p.preco)
        return self.preco_total




    def get_pizza(self, obj):
        return " ,".join([p.nome for p in obj.pizza.all()])
    
    get_pizza.short_description = "Pizza"

    
"""
@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'pizza', 'usuario')



@admin.register(Ingredientes)
class IngredientesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
"""

'''