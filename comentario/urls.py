from django.urls import path
from . import views

app_name = 'comentario'

urlpatterns = [
    path('', views.ComentarioView.as_view(), name='comentario'),
]
