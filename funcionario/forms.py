from django import forms
from funcionario.models import Funcionario
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

        
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
    

    codigo = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Matrícula",
                "class": "form-control"
            }
        ))
    
    unidade = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Unidade",
                "class": "form-control"
            }
        ))

    class Meta:
        model = Funcionario
        fields = ('nome', 'codigo','unidade')