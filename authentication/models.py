from django.db import models
from django.contrib.auth.models import User,AbstractUser

# Create your models here.
class CustomUser(AbstractUser):

    email = models.EmailField(unique=True)

    # Método para criar categorias padrão ao criar um novo usuário
    def save(self, *args, **kwargs):
        is_new = self._state.adding
        is_staff = False 
        is_active = True
        is_superuser = False
        super().save(*
        args, **kwargs)
    