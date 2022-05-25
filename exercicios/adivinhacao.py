import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,100)
    total_de_tentativas = 0
    pontos = 1000

    
    print ("Escolha o nivel de dificuldade")
    print ("(1) Facil / (2) Medio / (3) Dificil")
    nivel = int(input ("Digite o nivel: "))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    for rodada in range(1, total_de_tentativas + 1):
        print(f"Tentativa {rodada} de {total_de_tentativas}")
        chute_str = input ("Digite um número entre 1 e 99: ")
        print ("Você digitou " , chute_str)
        chute = int(chute_str)

        if chute < 1 or chute > 99:
            print("Você deve digitar um número entre 1 e 99!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if acertou:
            print(f"Você acertou!\nVoce fez {pontos}. Parabens.")
            break
        else:
            if maior:
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif menor:
                print("Você errou! O seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print (f'O numero secreto e: {numero_secreto}')
    print(f"Fim do jogo")

if __name__=='__main__':
    jogar()
