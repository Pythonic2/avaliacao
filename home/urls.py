from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import DashBoardView,home

urlpatterns = [
    path('dashboard/', DashBoardView.as_view(), name='dashboard'),
    path('', home, name='home'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)