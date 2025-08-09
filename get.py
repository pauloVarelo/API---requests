import requests

url = "https://67efe7452a80b06b8896368d.mockapi.io/pedido"

response = requests.get(url)

if response.status_code == 200:
    posts = sorted(response.json(), key=lambda x: int(x['id']))
    
    for post in posts[:10]:
        print(post)
else:
    print(f"Falha na requisição: {response.status_code}")