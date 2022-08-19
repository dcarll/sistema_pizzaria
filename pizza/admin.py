from django.contrib import admin

from .models import Pedido, Pizza, Comentario, Ingredientes

# Register your models here.

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ingredientes', 'descricao_pizza')