from .views import sei_la,obrigado,listar_avaliacoes,listar_avaliacoes_completas

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('avaliacao/<int:id_usuario>/<str:matricula>', sei_la, name='avaliacao'),
    path('obrigado/', obrigado, name='obrigado'),
    path('listar-avaliacoes/', listar_avaliacoes, name='listar_avaliacoes'),
    path('listar-all-avlc/', listar_avaliacoes_completas, name='listar_tds_avlc'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)