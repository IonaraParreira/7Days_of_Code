import requests # Usando o módulo request

# Exigência 1: Executar requisição do tipo GET
url = "https://last-airbender-api.fly.dev/api/v1/characters"
resposta = requests.get(url)

# Exigência 2: Pegar a resposta em JSON
dados = resposta.json()

# Exigência 3: Imprimir o corpo da resposta
print(dados)