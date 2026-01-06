import json
import requests
from googletrans import Translator #Exigência 1

def buscar_e_traduzir_personagens():
    """Conecta a API do Avatar, extrai os dados dos personagens e realiza a tradução dos campos 'name' e 'affiliation'"""

    url = 'https://last-airbender-api.fly.dev/api/v1/characters'
    
    try:
        #📡 Fazendo a chamada
        resposta = requests.get(url)

        #✅ Verifiando se a conexão deu certo(Status 200)
        if resposta.status_code == 200:
            personagens = resposta.json()
            tradutor = Translator()

            print("\n--- Personagens Traduzidos ---\n")#Exigência 2
            for p in personagens:
                nome_br = tradutor.translate(p['name'], dest='pt').text
                afiliacao = p.get('affiliation', 'N/A')
                filiacao_br = tradutor.translate(afiliacao, dest='pt').text
                print(f"👤 Nome: {nome_br}\n🛡️  Afiliação:{filiacao_br}")
                print("-" * 160)
        else:
            print(f"❌ Erro na API: Status{resposta.status_code}")
    
    except Exception as e:
        #🛡️ Se a internet cair, o programa avisa em vez de travar
        print(f"📡 Erro de conexão:{e}")

# O padrão para rodar scripts
if __name__ == "__main__":
    print("🌎 Buscando personagens do Avatar...")
    buscar_e_traduzir_personagens()