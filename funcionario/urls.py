from django.urls import path
from .models import Funcionario
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import FuncionarioDetailView, AuthorCreateView, ListFuncionarios,htmx_criar_funcionario

urlpatterns = [
    path('funcionario/<int:pk>/', FuncionarioDetailView.as_view(), name='funcionario_detail'),  # Adicione uma barra no final
    path('create-funci/', AuthorCreateView.as_view(), name='create_funci'), 
    path('salvar-funci/', htmx_criar_funcionario, name='salvar_funci'), 
    path('list-funcionarios/', ListFuncionarios.as_view(), name='list_funci'), 

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)