import os

lista = []
pasta_atual = os.getcwd()
arquivos = os.listdir(pasta_atual)
for i in arquivos:
    if not i.startswith("."):
        lista.append(i)

for i in  range(0, len(lista), 4):
    linha = lista [i:i+4]
    

    print  ("\t".join(linha))
