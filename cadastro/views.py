from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from cadastro.forms import PessoaForm
from cadastro.models import Pessoa

class IndexView(CreateView):
    template_name = 'index.html'
    model = Pessoa
    form_class = PessoaForm
    success_url = '/listar/'

class PessoasListarView(ListView):
    template_name = 'list.html'
    model = Pessoa
    context_object_name = 'pessoas'

class PessoasEditarView(UpdateView):
    template_name = 'edit.html'
    model = Pessoa
    form_class = PessoaForm
    success_url = '/listar/'

class PessoaDeleteView(DeleteView):
    model = Pessoa
    template_name = 'delete.html'
    success_url = reverse_lazy('cadastro:listar')
