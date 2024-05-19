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
from datetime import datetime
from django.db.models import Count
from django.utils.dateformat import DateFormat
import json
from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.utils.dateformat import DateFormat
from datetime import datetime
from administrador_unidade.forms import NovoAdministradorForm
from administrador_unidade.models import AdministradorUnidade



class ListFuncionarios(LoginRequiredMixin,ListView):
    model = Funcionario
    template_name = 'home/tables-bootstrap-tables.html'

    def get(self, request):
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
        context['unidades'] = Unidade.objects.all().order_by('-id')
        context['administradores'] = AdministradorUnidade.objects.all().order_by('-id')
        return context