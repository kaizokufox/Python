
class Conta:
         
    def __init__(self, numero, nome, saldo):  # construtor
        self.numero = numero
        self.nome = nome
        self.saldo = saldo
        print('classe inicializada pelo construtor\n')    

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if valor<=self.saldo:
                self.saldo -= valor
        else:
                print('Saldo insuficiente: %.2f' % self.saldo)

    def mostra(self):
        print('Número: %d' % self.numero)
        print('Nome: %s' % self.nome)
        print('Saldo: %.2f' % self.saldo)

    #Programa movimento:
from conta import Conta
numero = int(input("Digite o número: "))
nome = input("Digite o seu nome: ")
saldo = float(input("Digite o saldo: "))
conta = Conta(numero, nome, saldo)
conta.saque(float(input("Digite a quantidade do saque: ")))
conta.saque(float(input("Digite a quantidade do saque: ")))
conta.deposito(float(input("Digite a quantidade do valor a depositar: ")))
conta.mostra()
