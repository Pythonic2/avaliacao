from django import forms
from unidade.models import Unidade
from administrador_unidade.models import AdministradorUnidade

class NovaUnidadeForm(forms.ModelForm):
    nome = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nome Estabelecimento",
                "class": "form-control"
            }
        ))
    

    end = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Endreço",
                "class": "form-control"
            }
        ))
    
    administrador = forms.ModelChoiceField(
                queryset= AdministradorUnidade.objects.all(),
                empty_label="Select Administrador",
                widget=forms.Select(attrs={'class': 'form-control'})
            )

    class Meta:
        model = Unidade
        fields = ('nome', 'end','administrador')