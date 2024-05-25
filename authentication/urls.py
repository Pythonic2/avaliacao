from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import LoginUsuario, logout_view,RegisterUser, pagamento_aprovado

urlpatterns = [
    path('login/', LoginUsuario.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
    path('aprovado/', pagamento_aprovado, name='provado'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)