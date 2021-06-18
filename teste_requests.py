import requests


#GET Avaliacoes

#avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# Acessando o código de status HTTTP
#print(avaliacoes.status_code)


# Acessando os dados da resposta
#print(avaliacoes.json())
#print(type(avaliacoes.json()))

# Acessando a quantidade de registros
# print(avaliacoes.json()['count'])

# Acessando a próxima página de resultados
# print(avaliacoes.json()['next'])

# Acessando os resultados desta página
# print(avaliacoes.json()['results'])
# print(type(avaliacoes.json()['results']))

# Aceessando o primeiro elemento da lista de resultados
# print(avaliacoes.json()['results'][0])

# Aceessando o último elemento da lista de resultados
# print(avaliacoes.json()['results'][-1])

# Acessando somente o nome da pessoa que fez a última avaliação
# print(avaliacoes.json()['results'][-1]['nome'])


# GET Avaliacao

#avaliacao = requests.get('http://localhost:8000/api/v2/avaliacoes/61/')

#print(avaliacao.json())

# GET Cursos

headers = {'Authorization': 'Token cea6b2508d10f6f739a93108b6cd9f444c239590'}

cursos = requests.get(url='http://localhost:8000/api/v2/cursos/', headers=headers)

print(cursos.status_code)
print(cursos.json())