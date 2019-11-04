'''#3)
class Produto:
    #a)
    def __init__(self, codigo, descricao, qtd, preco):
        self.codigo = codigo
        self.descricao = descricao
        self.qtd = qtd
        self.preco = preco
        print("Inicialização pelo construtor")
    #b)
    def mostrar(self):
        print("Codigo: %d" % self.codigo)
        print("Descrição: %s" % self.descricao)
        print("Quantidade: %d" % self.qtd)
        print("Preço: %.2f" % self.preco)
    #c)
    def totall(self):
        return self.qtd * self.preco
#d)
cod = int(input("Digite o código: "))
desc = input("Digite a descrição: ")
qtd = int(input("Digitte a quantidade: "))
preco = float(input("Digite o preço: "))
prod = Produto(cod, desc, qtd, preco)
prod.mostrar()
print("Total: %.2f" % prod.totall())
'''
