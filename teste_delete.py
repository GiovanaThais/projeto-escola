import requests

headers = {'Authorization': 'Token cea6b2508d10f6f739a93108b6cd9f444c239590'}
url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'


resultado = requests.delete(url=f'{url_base_cursos}4/', headers=headers)

# Testando o código HTTP
assert resultado.status_code == 204

# print(resultado.text)

# Testando se o tamanho do conteúdo retorno é 0
assert len(resultado.text) == 0
