from django.shortcuts import render
from administrador_unidade.forms import NovoAdministradorForm
from administrador_unidade.models import AdministradorUnidade
from django.shortcuts import render
    

def htmx_criar_admin(request):
    form = NovoAdministradorForm(request.POST)
    context = {}
    if form.is_valid():
        admin = form.save(commit=False)
        admin.usuario = request.user
        admin.save()
        context['success'] = f'Administrador: "{admin.nome}" cadastrada com sucesso!'
        user = request.user
        # Replace 'created_by' with the correct field name in your model
        context['administradores'] = AdministradorUnidade.objects.filter(usuario=user).order_by('-id')
        return render(request, 'includes/administradores.html', context)
    else:
        context['erro'] = form.errors
        return render(request, 'includes/administradores.html', context)

def htmx_listar_admin(request):
    user = request.user
    context = {'administradores': AdministradorUnidade.objects.filter(usuario=user).order_by('-id')}
    return render(request, 'includes/administradores.html', context)
