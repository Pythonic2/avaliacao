from django.contrib import admin
from .models import Funcionario, Avaliacao, AdministradorUnidade,Unidade

admin.site.register(Funcionario)
admin.site.register(Avaliacao)
admin.site.register(AdministradorUnidade)
admin.site.register(Unidade)
