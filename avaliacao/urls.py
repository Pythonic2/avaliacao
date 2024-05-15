from .views import sei_la

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('avaliacao/', sei_la, name='avaliacao'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)