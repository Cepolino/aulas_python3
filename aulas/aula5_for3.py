l = [4,8,3,9]

soma = 0 
for elemento in l:
    if elemento % 2 == 0:
        soma = soma + elemento

print(f"soma = {soma}")