from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView,DeleteView, UpdateView,TemplateView, DetailView
from .models import Cliente
from .forms import NovoClienteForm

class Clientes(LoginRequiredMixin,ListView):
    model = Cliente
    template_name = 'home/clientes.html'
    form = NovoClienteForm

    def get(self, request):
        user = self.request.user
        autenticado = user.is_authenticated
        if autenticado:
            cleintes = Cliente.objects.filter(usuario=user).order_by('-id')
        else:
            cleintes = ''
        return render(request, self.template_name,{"autenticado":autenticado,'form':self.form,'clientes':cleintes})


def htmx_criar_cliente(request):
    form = NovoClienteForm(request.POST)
    context = {}
    if form.is_valid():
        cliente = form.save(commit=False)
        cliente.usuario = request.user
        cliente.save()
        user = request.user
        context['success'] = f'usuario: "{cliente.nome}" cadastrado com sucesso!'
        context['clientes'] = Cliente.objects.filter(usuario=user).order_by('-id')
        return render(request, 'includes/todos_clientes.html', context)
    else:
        context['erro']=form.errors
        print(context['erro'])
        return render(request, 'includes/todos_clientes.html', context)
