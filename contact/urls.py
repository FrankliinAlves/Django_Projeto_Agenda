from django.urls import path
from contact import views

app_name = 'contact'  # Define um namespace para as URLs da aplicação 'contact'

urlpatterns = [
    path('', views.index, name='index' ), # Mapeia a URL raiz para a view 'index' com o nome 'index'
]