from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Ingredientes(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'ingrediente'
        verbose_name_plural = 'ingredientes'
'''
    def set_default_ingredientes():
	    return Ingredientes.objects.get_or_create(nome='padrão')[0] #objeto ou boolena
'''
class Pizza(models.Model):
    nome = models.CharField(max_length=255)
    ingredientes = models.ManyToManyField(Ingredientes, blank=True,)
    descricao_pizza = models.TextField(blank=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'pizza'
        verbose_name_plural = 'pizzas'

    def get_ingredientes(self):
        return "\n".join([p.ingredientes for p in self.ingrediente.all()])

class Comentario(models.Model):
    titulo = models.CharField(max_length=255)
    texto = models.TextField()
    pizza = models.ForeignKey(Pizza, null=True, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'comentario'
        verbose_name_plural = 'comentarios'     

    


class Pedido(models.Model):
    titulo = models.CharField(max_length=255)
    usuario = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
    pizza = models.ForeignKey(Pizza, null=True, on_delete=models.DO_NOTHING)
    observacao = models.TextField(blank=True)

    def __str__(self):
        return self.titulo
    class Meta:
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
    
    


