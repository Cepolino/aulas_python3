import requests

resposta = requests.get("https://dadosabertos.camara.leg.br/api/v2/votacoes?ordem=DESC&ordenarPor=dataHoraRegistro", headers={'Accept': 'application/json'},)
resposta_dict = resposta.json()
dados = resposta_dict["dados"]
lista = []
for i in dados:
    lista.append(f"{i['siglaOrgao']},\n {i['data']},\n {i['descricao']}")

lista.sort()
print("\n".join(lista))



