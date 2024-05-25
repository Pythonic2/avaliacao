from django.db import models
from django.contrib.auth.models import User,AbstractUser
from datetime import timedelta
from django.utils import timezone
class CustomUser(AbstractUser):

    email = models.EmailField(unique=True)
    status_pagamento = models.BooleanField(default=False)
    data_pagamento = models.DateTimeField(default=timezone.now)
    data_cobrar = models.DateTimeField(default=timezone.now() + timedelta(days=30))
    # Método para criar categorias padrão ao criar um novo usuário
    def save(self, *args, **kwargs):
        is_new = self._state.adding
        is_staff = False 
        is_active = True
        is_superuser = False
        super().save(*
        args, **kwargs)
    