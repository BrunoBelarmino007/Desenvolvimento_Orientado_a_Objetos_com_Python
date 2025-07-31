class Conta:
    def __init__(self, titular, numero, saldo):
        self.saldo = 0
        self.numero = numero
        self.titular = titular

    @property 
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        if (valor < 0):
            print("O saldo não pode ser negativo")
        else:
            self._saldo = valor

    def saque(self, valor):
        if (self.saldo >= valor):
            self.saldo -= valor
            print("Saldo Realizado com sucesso")
        else:
            print("Saldo insuficiente para saque")

    def deposita(self, valor):
        self.saldo += valor
       
    def extrato(self):
        print("Cliente: ", self.titular, "Saldo: ", self.saldo)