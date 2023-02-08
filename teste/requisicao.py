import requests

api_key = "53946516f41af3e0ac2f77293e9eb855"
url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query='Gato+de+Botas+2:+O+Último+Pedido'&language=pt-BR"

response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    print(dados)
else:
    print("Erro ao consumir a API")