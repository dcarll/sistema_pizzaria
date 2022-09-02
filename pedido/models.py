from tabnanny import verbose
from django.db import models
from utils.base_class import Base
from django.contrib.auth.models import User
from produto.models import Pizza

# Create your models here.
class Pedido(Base):
    usuario = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='usuario_pedido')
    pizza = models.ManyToManyField(Pizza)
    observacao = models.TextField(blank=True)
    status = models.CharField(max_length=1,
                                default='C',
                                choices=(
                                    ('C', 'Criado'),
                                    ('A', 'Aprovado'),
                                    ('R','Reprovado'),
                                    ('P', 'Pendente'),
                                    ('E', 'enviado'),
                                    ('F', 'Finalizado'),
                                )
    )

    def __str__(self):
        return f'Pedido N. {self.pk}'

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

class ItemPedido(Base):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.CharField(max_length=255)
    produto_id = models.PositiveIntegerField()
    preco = models.FloatField()
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f'Item do {self.pedido}'

    class Meta:
        verbose_name = 'Item do pedido'
        verbose_name_plural ='Itens do pedido'