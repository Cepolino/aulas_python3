import os

pasta_atual = os.getcwd()
arquivos = os.listdir(pasta_atual)
for i in  range(0, len(arquivos), 4):
    linha = arquivos [i:i+4]
    print  ("\t".join(linha))


