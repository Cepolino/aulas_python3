l = []
for i in range(5):
    num = float(input(f"Digite numero real [{i+1}]: "))
    l.append(num)

for i in range(4, -1, -1):
    print(f"i={i} l[{i}]={l[i]}")

for i in l[::-1]:
    print(f"i={i}")

print(f"A lista inversa eh: {l[::-1]}")