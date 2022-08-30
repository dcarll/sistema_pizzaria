from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Base(models.Model):
    criado = models.DateTimeField(auto_now_add=True)
    publicado = models.DateTimeField(auto_now=True)
    modificado = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Ingredientes(Base):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'ingrediente'
        verbose_name_plural = 'ingredientes'

    def set_default_ingredientes():
	    return Ingredientes.objects.get_or_create(nome='padrão')[0] #objeto ou boolena

class Pizza(Base):
    nome = models.CharField(max_length=255)
    ingredientes = models.ManyToManyField(Ingredientes, blank=True,)
    descricao_pizza = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'pizza'
        verbose_name_plural = 'pizzas'

    def get_ingredientes(self):
        return "\n".join([p.ingredientes for p in self.ingrediente.all()])

class Comentario(Base):
    titulo = models.CharField(max_length=255)
    texto = models.TextField()
    pizza = models.ForeignKey(Pizza, null=True, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'comentario'
        verbose_name_plural = 'comentarios'     

    


class Pedido(Base):
    titulo = models.CharField(max_length=255)
    usuario = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    pizza = models.ManyToManyField(Pizza, null=False, blank=False )
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


class Avaliacao(Base):
    tituto = models.CharField(max_length=255)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    descricao = models.TextField()
    nota = models.DecimalField(max_digits=3, decimal_places=2)
    
    def __str__(self):
        return self.tituto 

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"
    
    


