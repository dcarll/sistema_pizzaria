from django.urls import path
from . import views

app_name = 'endereco'

urlpatterns = [
    path('', views.EnderecoView.as_view(), name='endereco'),
]