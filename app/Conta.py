class Conta:
    def __init__(self, titular, numero, saldo):
        self.saldo = 0
        self.numero = numero
        self.titular = titular
        
    # Método Get
    def get_saldo(self):
        return self._saldo
    
    # Método Set
    def set_saldo(self, valor):
        if (valor < 0):
            print("O saldo não pode ser negativo")
        else:
            self._saldo = valor