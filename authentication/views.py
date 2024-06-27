from django.shortcuts import render
from django.http.response import HttpResponse as HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from .models import CustomUser
from django.views.generic import TemplateView
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
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
@login_required
def pagamento_aprovado(request):
    import json
    parametros = request.GET.dict()  # Converte QueryDict para um dicionário comum
    print(parametros)
    if parametros['status'] == 'approved':
        user = request.user
        usuario = CustomUser.objects.get(username=user)
        usuario.status_pagamento = True
        usuario.data_pagamento = timezone.now()
        usuario.data_cobrar = timezone.now() + timedelta(days=30)
        usuario.save()
        return render(request,'accounts/retorno_pagamento.html',{'infos':'aprovado'})
    else:
        return render(request,'accounts/retorno_pagamento.html',{'infos':'recusado'})


