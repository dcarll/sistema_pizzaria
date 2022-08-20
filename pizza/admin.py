from django.contrib import admin

from .models import Pedido, Pizza, Comentario, Ingredientes

# Register your models here.

admin.site.register(Pedido)
admin.site.register(Pizza)
admin.site.register(Comentario)
admin.site.register(Ingredientes)

"""
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'get_ingrediantes', 'descricao_pizza')
    
    def get_ingrediantes(self, request):
        ing = request.objects.get('ingredientes')
        return f'{self.ing[:50]}'

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'usuario', 'pizza', 'get_texto')

    def get_texto(self, request):
        obs = request.objects.get('observacao')
        return f'{self.obs[:50]}'

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'pizza', 'usuario')



@admin.register(Ingredientes)
class IngredientesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
"""