from django.shortcuts import render
from django.http import HttpResponse
from .forms import NovaUnidadeForm
from .models import Unidade
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin



def htmx_criar_unidade(request):
    form = NovaUnidadeForm(request.POST)
    context = {}
    if form.is_valid():
        unidade = form.save(commit=False)
        unidade.usuario = request.user
        unidade.save()
        user = request.user
        context['success'] = f'Unidade: "{unidade.nome}" cadastrada com sucesso!'
        context['unidades'] = Unidade.objects.filter(usuario=user).order_by('-id')
        return render(request, 'includes/unidades.html', context)
    else:
        
        context['erro']=form.errors
        print(context['erro'])
        return render(request, 'includes/unidades.html', context)

def htmx_listar_unidade(request):
    user = request.user
    unidades = Unidade.objects.filter(usuario=user).order_by('-id')
    return render(request, 'includes/unidades.html',{'unidades':unidades})