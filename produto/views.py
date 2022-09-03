from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, TemplateView
from .models import Pizza
# Create your views here.
class ProdutoView(ListView):
    model = Pizza
    template_name = 'produtos.html'

