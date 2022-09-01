from django.db import models
from utils.base_class import Base
from django.contrib.auth.models import User
from produto.models import Pizza

class Comentario(Base):
    titulo = models.CharField(max_length=255)
    texto = models.TextField()
    pizza = models.ForeignKey(Pizza, null=True, on_delete=models.CASCADE, related_name='pizza_comentario')
    usuario = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='usuario_comentario')

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'comentario'
        verbose_name_plural = 'comentarios'     
