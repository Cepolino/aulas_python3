dado = float  (input ("Olá! Qual o tamanho do arquivo para download em megabites? "))
velocidade = float (input ("E a qual a velocidade do seu link de internet? em Mbps: "))
minutos = int (dado // (velocidade * 60))
segundos = int (dado % (velocidade * 60))
print (f" O tempo de Download do seu arquivo será: {minutos} minutos e { segundos } segundos ")
print  ("obrigado por sua participacao")