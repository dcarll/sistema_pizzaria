from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Ingredientes(models.Model):
    nome = models.CharField(max_length=255)
    pizza = models.ForeignKey("Pizza", on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'ingrediente'
        verbose_name_plural = 'ingredientes'
class Pizza(models.Model):
    nome = models.CharField(max_length=255)
    ingredientes = models.ManyToManyField(Ingredientes)
    descricao_pizza = models.TextField()

class Comentario(models.Model):
    titulo = models.CharField(max_length=255)
    texto = models.TextField()
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'comentario'
        verbose_name_plural = 'comentarios' 


    

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'pizza'
        verbose_name_plural = 'pizzas'


class Pedido(models.Model):
    titulo = models.CharField(max_length=255)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    pizza = models.ForeignKey(Pizza, on_delete=models.DO_NOTHING)
    descricao = models.TextField()

    def __str__(self):
        return self.titulo
    class Meta:
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'


