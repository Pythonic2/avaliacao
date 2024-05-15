from django.db import models
from authentication.models import CustomUser
# Create your models here.

class Unidade(models.Model):
    nome = models.CharField(max_length=100)
    end = models.CharField(max_length=100)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f'{self.nome} - {self.end}'