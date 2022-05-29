import requests

resposta = requests.get("https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome", headers={'Accept': 'application/json'},)
resposta_dict = resposta.json()
dados = resposta_dict["dados"]
lista = []
for deputado in dados:
    lista.append(f"{deputado['siglaPartido']}, {deputado['nome']}, {deputado['id']}")

lista.sort()
print("\n".join(lista))
