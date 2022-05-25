import forca
import adivinhacao

print ('*****************************************')
print ('*************Escolha o jogo**************')
print ('*****************************************')

print ('(1) Jogo da Forca / (2) Jogo da Adivinhacao')
jogo = int(input('Qual o jogo: '))

if jogo==1:
    forca.jogar()
elif jogo==2:
    adivinhacao.jogar()