from django.urls import path
from .models import Funcionario
from django.conf import settings
from django.conf.urls.static import static
from app.views import PublisherDetailView

from django.urls import path
from .views import PublisherDetailView, AuthorCreateView

urlpatterns = [
    path('funcionario/<int:pk>/', PublisherDetailView.as_view(), name='funcionario_detail'),  # Adicione uma barra no final
    path('create-funci/', AuthorCreateView.as_view(), name='create_funci'),  # Adicione uma barra no final
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
