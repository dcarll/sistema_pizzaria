from django.urls import path
from .views import ProdutoView, DetalheProduto

app_name = 'produto'

urlpatterns = [
    path('', ProdutoView.as_view(), name='lista'),
    path('<slug>', DetalheProduto.as_view(), name='detalhe'),

]