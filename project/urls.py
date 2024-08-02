from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('contact.urls')), # Inclui as URLs da aplicação 'contact'
    path('admin/', admin.site.urls),  # Adiciona a URL para o painel administrativo do Django
]
