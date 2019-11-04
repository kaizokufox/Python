#3)
class Produto:
    #a)
    def _init_(self, codigo, descricao, qtd, preco):
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
        print("=")*30
        return self.qtd * self.preco
#d)
print("=" *30)
cod = int(input("Digite o código: "))
print("=" *30)
desc = input("Digite a descrição: ")
print("=" *30)
qtd = int(input("Digitte a quantidade: "))
print("=" *30)
preco = float(input("Digite o preço: "))
print("=" *30)
prod = Produto(cod, desc, qtd, preco)
prod.mostrar()
print("Total: %.2f" % prod.totall())
