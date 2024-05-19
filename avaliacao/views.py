from django.shortcuts import render, get_object_or_404,redirect, HttpResponse
from .models import Funcionario
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
    return HttpResponse("<h1>Obrigado por nos avaliar</h1>")