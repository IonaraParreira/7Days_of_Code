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
                    # 1. PROCESSAMENTO DE DADOS
                    nome_raw = p.get('name', '')
                    nome_br = tradutor.translate(nome_raw, dest='pt').text.upper()
                    
                    afiliacao_raw = p.get('affiliation', 'Não informada')
                    dobra_br = tradutor.translate(afiliacao_raw, dest='pt').text.upper()
                    
                    aliados_raw = p.get('allies', [])
                    aliados_limpos = ", ".join(aliados_raw).upper() if aliados_raw else "SEM ALIADOS"
                    
                    inimigos_raw = p.get('enemies', [])
                    inimigos_limpos = ", ".join(inimigos_raw).upper() if inimigos_raw else "SEM INIMIGOS"

                    # 🖥️ 2. LOG DE SÊNIOR 
                    print(f"ID {indice+1}: {nome_br}")
                    print(f"   🤝 ALIADOS: {aliados_limpos}")
                    print(f"   🚫 INIMIGOS: {inimigos_limpos}")
                    print(f"   🌊 DOBRA: {dobra_br}")
                    print("-" * 30)

                    # 📦 3. PACOTE COMPLETO PARA O HTML (Site)
                    personagens_traduzidos.append({
                        'id': indice + 1,
                        'nome': nome_br,
                        'dobra': dobra_br,
                        'aliados': aliados_limpos,
                        'inimigos': inimigos_limpos,
                        'foto': p.get('photoUrl', 'https://via.placeholder.com/150')
                    })
                except Exception as e:
                    print(f"Erro no personagem {indice}: {e}")
                    continue
                
    except Exception as e:    
        print(f"Erro de conexão: {e}")

    return render(request, 'galeria/index.html', {'lista_avatar': personagens_traduzidos})