from django.db import models
from time import strftime
from authentication.models import CustomUser
from funcionario.models import Funcionario

from django.db import models

class Avaliacao(models.Model):
    OPCOES_SATISFACAO = [
        (1, 'Muito Insatisfeito'),
        (2, 'Insatisfeito'),
        (3, 'Neutro'),
        (4, 'Satisfeito'),
        (5, 'Muito Satisfeito')
    ]

    nome = models.CharField(max_length=100, blank=True, null=True)
    tipo_servico = models.CharField(max_length=20, choices=[('produto', 'Produto'), ('servico', 'Serviço')])
    
    cordialidade = models.IntegerField(choices=OPCOES_SATISFACAO)
    rapidez = models.IntegerField(choices=OPCOES_SATISFACAO)
    satisfacao_geral = models.IntegerField(choices=OPCOES_SATISFACAO)
    qualidade = models.IntegerField(choices=OPCOES_SATISFACAO)
    preco_qualidade = models.IntegerField(choices=OPCOES_SATISFACAO)
    ambiente = models.IntegerField(choices=OPCOES_SATISFACAO)
    limpeza = models.IntegerField(choices=OPCOES_SATISFACAO)
    
    gostou = models.TextField(blank=True, null=True)
    melhorar = models.TextField(blank=True, null=True)
    comentarios = models.TextField(blank=True, null=True)
    
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    data = models.DateField(default=strftime("%Y-%m-%d"), blank=True)
    
    def __str__(self):
        return f"Avaliação de {self.nome or 'Anônimo'} em {self.data_visita}"
