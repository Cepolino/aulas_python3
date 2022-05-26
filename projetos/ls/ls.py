import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--hidden", help= 'Use O para diretorios ocultos', action ="store_true")
args = parser.parse_args()

lista = []
pasta_atual = os.getcwd()
arquivos = os.listdir(pasta_atual)

if args.hidden:
    for i in  range(0, len(arquivos), 4):
        linha = arquivos [i:i+4]  
        print  ("\t".join(linha)) 

else:
    for i in arquivos:
        if not i.startswith("."):
            lista.append(i)

    for i in  range(0, len(lista), 4):
        linha = lista [i:i+4]
    
        print  ("\t".join(linha))
