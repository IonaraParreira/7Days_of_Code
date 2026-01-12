<h1>🏆 Dia 07: A Página desdobrada (7 Days of Code)</h1>
<h3>Neste dia, deixei de apenas "exibir dados" e passei a gerenciar o fluxo de informações entre o cliente, o servidor e a API.</h3>

<br><img width="1915" height="1079" alt="Captura de tela 2026-01-11 153647" src="https://github.com/user-attachments/assets/019e6b81-a564-4a8c-aa4b-b88f9af9848f" />

<h2>Como o fluxo funciona na prática</h2>
O Link Mágico (href="?page=..."): Ao clicar em "Próximo", o navegador atualiza a URL (ex: /?page=2). O Django captura esse número através do request.GET.get('page').

<br>O Python "Cérebro": O Python usa esse número para montar a URL da API, busca os 10 personagens específicos e os coloca na "maleta" (dicionário de contexto).

As Variáveis de Controle: Utilizei {{ pagina_atual }}, {{ proxima_pagina }} e {{ pagina_anterior }}. Esses nomes no HTML são os "rótulos" que conectam os dados calculados no Back-end com a interface do usuário.

O Loop Inteligente ({% for %}): O HTML percorre a lista_avatar, que agora é dinâmica e contém apenas os dados da página solicitada.

# ![Dica](https://img.shields.io/badge/DOBREITUDO-9400d3?style=for-the-badge)

"No começo, eu apenas trazia os dados e cortava os 10 primeiros no Python. Mas no Dia 07 eu mudei a arquitetura para paginação dinâmica. Isso tornou o site escalável, porque agora eu gerencio o que a API envia através de parâmetros de URL. Se a base de dados crescer absurdamente, minha aplicação continua leve e rápida.
Com isso, pude evoluir a lógica de exibição de um corte estático (slice) para uma paginação dinâmica via API. Agora, o sistema solicita apenas os dados necessários para a página atual, otimizando drasticamente o consumo de memória e banda (Network)."

<h1>O Aprimoramento está aqui 😏</h1>

<img width="1912" height="1062" alt="Captura de tela 2026-01-12 121001" src="https://github.com/user-attachments/assets/d2df2944-363f-4be9-9553-7091356a3e57" />

<br><h1>🏆 Resumo Técnico: Aprimoramento Dia 07</h1>

<h1>Front-end & Estilização (Bootstrap 5)</h1>

<img width="953" height="495" alt="image" src="https://github.com/user-attachments/assets/d4fc9950-0135-4e95-bf41-50d18d4c9608" />

## Bootstrap 5

|  |  |
| :--- | :--- |
| **O que é** | Framework CSS utilizado para acelerar o desenvolvimento de interfaces responsivas. |
| **Como usei** | Implementado via CDN (Content Delivery Network) para estilizar as tabelas de dados e o sistema de paginação do | projeto Avatar.|
| **Destaque** | Adaptabilidade: O layout se ajusta automaticamente a diferentes tamanhos de tela (desktop e mobile). |
| **UI/UX** | Uso de classes como table-hover e badges para melhorar a experiência visual do usuário. |
| **Eficiência** | Criação de uma interface moderna e limpa sem a necessidade de escrever CSS do zero, focando na integração com o Back-end. | 

### 🛠️ Minhas Ferramentas

| Tecnologia | Ícone | O que eu fiz com ela? |
| :--- | :---: | :--- |
| **Python** | <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="25" height="25"> | Consumi a API e tratei os dados dos personagens por meio da lógica de processamento.|
| **Django** | <img src="https://cdn.jsdelivr.net/npm/simple-icons@v13/icons/django.svg" width="25" height="25"> | Gerenciei as rotas e a lógica do servidor,pensando nele como framework principal para a arquitetura do site.
| **Bootstrap** | <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-original.svg" width="25" height="25"> | Estilizei a tabela de personagens e a paginação de forma responsiva e com componentes de interface.|
| **Git** | <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/git/git-original.svg" width="25" height="25"> | Controlei o versionamento e gerenciamento de branches.|

---

|<h2>💡O diferencial</h2>
|:---|
"Ajuste Fino de Layout:"
Implementação de técnicas de table-layout: fixed e quebra de linha dinâmica para garantir que nomes longos da API não quebrassem a estrutura visual do site.


