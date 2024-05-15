from django.shortcuts import render
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from .models import CustomUser
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView

User = CustomUser
# Create your views here.

def logout_view(request):
    logout(request)
    return redirect("login")


class RegisterUser(TemplateView):
    def get(self, request):
        form = SignUpForm()
        return render(request, "accounts/register.html", {"form": form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                # Autentica o usuário e redireciona para o painel de controle
                return redirect("dashboard")
            else:
                # Se o usuário não for autenticado, pode ser uma questão de integridade do banco de dados
                return redirect("login")
        else:
            # Se o formulário não for válido, retorna o formulário com uma mensagem de erro
            return render(request, "accounts/register.html", {"form": form, "error_message": "Form is not valid"})
    

class LoginUsuario(LoginView):
    template_name = 'accounts/login.html'

    def form_invalid(self, form):
        username = form.cleaned_data.get('username')
        user_exists = User.objects.filter(username=username).exists()

        error_messages = {
            'invalid_login': gettext_lazy('Verifique o usuário e senha e tente novamente.'),
            'inactive': gettext_lazy('Usuário inativo.'),
        }
        
        AuthenticationForm.error_messages = error_messages

        return super().form_invalid(form)

