from django import forms
from .models import Avaliacao

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['nome', 'atendimento', 'produto_servico', 'comentarios']
        widgets = {
            'atendimento': forms.RadioSelect(choices=Avaliacao.OPCOES_SATISFACAO),
            'produto_servico': forms.RadioSelect(choices=Avaliacao.OPCOES_SATISFACAO),
            'comentarios': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
        }
