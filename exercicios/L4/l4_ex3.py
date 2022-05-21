

l=[]

for i in range(4):
    num = float(input(f"Digite a nota {i+1}: "))
    l.append(num)


print(f"Notas = {l}")
print(f"Media = {sum(l)/4}")