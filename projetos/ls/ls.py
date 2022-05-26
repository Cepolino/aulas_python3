import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--all", help= 'Use a para visualizar todos os arquivos, inclusive ocultos', action ="store_true")
args = parser.parse_args()

lista = []
pasta_atual = os.getcwd()
arquivos = os.listdir(pasta_atual)

if args.all:
    lista = arquivos
else:
    for i in arquivos:
        if not i.startswith("."):
            lista.append(i)

for i in  range(0, len(lista), 4):
    linha = lista [i:i+4]
    print  ("\t".join(linha))