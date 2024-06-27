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
from funcionario.forms import NovoFunciForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from datetime import timedelta
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import FormView
from funcionario.forms import ContactForm
from funcionario.models import Funcionario
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
import os
from dotenv import load_dotenv
load_dotenv()
def pagamento():
    import mercadopago
    # Adicione as credenciais
    sdk = mercadopago.SDK(f"{os.getenv('CREDEN')}")

    request = {
        "items": [
            {
                "id": "1",
                "title": "Prime Portal BR",
                "description": "Portal de ferramentas Online",
                "quantity": 1,
                "currency_id": "BRL",
                "unit_price": 39.90,
            },
        ],
        
        "back_urls": {
            "success": "https://primeportalbr.com/aprovado/",
            
        },
        "auto_return": "approved",
        }

    preference_response = sdk.preference().create(request)
    preference = preference_response["response"]
    return preference['init_point']

class DashBoardView(LoginRequiredMixin, TemplateView):
    template_name = 'home/dashboard.html'
    form_class = NovoFunciForm

    def get(self, request):
        form = self.form_class()
        user = self.request.user
        autenticado = user.is_authenticated

        # Agregar avaliações por mês
        avaliacoes_por_mes = (
            Avaliacao.objects.filter(usuario=user)
            .annotate(month=TruncMonth('data'))
            .values('month')
            .annotate(total=Count('id'))
            .order_by('month')
        )
        total_avaliacoes = Avaliacao.objects.filter(usuario=user).count()
        try:
            init_point = pagamento()
        except Exception:
            init_point = None
        if user.pagamento_atrasado:
            user.status_pagamento = False
            print(f"O pagamento do usuário {user.username} está atrasado!")
        # Transformar os dados em um formato adequado para o gráfico
        total_avlc = {DateFormat(avaliacao['month']).format('M'): avaliacao['total'] for avaliacao in avaliacoes_por_mes}
        
        context = {
            'form': form,
            'autenticado': autenticado,
            'total_avlc': json.dumps(total_avlc),
            'total_av':total_avaliacoes,
            'unidades':Unidade.objects.filter(usuario=user).order_by('-id'),
            'pagar':init_point,
            'user':request.user,

        }
        return render(request, self.template_name, context)


def home(request):
    return HttpResponse('<h1> Pagina INicial</h1>')