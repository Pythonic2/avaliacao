from django import forms
from .models import Cliente

class NovoClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'celular', 'nascimento']
        labels = {
            'nome': 'Nome (Obrigatório)',
            'email': 'Email',
            'celular': 'Telefone para contato',
            'nascimento': 'Data de Nascimento',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
            'nascimento': forms.DateInput(attrs={'class': 'form-control','type':'date'}),
            
        }
