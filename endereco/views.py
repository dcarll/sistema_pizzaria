from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class EnderecoView(TemplateView):
    template_name = 'endereco/endereco.html'

