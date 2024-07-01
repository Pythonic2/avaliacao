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
from .forms import NovoFunciForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import FormView
from .models import Funcionario
from django.http import JsonResponse
from unidade.models import Unidade
from unidade.forms import NovaUnidadeForm
from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.utils.dateformat import DateFormat
from datetime import datetime
from administrador_unidade.forms import NovoAdministradorForm
from administrador_unidade.models import AdministradorUnidade
from authentication.models import CustomUser
from authentication.forms import SignUpForm, EditProfileForm


class ListFuncionarios(LoginRequiredMixin,ListView):
    model = Funcionario
    template_name = 'home/tables-bootstrap-tables.html'

    def get(self, request):
        user = self.request.user
        autenticado = user.is_authenticated
        if autenticado:
            lista = Funcionario.objects.filter(usuario=user)
            unidades = Unidade.objects.filter(usuario=user)
        else:
            lista = ''
        return render(request, self.template_name,{"page_obj":lista,"autenticado":autenticado,'tete':'d-none','unidades':unidades})


def htmx_editar_funcionario(request, id):
    funcionario = Funcionario.objects.get(id=id)
    unidades = Unidade.objects.filter(usuario=request.user)
    print(unidades)
    context = {'funci': funcionario, 'tete': '','form':NovoFunciForm,'unidades':unidades}
    return render(request, 'includes/editar_funcionario.html', context)

def htmx_update_funcionario(request,id):
    funcionario = Funcionario.objects.get(id=id)
    novo_nome = request.POST.get('nome')
    nova_matriula = request.POST.get('matricula')
    nova_unidade = request.POST.get('unidade')
    nova_unidade = Unidade.objects.get(id=nova_unidade)
    funcionario.nome = novo_nome
    funcionario.matricula = nova_matriula
    funcionario.unidade = nova_unidade
    funcionario.usuario = funcionario.usuario
    funcionario.save()
    return redirect('list_funci')


def htmx_apagar_funcionario(request, id):
    funcionario = Funcionario.objects.get(id=id)
    funcionario.delete()
    context = {'funci': funcionario, 'tete': ''}
    return redirect('list_funci')



def htmx_editar_estabelecimento(request, id):
    unidade = Unidade.objects.get(id=id)
    administradores = AdministradorUnidade.objects.filter(usuario=request.user)
    context = {'estabelecimento': unidade, 'tete': '','administradores':administradores}
    return render(request, 'includes/editar_estabelecimento.html', context)


def htmx_update_estabelecimento(request,id):
    unidade = Unidade.objects.get(id=id)

    novo_nome = request.POST.get('nome')

    novo_end = request.POST.get('end')

    novo_admin = request.POST.get('administrador')


    novo_admin = AdministradorUnidade.objects.get(id=novo_admin)
    print(f' ------------ {novo_admin}')
    unidade.nome = novo_nome
    unidade.end = novo_end
    unidade.usuario = unidade.usuario
    unidade.administrador = novo_admin

    unidade.save()
    return redirect('list_funci')


def htmx_apagar_estabeleciento(request, id):
    unidade = Unidade.objects.get(id=id)
    unidade.delete()
    context = {'unidade': unidade}
    return redirect('list_funci')

def htmx_criar_funcionario(request):
    form = NovoFunciForm(request.POST)
    context = {}
    if form.is_valid():
        funcionario = form.save(commit=False)
        funcionario.usuario = request.user
        funcionario.save()
        user = request.user
        context['success'] = f'usuario: "{funcionario.nome}" cadastrado com sucesso!'
        context['funcionarios'] = Funcionario.objects.filter(usuario=user).order_by('-id')
        return render(request, 'includes/msg.html', context)
    else:
        context['erro']=form.errors
        return render(request, 'includes/msg.html', context)


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
        form_unidade = NovaUnidadeForm
        form_administrador = NovoAdministradorForm
        
        lista = Funcionario.objects.filter(usuario=user).order_by('-id')
        context['autenticado'] = autenticado
        context['funcionarios'] = lista
        context['msg'] = 'funcionou'
        context['form_unidade'] = form_unidade
        context['form_administrador'] = form_administrador
        context['unidades'] = Unidade.objects.filter(usuario=user).order_by('-id')
        context['administradores'] = AdministradorUnidade.objects.filter(usuario=user).order_by('-id')
        return context

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('editar_perfil')  # Redirecione para a página de perfil ou outra página de sua escolha
    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'includes/editar_perfil.html', {'form_logo': form})