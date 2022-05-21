item = float (input(" digite a temperatura em graus fahrenheit: "))
celsius = 5 * ((item - 32) / 9)
print (f"A temperatura em Celsius é: {celsius}")
if celsius < 10:
    print ("que frio!!!")
elif celsius < 23:
    print ("perfeito!")
elif celsius < 38:
    print ("que calor!!!")
else:
    print ("acabou a vida na face da terra...")