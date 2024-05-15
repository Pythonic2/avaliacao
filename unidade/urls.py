from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import  htmx_criar_unidade,htmx_listar_unidade

urlpatterns = [
    path('criar-unidade/', htmx_criar_unidade, name='criar-unidade'),
    path('listar-unidade/', htmx_listar_unidade, name='listar-unidade'),
   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)