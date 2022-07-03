class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print(f'Construindo objeto...{self}.')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        disponivel_para_saque = self.__saldo + self.__limite
        return valor_a_sacar <= disponivel_para_saque

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print (f"O valor de {valor} eh maior que seu saldo e limite.")

    def transfere(self,valor,destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def extrato(self):
        print (f"Ola {self.__titular} o seu saldo e {self.__saldo}, com limite do cheque especial de {self.__limite}.")
    
    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_do_banco():
        return "001"
