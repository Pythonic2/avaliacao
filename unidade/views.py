from django.shortcuts import render
from django.http import HttpResponse
from .forms import NovaUnidadeForm
from .models import Unidade
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class UnidadeFormulario(LoginRequiredMixin,TemplateView):
    template_name = 'includes/unidade.html'
    form_class = NovaUnidadeForm

    def get(self, request):
        form = self.form_class()
        context = {'form_2':form}
        return render(request,self.template_name,context)


def htmx_criar_unidade(request):
    form = NovaUnidadeForm(request.POST)
    context = {}
    if form.is_valid():
        unidade = form.save(commit=False)
        unidade.usuario = request.user
        unidade.save()
        context['success'] = f'Unidade: "{unidade.nome}" cadastrada com sucesso!'
        context['unidades'] = Unidade.objects.all().order_by('-id')
        return render(request, 'includes/unidades.html', context)
    else:
        context['erro']=form.errors
        return render(request, 'includes/unidades.html', context)