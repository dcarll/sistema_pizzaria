from django.db import models
from utils.base_class import Base
from django.contrib.auth.models import User
from produto.models import Pizza

# Create your models here.
class Pedido(Base):
    titulo = models.CharField(max_length=255)
    usuario = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='usuario_pedido')
    pizza = models.ManyToManyField(Pizza)
    observacao = models.TextField(blank=True)
    @property
    def valor_total():
        pizza = self.pizza.all()
        preco_total = 0,0
        for p in pizza:
            preco_total += pizza.preco
        return preco_total

    def __str__(self):
        return self.titulo
    class Meta:
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'