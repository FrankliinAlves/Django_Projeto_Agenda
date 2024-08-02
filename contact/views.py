from django.shortcuts import render


def index(request): # Renderiza o template 'contact/index.html' para a resposta HTTP
    return render(
        request,
        'contact/index.html',
    )
