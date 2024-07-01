from django.urls import path
from .models import Funcionario
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('create-funci/', AuthorCreateView.as_view(), name='create_funci'), 
    path('salvar-funci/', htmx_criar_funcionario, name='salvar_funci'), 
    path('list-funcionarios/', ListFuncionarios.as_view(), name='list_funci'),
    path('detalhe-funcionario/<int:id>/', htmx_editar_funcionario, name='detalhe_funcionario'),
    path('update-funcionario/<int:id>/', htmx_update_funcionario, name='update-funcionario'),
    path('apagar-funcionario/<int:id>/', htmx_apagar_funcionario, name='apagar_funcionario'),
    path('detalhe-estabelecimento/<int:id>/', htmx_editar_estabelecimento, name='detalhe_estabelecimento'),
    path('update-estabelecimento/<int:id>/', htmx_update_estabelecimento, name='update_estabelecimento'),
    path('apagar-estabelecimento/<int:id>/', htmx_apagar_estabeleciento, name='apagar_estabelecimento'),
    path('editar-perfil/', editar_perfil, name='editar_perfil'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)