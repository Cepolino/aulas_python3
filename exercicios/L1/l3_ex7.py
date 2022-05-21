maior = 0 

for _ in range(5):
    num = int (input ("Digite um numero: "))
    if num > maior:
        maior = num


print(f"Maior = {maior}")