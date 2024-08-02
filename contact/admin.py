from django.contrib import admin
from contact import models


@admin.register(models.Contact)
class Contactadmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', # listando os dados com as colunas.
    ordering = 'id', # Ordena crescente 
    #ordering = '-id', # Ordena decrescente
    #list_filter = 'create_data', # Filtro por data
    search_fields = 'id', 'first_name', 'last_name', # campo de pesquisa
    list_per_page = 5 # paginação
    list_max_show_all = 100 
    #list_editable = 'first_name', 'last_name', 'phone', # Editar valores nas listas
    list_display_links = 'id', 'first_name',
