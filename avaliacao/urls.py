from django.urls import path 
from . import views

app_name = 'avaliacao'

urlpatterns = [
    path('', views.AvaliacaoView.as_view(), name='avaliacao'),

]