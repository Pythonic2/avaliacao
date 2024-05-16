from django.db import models
from time import strftime
from funcionario.models import Funcionario
from authentication.models import CustomUser
# Create your models here.
class Avaliacao(models.Model):
    FUNCIONARIO_CHOICES = (
        ('Bom', 'Bom'),
        ('Regular', 'Regular'),
        ('Ruim', 'Ruim'),
    )

    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    atendimento = models.CharField(max_length=10, choices=FUNCIONARIO_CHOICES)
    higiene = models.CharField(max_length=10, choices=FUNCIONARIO_CHOICES)
    comentario = models.TextField(blank=True)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    data = models.DateField(default=strftime("%d/%m/%Y"), blank=True)
    def __str__(self):
        return f"Avaliação de {self.funcionario.nome}"