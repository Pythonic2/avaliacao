from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import UnidadeFormulario, htmx_criar_unidade

urlpatterns = [
    path('unidade/', UnidadeFormulario.as_view(), name='unidade'),
    path('criar-unidade/', htmx_criar_unidade, name='criar-unidade'),
   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)