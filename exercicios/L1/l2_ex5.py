print ("Olá, vamos ver suas notas")
nota1 = 11
nota2 = 11

while nota1 > 10 or nota2 > 10:
    print ("Incorreto, tente de novo!")
    nota1 = int (input("Digite a nota do primeiro semestre: "))
    nota2 = int (input ("Digite a nora do segundo semestre: "))

media = (nota1 + nota2) / 2

if media == 10:
    print ("Aprovado com louvor")

elif media > 7 and media < 10:
    print ("Aprovado")

else:
    print ("REPROVADO")

print ("Obrigado pela participação!")