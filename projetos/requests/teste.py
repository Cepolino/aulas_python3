import requests

resposta = requests.get("https://aulaspython-aceb0-default-rtdb.firebaseio.com/.json")
dados = resposta.json()
print ("********************")
print (dados)
print ("********************")