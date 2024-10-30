from django.urls import path
from .views import *

app_name = 'cadastro'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('listar/', PessoasListarView.as_view(), name='listar'),
    path('editar/<int:pk>/', PessoasEditarView.as_view(), name='editar'),
    path('deletar/<int:pk>/', PessoaDeleteView.as_view(), name='deletar'),
]