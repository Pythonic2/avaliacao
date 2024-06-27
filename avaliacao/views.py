from django.shortcuts import render, get_object_or_404,redirect, HttpResponse
from .models import Funcionario, Avaliacao
from .forms import AvaliacaoForm


def sei_la(request, matricula):
    funcionario = get_object_or_404(Funcionario, matricula=matricula)
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            avaliacao = form.save(commit=False)
            avaliacao.usuario = funcionario.usuario
            avaliacao.funcionario = funcionario
            avaliacao.save()
            return redirect('obrigado')  # Redirecione para uma página de sucesso ou similar
    else:
        form = AvaliacaoForm()

    return render(request, 'home/avaliacao.html', {'form': form})

def obrigado(request):
    return render(request,'home/obrigado_avaliar.html')

def listar_avaliacoes(request):
    satisfacao = request.GET.get('satisfacao')
    if satisfacao:
        avaliacoes = Avaliacao.objects.filter(usuario=request.user, atendimento=int(satisfacao)).order_by('-id')
        total = avaliacoes.count()
    else:
        avaliacoes = Avaliacao.objects.filter(usuario=request.user).order_by('-id')
        total = avaliacoes.count()
    return render(request, 'includes/list_avaliacoes.html', {'avaliacoes': avaliacoes,'total':total})