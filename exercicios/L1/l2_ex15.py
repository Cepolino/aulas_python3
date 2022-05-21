print ("a seguir, informe as medias de cada lado do triangulo:")
lado1 = input ("Digite o primeiro lado: ")
lado2 = input ("Digite o segundo lado:")
lado3 = input ("Digite o terceiro lado: ")

if (lado1 + lado2) < lado3 or (lado2 + lado3) < lado1 or (lado3 + lado1) < lado2:
    print ("Essas medidas não de são de um triangulo: ")
if lado1 == lado2 == lado3:
    print ("Equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print ("Isósceles")
else:
    print ("Escaleno")
    
print ("Obrigado pela participação!")