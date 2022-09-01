from django.db import models

class Base(models.Model):
    criado = models.DateTimeField(auto_now_add=True)
    publicado = models.DateTimeField(auto_now=True)
    modificado = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True