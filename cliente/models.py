from django.db import models
from authentication.models import CustomUser
# Create your models here.


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True, blank=True, null=True)
    celular = models.CharField(max_length=11, blank=True,null=True)
    nascimento = models.DateField(blank=True,null=True)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


    def __str__(self):
        return self.nome

