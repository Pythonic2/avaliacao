from django.db import models
from unidade.models import Unidade
# Create your models here.

class AdministradorUnidade(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)