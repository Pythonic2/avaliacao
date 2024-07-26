from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Campos a serem exibidos no formulário de criação de usuário
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'status_pagamento', 'data_pagamento', 'data_cobrar', 'logo', 'cor_logo'),
        }),
    )

    # Campos a serem exibidos no formulário de alteração de usuário
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'email', 'status_pagamento', 'data_pagamento', 'data_cobrar', 'logo', 'cor_logo')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    )

    # Campos a serem exibidos na lista de usuários
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'status_pagamento', 'data_pagamento', 'data_cobrar')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'status_pagamento')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)
