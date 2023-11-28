#importar as bibliotecas para criação e manuseio do servidor e para as operações matemáticas
from flask import Flask, request, jsonify
import math

#Cria uma variável que armazena um objeto da classe Flask
app = Flask(__name__)

#Define a rota '/fatorial' que aceita requisições POST
@app.route('/fatorial', methods=['POST'])
def fatorial():
    #Obtém os dados JSON da requisição e aramzena em uma variável
    data = request.get_json()
    #Extrai o número do JSON
    num = data['num']
    #Calcula o fatorial do número e armazena em uma variável
    result = math.factorial(num)
    #Retorna o resultado como um JSON
    return jsonify({'fatorial': result})

#Define a rota '/fibonacci' que aceita requisições POST
@app.route('/fibonacci', methods=['POST'])
def fibonacci():
    #Obtém os dados JSON da requisição e armazena em uma variável
    data = request.get_json()
    #Extrai o número do JSON
    num = data['num']
    #inicializa a série Fibonacci
    fib_series = [0, 1]
    #Calcula a série Fibonacci até o número especificado
    while len(fib_series) < num:
        fib_series.append(fib_series[-1] + fib_series[-2])
    #Retorna a série Fibonacci como um JSON
    return jsonify({'sequencia': fib_series})

#Verifica se o script está sendo executado diretamente e, em caso afirmativo, inicia o servidor
if __name__ == '__main__':
    print("\nservidor iniciado\n\n")
    app.run(debug=True)