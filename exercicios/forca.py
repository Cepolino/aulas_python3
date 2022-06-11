import random

def jogar():

    mensagem_de_abertura()
    palavra_secreta = carrega_palavra_secreta('exercicios/ferramentas.txt')
    letras_acertadas = carregar_letras_acertadas(palavra_secreta)



    enforcou = False
    acertou = False
    erro = 0
    
    while not enforcou and not acertou:
        chute = pede_chute()

        if chute in letras_acertadas:
            marca_erro_se_repetir_letra(letras_acertadas, erro)
        
        elif chute in palavra_secreta:
            marca_chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            erro += 1
            print ("Voce errou!")
            print ("".join(letras_acertadas))
            desenha_forca(erro)
        enforcou = erro == 7
        acertou = "_" not in letras_acertadas
    if acertou:
        imprime_msg_vencedor()
    else:
        imprime_msg_perdedor(palavra_secreta)

    print ("Fim de Jogo!")
    

#Funções abaixo
###############################################################

def mensagem_de_abertura():
    print ('*****************************************')
    print ('*******Bem vindo ao jogo da Forca********')
    print ('*****************************************')

def carrega_palavra_secreta(nome_do_arquivo):
    arquivo = open(nome_do_arquivo, "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()    
    return palavra_secreta

def carregar_letras_acertadas(palavra_secreta):
    letras_acertadas = ["_" for letra in palavra_secreta]
    return letras_acertadas

def pede_chute():
    chute = input("Qual a letra? ")
    chute = chute.strip().upper()
    return chute

def marca_erro_se_repetir_letra(letras_acertadas, erro):
    print ('Voce repitiu a letra. Preste atenção!!!')
    print ("".join(letras_acertadas))
    erro+= 1
    desenha_forca(erro)

def marca_chute_correto(chute, palavra_secreta, letras_acertadas):
    posicao = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[posicao] =letra
        posicao = posicao + 1
    print ("".join(letras_acertadas))
        

def desenha_forca(erro):
    print("  _______     ")
    print(" |/      |    ")

    if(erro == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erro == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erro == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erro == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erro == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erro == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erro == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_msg_vencedor():
    print ("********************************************")
    print ("**********Parabens, voce ganhou!!!**********")
    print ("********************************************")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_msg_perdedor(palavra_secreta):
    print ("********************************************")
    print (f"*****{palavra_secreta}***Voce perdeu!********")
    print ("********************************************")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

if __name__=='__main__':
    jogar()
