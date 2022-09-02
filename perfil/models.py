from tabnanny import verbose
from django.db import models
from utils.base_class import Base
from django.contrib.auth.models import User
from endereco.models import Endereco
from utils.validacpf import valida_cpf
import re

# Create your models here.
class Perfil(Base):
    nome = models.OneToOneField(User, on_delete=models.CASCADE)
    endereco = models.ManyToManyField(Endereco)
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return f'{self.nome}'

    def clean(self):
         error_messages = {}

         cpf_enviado = self.cpf or None
         cpf_salvo = None
         perfil = Perfil.objects.filter(cpf=cpf_enviado).first()

         if perfil:
             cpf_salvo = perfil.cpf

             if cpf_salvo is not None and self.pk != perfil.pk:
                error_messages['cpf'] = 'CPF já existe.'

         if not valida_cpf(self.cpf):
            error_messages['cpf'] = 'Digite um CPF válido'
        
         if error_messages:
             raise ValidationError(error_messages)
    
    class Meta:
        verbose_name = 'Pefil'
        verbose_name_plural = 'Perfis'


    
    
