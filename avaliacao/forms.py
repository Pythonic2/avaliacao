from django import forms
from .models import Avaliacao

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = [
            'nome', 'tipo_servico', 'cordialidade', 'rapidez',
            'satisfacao_geral', 'qualidade', 'preco_qualidade', 'ambiente',
            'limpeza', 'gostou', 'melhorar', 'comentarios'
        ]
        widgets = {
            'cordialidade': forms.RadioSelect(choices=Avaliacao.OPCOES_SATISFACAO),
            'rapidez': forms.RadioSelect(choices=Avaliacao.OPCOES_SATISFACAO),
            'satisfacao_geral': forms.RadioSelect(choices=Avaliacao.OPCOES_SATISFACAO),
            'qualidade': forms.RadioSelect(choices=Avaliacao.OPCOES_SATISFACAO),
            'preco_qualidade': forms.RadioSelect(choices=Avaliacao.OPCOES_SATISFACAO),
            'ambiente': forms.RadioSelect(choices=Avaliacao.OPCOES_SATISFACAO),
            'limpeza': forms.RadioSelect(choices=Avaliacao.OPCOES_SATISFACAO),
            'gostou': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
            'melhorar': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
            'comentarios': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
        }
