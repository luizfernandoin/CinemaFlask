import os
from decouple import config as ENV

DEBUG = True

MOVIE_API_BASE_URL = "https://api.themoviedb.org/3/movie/{}?api_key={}&language=pt-BR"
MOVIE_API_KEY = ENV("MOVIE_API_KEY")
SECRET_KEY = ENV("SECRET_KEY")

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'postgresql',
        usuario = ENV("USUARIO"),
        senha = ENV("SENHA"),
        servidor = 'localhost',
        database = ENV("DATABASE")
    )

# pegando o nome do caminho absoluto do diretório e concatenando com o diretório uplouds
UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'