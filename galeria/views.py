import requests
from django.shortcuts import render
from googletrans import Translator

def index(request):
    url = 'https://last-airbender-api.fly.dev/api/v1/characters'
    personagens_traduzidos = []
    
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            personagens = resposta.json()
            tradutor = Translator()

            for indice, p in enumerate(personagens[:10]):
                try:
                    # Traduzindo o nome para Português
                    nome_br = tradutor.translate(p.get('name', ''), dest='pt').text
                    
                    # 🛡️ TRATAMENTO PROFISSIONAL (BACK-END)
                    # Pegamos as listas, limpamos e deixamos em MAIÚSCULO como você queria
                    aliados_raw = p.get('allies', [])
                    aliados_limpos = ", ".join(aliados_raw).upper() if aliados_raw else "SEM ALIADOS"
                    
                    inimigos_raw = p.get('enemies', [])
                    inimigos_limpos = ", ".join(inimigos_raw).upper() if inimigos_raw else "SEM INIMIGOS"

                    # 🖥️ ISSO VAI APARECER NO SEU TERMINAL (LOG DE SÊNIOR)
                    print(f"ID {indice+1}: {nome_br} | ALIADOS: {aliados_limpos}")

                    personagens_traduzidos.append({
                        'id': indice + 1,
                        'nome': nome_br,
                        'aliados': aliados_limpos,
                        'inimigos': inimigos_limpos,
                        'foto': p.get('photoUrl', 'https://via.placeholder.com/150')
                    })
                except Exception as e:
                    print(f"Erro no processamento do personagem {indice}: {e}")
                    continue
                
    except Exception as e:    
        print(f"Erro de conexão com a API: {e}")

    # Enviando a lista para o seu HTML
    return render(request, 'galeria/index.html', {'lista_avatar': personagens_traduzidos})