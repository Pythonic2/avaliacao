from typing import Any
from django.db.models.query import QuerySet
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from funcionario.models import Funcionario
from django.views.generic import CreateView, ListView,DeleteView, UpdateView,TemplateView, DetailView
from funcionario.forms import ContactForm
from django.http import  HttpResponseRedirect
from funcionario.models import Funcionario
from django.contrib.auth import get_user_model
import logging
logger = logging.getLogger(__name__)
from django.contrib.auth import user_logged_in
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import authenticate
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import user_logged_in
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from .forms import SignUpForm,NovoFunciForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from datetime import timedelta
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import ContactForm  # Substitua pelo caminho real do seu formulário
from .models import Funcionario, Avaliacao,Unidade,AdministradorUnidade
from django.http import JsonResponse

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




class DashBoardView(LoginRequiredMixin,TemplateView):
    template_name = 'home/dashboard.html'
    form_class = NovoFunciForm
    def get(self, request):
        form = self.form_class()
        user = self.request.user
        autenticado = user.is_authenticated
        funcionario_existe = Funcionario.DoesNotExist
        
        lista = Funcionario.objects.filter(usuario=user).order_by('-id')
        print(lista)
        for funcionario in lista:
            funcionario.total_avaliacoes = Avaliacao.objects.filter(funcionario=funcionario).count()
        print(f"##############{user}#################")
        try:
            
            # Contagem de avaliações "Bom" para atendimento
            avaliacoes_bom_atendimento = Avaliacao.objects.filter(funcionario=funcionario, atendimento='Bom').count()
            regular_atendimento = Avaliacao.objects.filter(funcionario=funcionario, atendimento='Regular ').count()
            regular_higiene = Avaliacao.objects.filter(funcionario=funcionario, higiene='Regular ').count()
            # Contagem de avaliações "Ruim" para atendimento
            avaliacoes_ruim_atendimento = Avaliacao.objects.filter(funcionario=funcionario, atendimento='Ruim').count()
            # Contagem de avaliações "Bom" para higiene
            avaliacoes_bom_higiene = Avaliacao.objects.filter(funcionario=funcionario, higiene='Bom').count()
            # Contagem de avaliações "Ruim" para higiene
            avaliacoes_ruim_higiene = Avaliacao.objects.filter(funcionario=funcionario, higiene='Ruim').count()
            total_avaliacoes = Avaliacao.objects.filter(funcionario=funcionario).count()

        
            data_atual = timezone.now()

            # Data de 7 dias atrás
            data_sete_dias_atras = data_atual - timedelta(days=7)

            # Filtrar avaliações dos últimos 7 dias para o funcionário
            avaliacoes_ultimos_sete_dias = Avaliacao.objects.filter(funcionario=funcionario, data__gte=data_sete_dias_atras, data__lte=data_atual)

            # Contagem de avaliações dos últimos 7 dias
            total_avaliacoes_ultimos_sete_dias = avaliacoes_ultimos_sete_dias.count()
            print("Total de avaliações nos últimos 7 dias para o funcionário:", total_avaliacoes_ultimos_sete_dias)

        except Exception as e:
            lista= []
            total_avaliacoes = 0
            
        context = {
            'form':form,
            'autenticado':autenticado,
            'funcionarios':lista,
            'tot':total_avaliacoes
        }
        print(context['funcionarios'])
        return render(request,self.template_name,context)
        

class ListFuncionarios(LoginRequiredMixin,ListView):
    model = Funcionario

    template_name = 'home/tables-bootstrap-tables.html'
    def get(self, request):
        user = self.request.user
        user = self.request.user
        autenticado = user.is_authenticated
        if autenticado:
            lista = Funcionario.objects.filter(usuario=user)
        else:
            lista = ''
        return render(request, self.template_name,{"page_obj":lista,"autenticado":autenticado})
    
class FuncionarioDetailView(LoginRequiredMixin,DetailView):
    model = Funcionario
    template_name = 'funcionario_detail.html'
    def get_queryset(self):
        user = self.request.user

        funcionario_id = self.kwargs['pk']
        return Funcionario.objects.filter(id=funcionario_id,usuario=user)



class AuthorCreateView(LoginRequiredMixin, FormView):
    form_class = NovoFunciForm
    success_url = reverse_lazy('create_funci')
    template_name = 'home/settings.html'
    def form_valid(self, form):
        funcionario = form.save(commit=False)
        funcionario.usuario = self.request.user
        funcionario.save()
        print('certo')
        return JsonResponse({'id':funcionario.id,'nome': funcionario.nome,'codigo':funcionario.codigo,'unidade':funcionario.unidade})  # Retornar o nome do funcionário

    def form_invalid(self, form):
        return JsonResponse({'error': 'Erro ao cadastrar funcionário.'}, status=400)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        autenticado = user.is_authenticated
        lista = Funcionario.objects.filter(usuario=user).order_by('-id')
        context['autenticado'] = autenticado
        context['funcionarios'] = lista
        context['msg'] = 'funcionou'
        
        return context
