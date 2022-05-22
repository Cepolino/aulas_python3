
lista = [4, 19, 6]
# class range(start, stop[, step])
# range(10) - stop
# range(3, 10) - start, stop
# range(3, 10, 2) - start, stop, step
posicoes = [0, 1, 2]
tamanho_lista = 3
# tamanho_lista = len(lista)
posicoes = range(tamanho_lista)

for elemento in lista:
    print(elemento)

for posicao in range(len(lista)):  
    print(f"posicao = {posicao} elemento = {lista[posicao]}")