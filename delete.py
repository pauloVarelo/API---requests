import requests

id = 2

url = f"https://67efe7452a80b06b8896368d.mockapi.io/camisa/{id}"

response = requests.delete(url)

if response.status_code == 200:
    print(f"Usuário com ID {id} foi excluído com sucesso 😁")
else:
    print(f"Falha da requisição😟: {response.status_code}{response.text}")