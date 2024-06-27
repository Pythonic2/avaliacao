from django import forms
from .models import Avaliacao

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['nome', 'atendimento', 'produto_servico', 'comentarios']
        labels = {
            'nome': 'Nome (Opcional)',
            'atendimento': 'Avaliação do Atendimento',
            'produto_servico': 'Avaliação do Produto/Serviço',
            'comentarios': 'Comentários (Opcional)',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'atendimento': forms.Select(choices=Avaliacao.OPCOES_SATISFACAO, attrs={'class': 'form-control'}),
            'produto_servico': forms.Select(choices=Avaliacao.OPCOES_SATISFACAO, attrs={'class': 'form-control'}),
            'comentarios': forms.Textarea(attrs={'rows': 4, 'cols': 50, 'class': 'form-control'}),
        }
