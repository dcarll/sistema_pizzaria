from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, TemplateView
from .models import Pizza
# Create your views here.
class ProdutoView(ListView):
    model = Pizza
    paginate_by = 6
    context_object_name = 'produtos'
    template_name = 'produto/produtos.html'

class DetalheProduto(DetailView):
    model = Pizza
    context_object_name = 'produto'
    template_name = 'produto/detalhe.html'
    slug_url_kwarg = 'slug'


