n = 10  
print("for com range")
for i in range(n):
    print(f"O valor de i = {i}")

print("for com lista")
for elemento in [3,6,8]:
    print(f"O valor de i = {elemento}")    

print("for com lista por posicao")
l = [3,6,8]
for posicao in range(len(l)): #  len(l) = 3
    print(f"O valor de i = {posicao} l[{posicao}]={l[posicao]}")     

