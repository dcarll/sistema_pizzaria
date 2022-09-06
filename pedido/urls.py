from django.urls import path
from . import views

app_name = 'pedido'

urlpatterns = [
    path('', views.PedidoView.as_view(), name='pedido'),
]