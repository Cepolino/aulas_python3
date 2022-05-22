base = int(input("Digite a base:"))

expoente = int(input("Digite o expoente:"))

resultado = 1

for _ in range (expoente):
    resultado = resultado * base



print(f"{base} elevado a {expoente} = {resultado}")