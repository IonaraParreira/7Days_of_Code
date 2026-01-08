from django.shortcuts import render

def index(request):
    # Criamos uma lista [] que contém vários dicionários {}
    personagens_lista = [
        {'nome': 'Aang', 'elemento': 'Ar'},
        {'nome': 'Katara', 'elemento': 'Água'},
        {'nome': 'Sokka', 'elemento': 'Guerreiro'},
        {'nome': 'Toph', 'elemento': 'Terra'}
    ]
    
    # O contexto leva a lista para o HTML com o nome 'lista_avatar'
    return render(request, 'galeria/index.html', {'lista_avatar': personagens_lista})