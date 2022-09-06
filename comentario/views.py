from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class ComentarioView(TemplateView):
    template_name = 'comentario/comentario.html'
