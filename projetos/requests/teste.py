import requests

resposta = requests.get("https://aulaspython-aceb0-default-rtdb.firebaseio.com/.json")
dados = resposta.json()
print ("********************")
print (dados)
print ("********************")

#*****inserir novos dados
novo_dado = '{"Lila":"gatinha_senpai"}' 
resposta = requests.post("https://aulaspython-aceb0-default-rtdb.firebaseio.com/-Lila.json", novo_dado)
dados = resposta.json()
print ("********************")
print (dados)
print ("********************")

#*****mudar dados
novo_dado = '{"Lila":"gatinha_senpai", "especie":"felina","parentesco": "como_se_fosse_da_familia"}' 
resposta = requests.patch("https://aulaspython-aceb0-default-rtdb.firebaseio.com/-Lila.json", novo_dado)
dados = resposta.json()
print ("********************")
print (dados)
print ("********************")
#*******deletar dados
#resposta = requests.delete("https://aulaspython-aceb0-default-rtdb.firebaseio.com/-Lila.json")
#print(resposta)
#print(resposta.json)

