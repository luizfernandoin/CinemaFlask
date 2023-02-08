
from .models.tables import Movies
import requests
'''
response = requests.get(url)

if response.status_code == 200:
    dados = response.json()['results']
    for dado in dados:
        print(dado)
else:
    print("Erro ao consumir a API")

# Getting api key
api_key = "53946516f41af3e0ac2f77293e9eb855"

# Getting the movie base url
base_url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query='Gato de Botas 2: O Último Pedido'&language=pt-BR"


def configure_request(app):
    global api_key, base_url
    api_key = app.config["MOVIE_API_KEY"]
    base_url = app.config["MOVIE_API_BASE_URL"]


def get_movies(category):
    """
    Function that gets the json response to our url request
    """
    get_movies_url = base_url.format(category, api_key)
    get_movies_response = requests.get(get_movies_url).json()
    
    if get_movies_response['results']:
        movie_results_list = get_movies_response['results']
        movie_results = process_results(movie_results_list)

    return movie_results

'''
def process_results(movie_list):
    """
     Função que processa o resultado do filme e os transforma em uma lista de Objetos

     Argumentos:
         movie_list: Uma lista de dicionários que contém detalhes do filme

     Devoluções:
         movie_results: Uma lista de objetos de filme
    """
    movie_results = []
    for movie_item in movie_list:
        id = movie_item.get('id')
        title = movie_item.get('original_title')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster_path')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')

        if poster:
            movie_object = Movies(id, title, overview, poster, vote_average, vote_count)
            Movies.add_movie(id, title, overview, poster, vote_average, vote_count)
            movie_results.append(movie_object)

    return movie_results

'''
def get_movie(id):
    get_movie_details_url = base_url.format(id, api_key)
    movie_details_response = requests.get(get_movie_details_url).json()

    if movie_details_response:
        id = movie_details_response.get('id')
        title = movie_details_response.get('original_title')
        overview = movie_details_response.get('overview')
        poster = movie_details_response.get('poster_path')
        vote_average = movie_details_response.get('vote_average')
        vote_count = movie_details_response.get('vote_count')

        movie_object = Movie(id, title, overview, poster, vote_average, vote_count)

    return movie_object
'''

def search_movie(movie_name):
    api_key = "53946516f41af3e0ac2f77293e9eb855"
    search_movie_url = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}&language=pt-BR'.format(api_key, movie_name)
    search_movie_response = requests.get(search_movie_url).json()

    if search_movie_response['results']:
        search_movie_list = search_movie_response['results']
        search_movie_results = process_results(search_movie_list)
        return search_movie_results
    return False