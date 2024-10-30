from typing import Any
from django import forms
from .models import Pessoa

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'idade': forms.NumberInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self) -> dict[str, Any]:
        cleaned_data = super().clean()
        idade = cleaned_data.get('idade')
        nome = cleaned_data.get('nome')
        if nome and len(nome.split()) < 2:
            self.add_error('nome', 'Nome completo é obrigatório.')

        if idade and idade < 18:
            self.add_error('idade', 'Idade deve ser maior ou igual a 18 anos.')
        return cleaned_data
        