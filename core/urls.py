
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('administrador_unidade.urls')),
    path('', include('authentication.urls')),
    path('', include('avaliacao.urls')),
    path('', include('funcionario.urls')),
    path('', include('home.urls')),
    path('', include('unidade.urls')),
    path('', include('cliente.urls')),
]
