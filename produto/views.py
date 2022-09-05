from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, TemplateView
from .models import Pizza
# Create your views here.
class ProdutoView(ListView):
    model = Pizza
    paginate_by = 2
    template_name = 'produtos.html'


