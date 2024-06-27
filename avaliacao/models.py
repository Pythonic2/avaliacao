from django.db import models
from time import strftime
from authentication.models import CustomUser
from funcionario.models import Funcionario

class Avaliacao(models.Model):
    OPCOES_SATISFACAO = [
        (1, 'Muito Ruim'),
        (2, 'Ruim'),
        (3, 'Regular'),
        (4, 'Bom'),
        (5, 'Muito Bom')
    ]

    nome = models.CharField(max_length=100, blank=True, null=True)
    atendimento = models.IntegerField(choices=OPCOES_SATISFACAO)
    produto_servico = models.IntegerField(choices=OPCOES_SATISFACAO)
    comentarios = models.TextField(blank=True, null=True)
    
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    data = models.DateField(default=strftime("%Y-%m-%d"), blank=True)
    
    def __str__(self):
        return f"Avaliação de {self.nome or 'Anônimo'}"
