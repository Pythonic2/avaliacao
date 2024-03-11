from django.urls import path
from .models import Funcionario
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import FuncionarioDetailView, AuthorCreateView, ListFuncionarios,LoginUsuario, logout_view,RegisterUser, DashBoardView

urlpatterns = [
    path('funcionario/<int:pk>/', FuncionarioDetailView.as_view(), name='funcionario_detail'),  # Adicione uma barra no final
    path('create-funci/', AuthorCreateView.as_view(), name='create_funci'), 
    path('list-funcionarios/', ListFuncionarios.as_view(), name='list_funci'), 
    path('dashboard/', DashBoardView.as_view(), name='dashboard'), 
    path('', LoginUsuario.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_view, name='logout'), 

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

