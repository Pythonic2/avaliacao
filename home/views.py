from typing import Any
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from funcionario.models import Funcionario
from funcionario.models import Funcionario
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
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from datetime import timedelta
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import FormView
from funcionario.models import Funcionario
from django.http import JsonResponse
from funcionario.forms import NovoFunciForm
from avaliacao.models import Avaliacao
from django.views.generic import TemplateView
from unidade.models import Unidade

class DashBoardView(LoginRequiredMixin,TemplateView):
    template_name = 'home/dashboard.html'
    form_class = NovoFunciForm
    def get(self, request):
        form = self.form_class()
        user = self.request.user
        autenticado = user.is_authenticated
        funcionario_existe = Funcionario.DoesNotExist
        
        lista = Funcionario.objects.filter(usuario=user).order_by('-id')
        unidade = Unidade.objects.filter(usuario=user).order_by('-id')
        print(unidade)
        
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