# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

pares = 0
impares = 0

for _ in range (10):
    num = int (input ("Digite um numero: "))
    if num % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
        


print (f" o numero de pares e:{pares}, impares: {impares}")