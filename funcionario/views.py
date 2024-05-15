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
from django.utils import timezone
from datetime import timedelta
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import ContactForm
from .models import Funcionario
from django.http import JsonResponse
from avaliacao.models import Avaliacao
from unidade.models import Unidade
from unidade.forms import NovaUnidadeForm

class DashBoardView(LoginRequiredMixin,TemplateView):
    template_name = 'home/dashboard.html'
    form_class = NovoFunciForm
    def get(self, request):
        form = self.form_class()
        user = self.request.user
        autenticado = user.is_authenticated
        funcionario_existe = Funcionario.DoesNotExist
        
        lista = Funcionario.objects.filter(usuario=user).order_by('-id')
        for funcionario in lista:
            funcionario.total_avaliacoes = Avaliacao.objects.filter(funcionario=funcionario).count()
        try:
            
            avaliacoes_bom_atendimento = Avaliacao.objects.filter(funcionario=funcionario, atendimento='Bom').count()
            regular_atendimento = Avaliacao.objects.filter(funcionario=funcionario, atendimento='Regular ').count()
            regular_higiene = Avaliacao.objects.filter(funcionario=funcionario, higiene='Regular ').count()
            # Contagem de avaliações "Ruim" para atendimento
            avaliacoes_ruim_atendimento = Avaliacao.objects.filter(funcionario=funcionario, atendimento='Ruim').count()
            # Contagem de avaliações "Bom" para higiene
            avaliacoes_bom_higiene = Avaliacao.objects.filter(funcionario=funcionario, higiene='Bom').count()
            # Contagem de avaliações "Ruim" para higiene
            avaliacoes_ruim_higiene = Avaliacao.objects.filter(funcionario=funcionario, higiene='Ruim').count()
        except Exception as e:
            lista= []
            total_avaliacoes = 0
            
        context = {
            'form':form,
            'autenticado':autenticado,
            'funcionarios':lista,
            'total_avlc':total_avaliacoes
        }
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


def htmx_criar_funcionario(request):
    form = NovoFunciForm(request.POST)
    context = {}
    if form.is_valid():
        funcionario = form.save(commit=False)
        funcionario.usuario = request.user
        funcionario.save()
        context['success'] = f'usuario: "{funcionario.nome}" cadastrado com sucesso!'
        context['funcionarios'] = Funcionario.objects.all().order_by('-id')
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
        lista = Funcionario.objects.filter(usuario=user).order_by('-id')
        context['autenticado'] = autenticado
        context['funcionarios'] = lista
        context['msg'] = 'funcionou'
        context['form_unidade'] = form_unidade
        context['unidades'] = Unidade.objects.all().order_by('-id')
        return context