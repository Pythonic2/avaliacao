from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from funcionario.views import DashBoardView

urlpatterns = [
    path('dashboard/', DashBoardView.as_view(), name='dashboard'), 
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)