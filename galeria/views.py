import requests
from django.shortcuts import render
from googletrans import Translator

def index(request):
    # 📄 1. CAPTURA A PÁGINA (Novidade do Dia 7)
    pagina_atual = int(request.GET.get('page', 1))
    
    # 🔗 2. URL COM PARÂMETROS (Novidade do Dia 7)
    url = f'https://last-airbender-api.fly.dev/api/v1/characters?perPage=10&page={pagina_atual}'
    
    personagens_traduzidos = []
    
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            personagens = resposta.json()
            tradutor = Translator()

            # Note: O enumerate ajuda no Log de Sênior!
            for indice, p in enumerate(personagens):
                try:
                    # ---PROCESSAMENTO DE DADOS (Mantido!) ---
                    nome_raw = p.get('name', '')
                    nome_br = tradutor.translate(nome_raw, dest='pt').text.upper()
                    
                    afiliacao_raw = p.get('affiliation', 'Não informada')
                    dobra_br = tradutor.translate(afiliacao_raw, dest='pt').text.upper()
                    
                    aliados_raw = p.get('allies', [])
                    aliados_limpos = ", ".join(aliados_raw).upper() if aliados_raw else "SEM ALIADOS"
                    
                    inimigos_raw = p.get('enemies', [])
                    inimigos_limpos = ", ".join(inimigos_raw).upper() if inimigos_raw else "SEM INIMIGOS"

                    # 🖥️ LOG DE SÊNIOR (Mantido!)
                    print(f"PÁGINA {pagina_atual} | ID {indice+1}: {nome_br}")
                    print(f"   🤝 ALIADOS: {aliados_limpos}")  # <--- Use o nome que você definiu!
                    print(f"   🚫 INIMIGOS: {inimigos_limpos}") # <--- Use o nome que você definiu!
                    print(f"   🌊 DOBRA: {dobra_br}")
                    print("-" * 30)

                    personagens_traduzidos.append({
                        'id': indice + 1,
                        'nome': nome_br,
                        'dobra': dobra_br,
                        'aliados': aliados_limpos,
                        'inimigos': inimigos_limpos,
                        'foto': p.get('photoUrl', 'https://via.placeholder.com/150')
                    })
                except Exception as e:
                    print(f"Erro no personagem: {e}")
                    continue
                
    except Exception as e:    
        print(f"Erro de conexão: {e}")

    # 🧮 3. LÓGICA DE NAVEGAÇÃO (Novidade do Dia 7)
    proxima_pagina = pagina_atual + 1
    pagina_anterior = pagina_atual - 1 if pagina_atual > 1 else None

    # 📦 4. A MALETA DE CONTEXTO (Agora com mais itens)
    contexto = {
        'lista_avatar': personagens_traduzidos,
        'pagina_atual': pagina_atual,
        'proxima_pagina': proxima_pagina,
        'pagina_anterior': pagina_anterior,
    }

    return render(request, 'galeria/index.html', contexto)