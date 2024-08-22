from .views import Clientes, htmx_criar_cliente
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('clientes/', Clientes.as_view(), name='clientes'),
    path('cadastrar-cliente/', htmx_criar_cliente, name='cadastrar-cliente'),
   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)