import requests
from django.shortcuts import render
from googletrans import Translator

def index(request):
    url = 'https://last-airbender-api.fly.dev/api/v1/characters'
    personagens_traduzidos = []
    
    try:
        # 📡 Chamando a API do Avatar
        resposta = requests.get(url)
        if resposta.status_code == 200:
            personagens = resposta.json()
            tradutor = Translator()

            # 🆔 O 'enumerate' nos dá o índice (0, 1, 2...) para criar o ID
            for indice, p in enumerate(personagens[:10]):
                try:
                    # Traduzindo Nome e Afiliação
                    nome_br = tradutor.translate(p.get('name', ''), dest='pt').text
                    afiliacao = p.get('affiliation', 'Sem afiliação')
                    afiliacao_br = tradutor.translate(afiliacao, dest='pt').text

                    # 📥 Encaixando tudo na lista (ID, Nome, Elemento e Foto)
                    personagens_traduzidos.append({
                        'id': indice + 1,  # O ID começa em 1
                        'nome': nome_br,
                        'elemento': afiliacao_br,
                        'foto': p.get('photoUrl', 'https://via.placeholder.com/150')
                    })
                except Exception as e:
                    print(f"Erro ao processar personagem: {e}")
                    continue
                
    except Exception as e:    
        print(f"Erro de conexão: {e}")

    # Enviando a lista atualizada para o HTML
    return render(request, 'galeria/index.html', {'lista_avatar': personagens_traduzidos})