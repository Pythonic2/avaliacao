from .views import htmx_criar_admin, htmx_listar_admin

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('criar-administrador/', htmx_criar_admin, name='criar-administrador'),
    path('listar-administrador/', htmx_listar_admin, name='listar-administrador'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)