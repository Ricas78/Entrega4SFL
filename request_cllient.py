#biblioteca para uso de requisições
import requests

#Define a URL da rota '/fatorial'
url = 'http://127.0.0.1:5000/fatorial'

#Define o JSON a ser enviado no corpo da requisição
data = {'num': 10}

#Faz a requisição POST
response = requests.post(url, json=data)

#imprime a resposta recebida do servidor
print(response.json())

#Define a URL da rota '/fibonacci'
url = 'http://127.0.0.1:5000/fibonacci'

#Define o JSON a ser enviado no corpo da requisição
data = {'num': 10}

#Faz a requisição POST
response = requests.post(url, json=data)

#imprime a resposta recebida do servidor
print(response.json())