from django import forms
from .models import AdministradorUnidade

class NovoAdministradorForm(forms.ModelForm):
    nome = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nome Administrador",
                "class": "form-control"
            }
        ))
    

    cargo = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Supervisor, Administrador, Gerente ...",
                "class": "form-control"
            }
        ))

    
    class Meta:
        model = AdministradorUnidade
        fields = ('nome', 'cargo')