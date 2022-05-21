metros = int ( input ("Quantos metros quadrados serão pintados? "))
tinta = int ((metros / 6) * 1.1)
latas = int (tinta // 18)
galões = int (tinta // 3.6)

if latas % 18 !=0:
    latas2 = latas + 1

if galões % 3.6 !=0:
    galões += 1

mistura = (((latas * 18) - tinta) % 3.6) 
if mistura !=0:
    mistura = 1

valor1 = 80 * latas2
valor2 = 25 * galões
valor3 = ((80 * latas) + (25 * mistura))

print (f"O total de tinta a ser usada é:{tinta}. O total de latas a serem usadas será: {latas2}, ao preço de: R${valor1},00. O total de galões a serem utilizados será: {galões}, ao preço de: R${valor2},00. O total de latas e galões será: {latas} latas, e {mistura} galões, no valor total de: R${valor3},00.")