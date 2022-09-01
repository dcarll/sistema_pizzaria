from django.db import models
from produto.models import Base
from utils.base_class import Base
from django.contrib.auth.models import User
from produto.models import Pizza

# Create your models here.
class Avaliacao(Base):
    tituto = models.CharField(max_length=255)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario')
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    descricao = models.TextField()
    nota = models.DecimalField(max_digits=3, decimal_places=2)
    
    def __str__(self):
        return self.tituto 

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"
    