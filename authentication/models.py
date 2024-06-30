from django.db import models
from django.contrib.auth.models import User,AbstractUser
from datetime import timedelta
from django.utils import timezone
from datetime import datetime

def salvar_no_diretorio_do_user(instace, filename):
    return f'{instace.username}/logo/{filename}'

class CustomUser(AbstractUser):

    email = models.EmailField(unique=True)
    status_pagamento = models.BooleanField(default=False)
    data_pagamento = models.DateTimeField(default=timezone.now)
    data_cobrar = models.DateTimeField(default=timezone.now() + timedelta(days=30))
    logo = models.ImageField(blank=True, upload_to=salvar_no_diretorio_do_user)
    cor_logo = models.CharField(max_length=7, blank=True, null=True)
    def save(self, *args, **kwargs):
        is_new = self._state.adding
        is_staff = False 
        is_active = True
        is_superuser = False
        super().save(*
        args, **kwargs)

    @property
    def pagamento_atrasado(self):
        return timezone.now() >= self.data_cobrar
    
   
    