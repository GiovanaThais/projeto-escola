import requests
import jsonpath


avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

resultados = jsonpath.jsonpath(avaliacoes.json(), 'results')

print(resultados)

# primeira = jsonpath.jsonpath(avaliacoes.json(), 'results[0]')

# print(primeira)

# nome = jsonpath.jsonpath(avaliacoes.json(), 'results[0].nome')

# print(nome)

# nota_data = jsonpath.jsonpath(avaliacoes.json(), 'results[0].avaliacao')

# print(nota_data)

# curso_id = jsonpath.jsonpath(avaliacoes.json(), 'results[0].curso')
# print(curso_id)


# Todos os nomes das pessoas que avaliaram  o curso
# nomes = jsonpath.jsonpath(avaliacoes.json(), 'results[*].nome')
#print(nomes)


# Todas as avaliacoes das pessoas que avaliaram  o curso
#notas = jsonpath.jsonpath(avaliacoes.json(), 'results[*].avaliacao')
#print(notas)
