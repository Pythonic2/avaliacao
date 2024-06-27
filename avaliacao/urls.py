from .views import sei_la,obrigado,listar_avaliacoes

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('avaliacao/<str:matricula>', sei_la, name='avaliacao'),
    path('obrigado', obrigado, name='obrigado'),
    path('listar-avaliacoes/', listar_avaliacoes, name='listar_avaliacoes'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)