<h1 align="center">InCine com Flask</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.1.1-blue.svg?cacheSeconds=2592000" />
  <a href="LICENSE" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/npm/l/react" />
  </a>
</p>

### 🏠 [Homepage](https://github.com/luizfernandoin/CinemaFlask)

###  Aplicação para listagem de filmes.
![alt text](aplicacao2.gif)

### Descrição
InCine é um serviço web desenvolvido durante o curso Tecnico em Informatica Integrado como requisito **obrigatório** da disciplina de Desenvolvimento de Aplicações Web do Instituto Federal de Educação, Ciência e Tecnologia da Paraíba.
Trata-se de uma aplicação web para visualizar informações de filmes criado com o framework Flask usando a API TMDB. O mesmo possui CRUD, autenticação de usuário, pesquisa de mídias e dados sobre o serviço.

### Características
Aqui estão os recursos em resumo:
* Exibe os filmes mais populares do TMDB e adicionados manualmente;
* O usuário pode pesquisar, visualizar e editar qualquer filme.

# Requisitos
- Python 3+
- Pip
- PostgresSQL
## Front end
- CSS / JS / TypeScript
- React Native
- Expo

### Instalação e configuração
Aqui está um resumo de como configurar o aplicativo:
* **1º Passo** : Clone este repositório usando **`git clone https://github.com/luizfernandoin/CinemaFlask.git`**, ou baixando um arquivo ZIP do código.
* **2º Passo** : O repositório, se baixado como um arquivo .zip, precisará ser extraído para o local de sua preferência e aberto
* **3º Passo** : Vá para o diretório raiz do projeto e instale a biblioteca venv usando pip e depois crie um ambiente virtual. Execute os seguintes comandos respectivamente:
    * **`pip install -m venv venv`**
    * **`cd .\venv\Scripts\`**
    * **`.\activate`**
* **4º Passo** : Faça o download de todas as dependências no requirements.txt usando **`pip install -r requirements.txt`**
* **5º Passo** : Acesse o [API do banco de dados de filmes (TMDB)](https://www.themoviedb.org/) SITE, inscreva-se para obter uma conta gratuita e gere uma chave de API. 
    * Crie um arquivo **.env** em seu diretório raiz e armazene a chave API assim **MOVIE_API_KEY="sua chave"`**
    * No mesmo arquivo, adicione as informações **`SECRET_KEY="chave secreta da aplicação"`** e os dados do BD.
    * Você deve ter algo assim:
    ```
    MOVIE_API_KEY = 'chave api'
    SECRET_KEY= 'chave secreta'
    USUARIO= 'postgres'
    SENHA= 'senha do banco'
    DATABASE= 'cinema-flask'
    ```
* **6º Passo** : Para realizar as configurações de banco de dados, basta codar os seguintes comandos:
    **`flask run.py db init `**
    **`flask run.py db migrate`**
    **`flask run.py db upgrade`**
    
* **7º Passo** : Agora você pode iniciar o aplicativo localmente executando o comando **`python run.py`**
    * Abra o navegador de sua preferência e visualize o aplicativo abrindo o link **http://127.0.0.1:5000/**.

### IMPORTANTE
* **OBSERVAÇÃO**: Este projeto usa flask-migrate para acompanhar as alterações feitas nas tabelas; portanto, sempre que você fizer modificações no arquivo tables.py; certifique-se de executar o seguinte comando:
```
python run.py db migrate"
```
```
python run.py db upgrade"
```
  * Você pode ler mais sobre flask-migrate verificando a [documentação](https://flask-migrate.readthedocs.io/en/latest/)

# Tecnologias utilizadas
* Python 3.7.4
* Flask 1.1.1
* HTML  
* CSS
* PostgreSQL
* Bootstrap 3.3.7

## Technologies Used
* Python
* Flask
* HTML  
* CSS
* PostgreSQL
* Bootstrap

## Desenvolvedores

👤 **Luiz Fernando**
👤 **Virgínia Maria**
👤 **Rosaliny Caldeira**
👤 **Maria Eloisa**

## Mostre seu apoio

Dê um ⭐️ se esse projeto te ajudou!
