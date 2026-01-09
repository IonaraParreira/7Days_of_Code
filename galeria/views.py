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

            # Pegando os 10 primeiros para ser mais rápido
            for p in personagens[:10]:
                nome_br = tradutor.translate(p['name'], dest='pt').text
                afiliacao = p.get('affiliation', 'Sem afiliação')
                afiliacao_br = tradutor.translate(afiliacao, dest='pt').text

                personagens_traduzidos.append({
                    'nome': nome_br,
                    'elemento': afiliacao_br})
                
    except Exception as e:    
        print(f"Erro de conexão: {e}")

    # Enviando a lista real para o seu HTML
    return render(request, 'galeria/index.html', {'lista_avatar': personagens_traduzidos})
        