<br>![#7DaysOfCode](https://img.shields.io/badge/%237DaysOfCode-black?style=for-the-badge&logoColor=white)

<p align ="center"><img width="293" height="235" alt="Captura de tela 2026-01-08 120833" src="https://github.com/user-attachments/assets/0bc57ef3-a2a1-46df-a159-c0f5b0722c71" /></p>

<h3><p align="center">Por hoje é só pessoal, e se gostou ou foi útil <br>fique à vontade⭐</p></h3>

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png" width="100%">

<h1>🏆 Conquistas do Dia 06 - Desafio Back comback😏😎 (7 Days of Code)</h1>
<br><h2>Obstáculos do desenvolvimento,hoje foi um Back comback:</h2>

<h5>Embora a tela pareça "simples" como vista no dia 2, não,não é o mesmo código!Sabe por quê?:
Porque nesse desafio eu "entrei na illuminati" o código secreto,na verdade, eu usei o enumerate() para criar um "crachá" (ID) único para cada personagem. (<strong>Identidade Própria</strong>)</h5>

<h5>E se ainda não "view"(só os backs, conseguem 😅)! O meu views.py agora organiza Nome,Elemento,Foto e ID de forma estruturada (**Dicionário Profissional com uma lógica que deixa qualquer programador de back aberta**)<h5></h5>

<h5>Mantive o template HTML minimalista para validar a integridade da nova estrutura de IDs, com o objetivo de reintroduzir a renderização visual completa no desafio final. (**Separação de Camadas**)</h5>
<br><h1>Dia 6</h1>
<img width="1917" height="1036" alt="Captura de tela 2026-01-10 170540" src="https://github.com/user-attachments/assets/fed6470e-47af-4247-8e3e-86841597b125" />

<h1>Dia 2</h1>
<img width="1302" height="616" alt="image" src="https://github.com/user-attachments/assets/f7ede230-0977-4c8b-9579-6233774970d1" />

<h1>O Aprimoramento está aqui 😏</h1>
<img width="1913" height="1035" alt="image" src="https://github.com/user-attachments/assets/7c882a46-02e4-4329-9f20-a2ca756e1755" />

<br><h1>🏆 Resumo Técnico: Aprimoramento Dia 06</h1>

Inteligência no Back-end (Python/Django)
Tratamento de Listas: Aprendi a pegar dados brutos da API (que vinham como listas feias com colchetes ['exemplo']) e transformá-los em strings limpas usando o .join().

Formatação de String: Implementei o .upper() para garantir que informações cruciais (Aliados, Inimigos e Dobras) aparecessem com destaque e autoridade.

Tradução Dinâmica: Integrei a biblioteca googletrans para que o site fosse acessível em português, traduzindo nomes e afiliações em tempo real.

Monitoramento (Logs de Sênior)
Criei um sistema de Logs no Terminal. Agora, antes mesmo de abrir o navegador,eu já sei exatamente qual ID está sendo processado e se os dados estão corretos. Isso economiza horas de manutenção!

Sincronização com o Front-end (HTML)
Dominei o conceito de Chave/Valor. Entendi que o nome da "caixa" criada no Python ('dobra', 'aliados') precisa ser exatamente o mesmo usado no HTML ({{ personagem.dobra }}).

Interface Visual: Adicionei tags de imagem com estilos CSS inline (border-radius, width) para transformar uma lista de texto em uma galeria visual profissional.

<h2>Em Resumo</h2>
filtrei, traduzi, formatei, monitorei o terminal e só depois entreguei para o usuário final.


<br>![#7DaysOfCode](https://img.shields.io/badge/%237DaysOfCode-black?style=for-the-badge&logoColor=white)

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png" width="100%">


<h1>🏆 Conquistas do Dia 05 - Desafio BOOTSTRAP JUNTO AO DJANGO (7 Days of Code)</h1>
<br><h2>Obstáculos do desenvolvimento Back-end e venci😁 as seguintes etapas:</h2>

Integração de Back-end: Os dados estão vindo da API, sendo processados pela minha View e entregues ao Template.

Uso de Bootstrap: Instalei o framework corretamente via CDN e ele transformou meu HTML básico em algo profissional.

Visual em Tabela: Em vez de uma lista simples,criei uma tabela organizada, com cabeçalho e estilos (table-striped, table-dark).

<br><img width="938" height="918" alt="image" src="https://github.com/user-attachments/assets/9ea1f9f0-fc4e-4b53-bea3-82e775d29b3b" />

<br><img width="1910" height="1015" alt="Captura de tela 2026-01-09 125858" src="https://github.com/user-attachments/assets/10641b9c-4d16-468a-be4d-644f94557b35" />

| **Bootstrap**| **Utilidade** |
| :--- | :--- |
| É como uma loja de construção que entrega as paredes prontas. É um framework de CSS com códigos prontos para botões e tabelas. |Serve para deixar o projeto bonito e organizado sem precisar escrever centenas de linhas de código visual do zero. |


<br><h2>![Dica](https://img.shields.io/badge/🕵️_Dica_de_Programadora_Back_end-9400d3?style=for-the-badge)</h2>

Muitas vezes, quando você estiver usando uma biblioteca nova no Django (como uma para gráficos ou mapas), você vai procurar no Google por: "NomeDaLib CDN".
Isso vai te levar direto para sites como o cdnjs.com ou o jsdelivr.com, que são grandes bibliotecas de links prontos para você copiar e colar no seu head.

<br>![#7DaysOfCode](https://img.shields.io/badge/%237DaysOfCode-black?style=for-the-badge&logoColor=white)

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png" width="100%">


<h1>🏆 Conquistas do Dia 04 - Desafio DJANGO (7 Days of Code)</h1>
<br><h2>Obstáculos do desenvolvimento Back-end e superação🥳 das seguintes etapas:</h2>

<img width="1047" height="583" alt="Captura de tela 2026-01-08 120036" src="https://github.com/user-attachments/assets/eeb9ff14-8148-4cc5-9bdd-03a0b962ad5d" />

<h2>📜 Minha Jornada</h2> 

### 🏆 Me desdobrei hoje:

<br><img width="30" height="250" alt="Captura de tela 2026-01-08 115710" src="https://github.com/user-attachments/assets/cd4eb03b-edbf-44dc-8b65-7259051b4809" />
Dobra de Ar (**Navegação**): Dominei o vento para me mover entre os diretórios com o cd .. e o ls, encontrando o caminho de volta para a raiz do projeto. 

<br><img width="30" height="257" alt="Captura de tela 2026-01-08 115658" src="https://github.com/user-attachments/assets/c0e09a43-7042-4cb3-a094-9a54478dbb78" />
Dobra de Terra (**Estrutura**): Assentei a base sólida da arquitetura MVT, criando pastas e conectando URLs. Cada arquivo está em seu lugar sagrado. 

<br><img width="30" height="275" alt="Captura de tela 2026-01-08 115704" src="https://github.com/user-attachments/assets/f8ea08af-726e-462e-9cd9-3c853dc877e7" />
Dobra de Fogo (**Execução**): Acendi a chama do servidor com o runserver. O fogo da criação deu vida à minha primeira página HTML! 

<br><img width="30" height="311" alt="Captura de tela 2026-01-08 115654" src="https://github.com/user-attachments/assets/838c83e3-0adf-4039-b44d-90c05c64b827" />
Dobra de Água (**Fluidez**): Fiz o código fluir entre a View e o Template, separando a lógica da apresentação para um sistema harmonioso. 

<img width="1789" height="1079" alt="Captura de tela 2026-01-09 094520" src="https://github.com/user-attachments/assets/824f53fe-c3d7-466a-97e3-6a8e4f1866ec" />



<br><img width="1809" height="862" alt="image" src="https://github.com/user-attachments/assets/bb8bd426-d8ab-4e22-bf1a-8d6d57a31ab7" />

<h2>Curiosidade🕵️</h2>

💡 Por que esse comando? | python manage.py runserver|
|:---|:---|
python: Chama o intérprete da linguagem.
manage.py: É o seu "controle remoto" do projeto (o arquivo deixado na raiz).
runserver: É a ordem específica para ligar o motor e colocar o site no ar..


<br>![#7DaysOfCode](https://img.shields.io/badge/%237DaysOfCode-black?style=for-the-badge&logoColor=white)

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png" width="100%">

<h1>🏆 Conquistas do Dia 03 - Desafio DJANGO (7 Days of Code)</h1>
<br><h2>Obstáculos do desenvolvimento Back-end e superação💪🏻 das seguintes etapas:</h2>
Neste desafio, saí dos scripts isolados e iniciei a construção de uma aplicação Web robusta utilizando o framework Django.

Configuração de Ambiente Web: Fiz a instalação e preparação do framework Django dentro de um ambiente virtual (venv).

Arquitetura de Projeto: Criei a estrutura base do projeto utilizando o comando startproject e organização da lógica em aplicativos com startapp.

Gestão de Configurações: Registrei e ativei novos aplicativos dentro do arquivo settings.py (essencial para o funcionamento do ecossistema Django).

Servidor de Desenvolvimento: Executei e monitorei um servidor local via manage.py runserver, garantindo a comunicação correta entre o Back-end e o navegador.

Manutenção de Banco de Dados: Entendi sobre Migrações (migrations) e tratei avisos do terminal para manter a integridade do sistema.

<img width="1906" height="1078" alt="Captura de tela 2026-01-07 120608" src="https://github.com/user-attachments/assets/2c5d8378-450c-4d71-9bd5-33876e08a227" />

<img width="953" height="1029" alt="Captura de tela 2026-01-07 105132" src="https://github.com/user-attachments/assets/38908ed4-b676-4ca4-aefa-99a5b86faf56" />

<br>![Tradutor](https://img.shields.io/badge/Nota-lilac?style=for-the-badge&color=9400d3)

"Neste desafio, utilizei o terminal para orquestrar toda a infraestrutura do Django, desde a instalação até a execução do servidor dinâmico."

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/44e78d47-a864-4949-b1e6-cf882a94496f" />


<h2>Curiosidade🕵️</h2>

|DJANGO | SUA IMPORTÂNCIA |
|:--- | :---|
| É um DJ | Coordena faixas(arquivos) ritmos(dados) para que a festa(o site) aconteça sem ninguém sair do compasso! |


<br>![#7DaysOfCode](https://img.shields.io/badge/%237DaysOfCode-black?style=for-the-badge&logoColor=white)

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png" width="100%">

<h1>🏆 Conquistas do Dia 02 - Desafio Avatar (7 Days of Code)</h1>

<img width="1919" height="1069" alt="image" src="https://github.com/user-attachments/assets/567c6a38-b280-4021-952b-deb153795e12" />

<br><h2>Obstáculos do desenvolvimento Back-end e superação🌟 das seguintes etapas:</h2>
Instalei de novo a venv e importei corretamente.

Passei uma função para ler os nomes e afiliações.
Criei a função buscar_e_traduzir_personagens e usei o laço for p in personagens para navegar pelos dados.

Traduzi esses atributos usando o tradutor.translate para converter os campos de inglês para português.

Fiz um print para ver os nomes traduzidos e usei emojis e linhas de separação para melhorar a legibilidade.

Manipulei a Estrutura de Dados: Aprendendo a "abrir o pacote" (JSON) e percorrendo uma lista de dicionários. 

Tratei Dados Reais: Ao usar o .get('affiliation', 'N/A'), demonstrei que sei lidar com dados incompletos.

Comunicação entre Sistemas: Integrei o Python com duas coisas diferentes ao mesmo tempo: uma API de dados (Avatar) e um serviço de tradução (Google).

Persistência Técnica: Enfrentei erros de digitação na URL, erros de nome de variável e não desisti até o terminal mostrar exatamente o que planejei.

<h2>Curiosidade🕵️</h2>

Porque usei| E não usei|Motivo
|:---|:---|:---|
|from googletrans import Translator|import googletrans|Para deixar o código mais limpo e leve

<br>![#7DaysOfCode](https://img.shields.io/badge/%237DaysOfCode-black?style=for-the-badge&logoColor=white)

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png" width="100%">

<br><h1>🏆 Conquistas do Dia 01 - Desafio Avatar (7 Days of Code)</h1>

<img width="1913" height="1079" alt="image" src="https://github.com/user-attachments/assets/98639513-f4bb-461f-ab96-d45993044c13"/>


<br><h2>Obstáculos do desenvolvimento Back-end e superação das seguintes etapas:</h2>

Configuração de Ambiente Profissional: Criei um ambiente virtual (venv) dedicado para o projeto, garantindo que as dependências fiquem isoladas e não interfiram em outras aplicações do meu sistema.

Domínio do Módulo Requests: Instalei e utilizei a biblioteca requests para realizar comunicações via protocolo HTTP.

Consumo de API REST: Implementei com sucesso uma requisição do tipo GET para a API de "Avatar: The Last Airbender", estabelecendo conexão com  (Água, Terra, Fogo e Ar, sendo capaz de dominá-los para manter o equilíbrio), na verdade estabeleci conexão com apenas um servidor externo.

Manipulação de Dados JSON: Recebi a resposta da API, tratei os dados brutos para o formato JSON e utilizei o Python para exibir essas informações no terminal.

Versionamento e Organização: Superei desafios de diretórios e caminhos no terminal, organizando meus scripts de forma que o código e o ambiente virtual trabalhem em harmonia.

<h1>Resumo das Relações</h1>

|Conceito|O que é|Papel na comunicação|
|:---|:---|:---|
|GET|Método HTTP (verbo)|Ação de buscar/recuperar dados
|URL|Endereço|Local do recurso na rede
|API|Interface/Contrato|Define as regras de interação
|POSTMAN|Ferramenta|Ambiente para testar a API usando métodos e URLs

<br>![Tradutor](https://img.shields.io/badge/Dica-lilac?style=for-the-badge&color=9400d3)

Em essência, você usa o Postman para enviar uma requisição GET para uma URL específica que faz parte de uma API.


<br>![#7DaysOfCode](https://img.shields.io/badge/%237DaysOfCode-black?style=for-the-badge&logoColor=white)

<h2>Obrigada por ver este repositório😉. E se ele te ajudou de alguma forma, deixe uma ⭐ em troca</h2>
