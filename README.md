# Entrega4SFL
O código API.py é o script que inicializa o servidor local e define as funções que serão executadas nele quando ele for requesitado;

O código request_client.py é o script que faz a requisição ao servidor e fornece o json com o parâmetro que sera usado nas funções que serão executadas no servidor, após isso ele retorna o que o servidor retornou pra ele após a requisição.
 
Portanto, o script cliente e o servidor Flask trabalham juntos da seguinte maneira:

O script cliente faz uma requisição POST para a API Flask, enviando um JSON no corpo da requisição;

O servidor Flask recebe a requisição, extrai o número do JSON e calcula o fatorial e a série de Fibonacci;

O servidor Flask envia o resultado de volta ao script cliente como uma resposta;

O script cliente recebe a resposta e imprime o resultado.
