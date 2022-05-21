metros = float ( input ("Quantos metros quadrados serão pintados? "))
tinta = metros / 3
latas = tinta // 18
print (f"total de litros a serem usados: {tinta: .2f}")
if tinta % 18 > 0:
    latas = latas + 1
    
print (f"Total de latas será:{latas}")
    
custo = latas * 80  
print  (f"Preço total: R${ custo}")