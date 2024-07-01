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
    logo = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "placeholder": "logo",
                "class": "form-control"
            }
        ))
    cor_logo = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'color'}),
        label='Cor da Logo',
        required=False,
    )

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
        fields = ('username', 'logo', 'cor_logo', 'email', 'password1', 'password2')

class SignUpFormLogo():
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    logo = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "placeholder": "logo",
                "class": "form-control"
            }
        ))
    cor_logo = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'color'}),
        label='Cor da Logo',
        required=False,
    )

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
        fields = ('username', 'logo', 'cor_logo', 'email', 'password1', 'password2')


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['logo', 'cor_logo']
        widgets = {
            'logo': forms.FileInput(attrs={'class': 'form-control'}),
            'cor_logo': forms.TextInput(attrs={'type': 'color', 'class': 'form-control'}),
        }
