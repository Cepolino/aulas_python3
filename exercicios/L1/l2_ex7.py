item1 = int (input("digite um numero: "))
item2 = int(input("digite outro numero: "))
item3 = int (input("digite outro numero: "))

if item1 > item2 and item1 > item3:
    maior = item1
elif item2 > item1 and  item2 > item3:
    maior = item2
else :
    maior = item3
    
if item1 < item2 and  item1 < item3:
    menor = item1
elif item2 < item1 and item2 < item3:
    menor = item2 
else:
    menor = item3 

print (f"O maior numero é: {maior}")   
print (f"O menor numero é: {menor}")
