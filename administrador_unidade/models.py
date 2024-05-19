from django.db import models
from authentication.models import CustomUser

class AdministradorUnidade(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.nome}'