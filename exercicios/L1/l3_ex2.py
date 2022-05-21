print ("Olá, vamos cadastrar seu usuário e senha!")
usuario = input ("Digite seu nome de usuário:  ")
senha = input ("Digite sua senha: ")

while usuario == senha:
    print (f"Erro; não deve usar o mesmo nome de usuário para senha. tente de novo: ")  
    usuario = input ("Digite seu nome de usuário:  ")
    senha = input ("Digite sua senha: ")
else:
    print ("ok")  