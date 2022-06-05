import random

def jogar():
    print ('*****************************************')
    print ('*******Bem vindo ao jogo da Forca********')
    print ('*****************************************')

    arquivo = open("C:/Users/Manoel/Documents/workspace/aulas_python3/exercicios/frutas.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erro = 0
    
    while not enforcou and not acertou:
        chute = input("Qual a letra? ")
        chute = chute.strip().upper()
        posicao = 0
        if chute in palavra_secreta:
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[posicao] =letra
                    print ("".join(letras_acertadas))
                               
                posicao = posicao + 1
        else:
            erro += 1
            print ("Voce errou!")
        enforcou = erro == 6
        acertou = "_" not in letras_acertadas
    if acertou:
        print ("********************************************")
        print ("**********Parabens, voce ganhou!!!**********")
        print ("********************************************")
    else:
        print ("********************************************")
        print("Voce perdeu!")
        print ("********************************************")

    print ("Fim de Jogo!")
    












if __name__=='__main__':
    jogar()