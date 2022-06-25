class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print(f'Construindo objeto...{self}.')
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = 1000.0

    def extrato(self):
        print (f"Ola {self.titular} o seu saldo e {self.saldo}, com limite do cheque especial de {self.limite}.")

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor


