n = int(input("Digite um numero de 1 a 10: "))

if n > 10:
    print("Maior que 10")
elif n > 5:
    print("Maior que 5")
elif n > 3:
    print("Maior que 5")
else:
    x = 30 ** 2
    print(f"o valor de x eh {x}")
    print("Nao eh maior nem que 10 nem que 5")

if n > 10:
    print("Maior que 10")
else:
    if n > 5:
        print("Maior que 5")
    else:
        if n > 3:
            print("Maior que 5")
        else:
            print("Nao eh maior nem que 10 nem que 5")


