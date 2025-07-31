class Main:
    pass

print("Testando o arquivo main.py")

from Cliente import Cliente

c1 = Cliente("Bruno", "(81) 99999-9999")

print(c1)
print(c1.nome, "e", c1.telefone)