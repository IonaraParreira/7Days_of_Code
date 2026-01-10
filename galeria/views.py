import requests
from django.shortcuts import render
from googletrans import Translator

def index(request):
    url = 'https://last-airbender-api.fly.dev/api/v1/characters'
    personagens_traduzidos = []
    
    try:
        #📡 Chamando a API do Avatar
        resposta = requests.get(url)
        if resposta.status_code == 200:
            personagens = resposta.json()
            tradutor = Translator()

           #Pegando todos os personagens
        for p in personagens:
            try:
                    # Traduzindo Nome e Afiliação
                nome_br = tradutor.translate(p.get('name', ''), dest='pt').text
                afiliacao = p.get('affiliation', 'Sem afiliação')
                afiliacao_br = tradutor.translate(afiliacao, dest='pt').text

                # Adicionando foto e listas de amigos/inimigos
                personagens_traduzidos.append({
                    'nome': nome_br,
                    'elemento': afiliacao_br,
                    'foto': p.get('photoUrl', 'https://via.placeholder.com/150'),
                    'aliados': p.get('allies', []),
                    'inimigos': p.get('enemies', [])})
            except:
                continue #Se um falhar,pula para o próximo
                
    except Exception as e:    
        print(f"Erro de conexão: {e}")

    # Enviando a lista real para o seu HTML
    return render(request, 'galeria/index.html', {'lista_avatar': personagens_traduzidos})
        