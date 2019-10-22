#função de operação matematica
def soma(n1, n2):
    return n1 + n2
def subtracao(n1, n2):
    return n1 - n2
def multiplicacao(n1, n2):
    return n1 * n2
def divisao(n1, n2):
    return n1 / n2
#Entrada de dados
n1 = int(input("Digite primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
#chamando as funções
print("\n%d + %d = %d" % (n1, n2, soma(n1, n2 )))
print("\n%d - %d = %d" % (n1, n2, subtracao(n1, n2 )))
print("\n%d * %d = %d" % (n1, n2, multiplicacao(n1, n2 )))
print("\n%d / %d = %.2f" % (n1, n2, divisao(n1, n2 )))
