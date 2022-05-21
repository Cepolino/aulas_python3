print ("Olá! Vamos calcular o salário mensal.")
item1 = float (input ("Quantas horas trabalha no mês? "))
item2 = float (input ("Quanto recebe por hora? "))
item3 = (item1 * item2) / 100
imposto = item3 * 11
inss = item3 * 8
sindicato = item3 * 5
print (f"Salario bruto:         R${item1 * item2}")
print (f"Imposto de Renda:      R$ {imposto}")
print (f"Previdência:           R$ {inss}")
print (f"Contribuição Sindical: R$ {sindicato}")
print (f"Total de descontos:    R$ {imposto + inss + sindicato}")
print (f"Salário líquido:       R${(item1 * item2) - imposto - inss - sindicato}")
print ("Não vai gastar tudo!")
