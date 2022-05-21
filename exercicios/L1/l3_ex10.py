x=int(input("Digite um numero:  "))
y=int(input("Digite outro numero: "))

print("for")
for i in range(x, y+1, 2):
	print(i)

print("while")
i = x
while i < y + 1:
	print(i)
	i = i + 1
    