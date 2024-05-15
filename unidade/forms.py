from django import forms
from unidade.models import Unidade


class NovaUnidadeForm(forms.ModelForm):
    nome = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "nome",
                "class": "form-control"
            }
        ))
    

    end = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Matrícula",
                "class": "form-control"
            }
        ))
    
   

    class Meta:
        model = Unidade
        fields = ('nome', 'end')