from django import forms
from funcionario.models import Funcionario
from unidade.models import Unidade

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Funcionario
        fields = ['nome','codigo']

    def __init__(self, *args, **kwargs):
        ''' remove any labels here if desired
        '''
        super(ContactForm, self).__init__(*args, **kwargs)
        # you can also remove labels of built-in model properties
        self.fields['nome'].label = ''
        self.fields['nome'].widget.attrs['class'] = 'form-control'
        self.fields['nome'].widget.attrs['id'] = 'nome'
        self.fields['nome'].widget.attrs['placeholder'] = 'Nome'

        self.fields['codigo'].label = ''
        self.fields['codigo'].widget.attrs['class'] = 'form-control'
        self.fields['codigo'].widget.attrs['id'] = 'codigo'
        self.fields['codigo'].widget.attrs['placeholder'] = 'exemplo@exemplo.com'



class NovoFunciForm(forms.ModelForm):
    nome = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "nome",
                "class": "form-control"
            }
        ))
    

    matricula = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Matrícula",
                "class": "form-control"
            }
        ))
    
    unidade = forms.ModelChoiceField(
            queryset=Unidade.objects.all(),
            empty_label="Select Unidade",
            widget=forms.Select(attrs={'class': 'form-control'})
        )

    class Meta:
        model = Funcionario
        fields = ('nome', 'matricula','unidade')