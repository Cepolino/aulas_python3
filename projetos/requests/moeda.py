import requests

resposta = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
dados = resposta.json()
cotacao_dolar = dados['USDBRL']['bid']
cotacao_euro = dados['EURBRL']['bid']
cotacao_bitcoin = dados['BTCBRL']['bid']
print ("********************")
print (f"Dolar: R${cotacao_dolar} / Euro: R${cotacao_euro} / Bitcoin: R${cotacao_bitcoin}")
print ("********************")