'''class Vendedor:
    # construtor:
    def __init__(self, codigo, nome, vendas):  # construtor
        self.codigo = codigo
        self.nome = nome
        self.vendas = vendas
        self.comissao = vendas * 0.10
        print('classe inicializada pelo construtor\n')
    def add_vendas(self, vendas):
        self.vendas += vendas
        self.comissao = self.vendas * 0.10
    def mostra(self):
        print('Código: %.2f' % self.codigo)
        print('Nome: %s' % self.nome)
        print('Vendas: %.2f' % self.vendas)
        print('Comissão: %.2f' % self.comissao)
#Programa vendas:
from vendedor import Vendedor
vendas = Vendedor(1, 'João da Silva', 100.00)
vendas.add_vendas(1500)
vendas.mostra()
'''
