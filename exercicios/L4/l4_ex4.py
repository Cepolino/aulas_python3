
num_vogais = 0
palavra = input("Digite uma palavra: ").lower()
print(f"palavra = {palavra}")
for letra in palavra: 
    if letra in "aeiou":
        num_vogais = num_vogais + 1

print(f"Foram lidas {num_vogais} vogais")