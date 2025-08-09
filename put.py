import requests

id = 2

url = f"https://67efe7452a80b06b8896368d.mockapi.io/camisa/{id}"

data = {
    "nome" : "Paulo",
    "marca" : "Adidas",
    "preco" : 49.00,
    "tamanho" : "M"
}

response = requests.put(url, json=data)

if response.status_code == 200:
    atualizado = response.json()
    print(f"Usuário com ID {id} foi atualizado com sucesso 😁")
    print(atualizado)
else:
    print(f"Falha da requisição😟: {response.status_code}{response.text}")