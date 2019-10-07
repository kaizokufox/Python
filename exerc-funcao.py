#função em python:
'''def hello(meu_nome):
    print("Olá", meu_nome)
nome = input("Digite o seu nome: ")

#chamando a função:
hello(nome)
'''

'''def hello(meu_nome, sua_idade):
    print("Olá", meu_nome,"\nvocê tem", sua_idade,"anos")
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

hello(nome, idade)
'''

#função de operação matematica
'''def soma(n1, n2):
    return n1 + n2
def subtracao(n1, n2):
    return n1 - n2
def multiplicacao(n1, n2):
    return n1 * n2
def divisao(n1, n2):
    return n1 / n2
n1 = int(input("Digite primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
#chamando as funções
print("\n%d + %d = %d" % (n1, n2, soma(n1, n2 )))
print("\n%d - %d = %d" % (n1, n2, subtracao(n1, n2 )))
print("\n%d * %d = %d" % (n1, n2, multiplicacao(n1, n2 )))
print("\n%d / %d = %d" % (n1, n2, divisao(n1, n2 )))
'''

#2)
'''def calcular_pagamento(horas, valor_hora):
    if horas <= 40:
        salario = horas*valor_hora
    else:
        h_excd = horas - 40
        salario = 40 * valor_hora + (h_excd*(1.5 * valor_hora))
    return salario
qtd_horas = float(input("Digite a quantidade de horas: "))
valor = float(input("Digite o valor da hora trabalhada: "))
#chamado a função
salario = calcular_pagamento(qtd_horas, valor)
print("Salário: %.2f " % salario)
'''

#Exercícios
#1)Faça um programa que recebe um número inteiro e através de um módulo
#função calcula e mostra se o número é primo ou não.
'''def numero_primo(numero):
    cont = 0
    for i in range(2, numero):
        if numero % i == 0:
            cont = cont + 1
            break
    if cont == 0:
        return True
    else:
        return False
numero = int(input("Digite um numero: "))
primo = numero_primo (numero)
if primo:
    print("{} é primo".format(numero))
else :
    print("{} não é primo".format(numero))
'''

#2)Faça um programa que receba um número inteiro e através de um módulo
#função calcule e mostre se este número é par ou ímpar.
'''def par_impar (numero):
    if numero % 2 == 0:
        return True
    else:
        return False
numero = int(input("Digite um numero: "))
num = par_impar (numero)
if num:
    print("%d é par" % numero)
else:
    print("%d é impar" % numero)
'''

#3)Faça um programa que recebe dois números reais e através de um módulo
#procedimento(sem retorno, mostrar o resultado dentro da função) calcula e mostra a potenciação do primeiro número pelo segundo
#e a divisão do primeiro número pelo segundo.
'''def calculo(num1, num2):
    pont = num1 ** num2
    divi = num1 / num2
    print(" %.2f" % pont)
    print(" %.2f" % divi)
num1 = float(input("Digite primeiro numero: "))
num2 = float(input("Digite segundo numero: "))
calculo(num1, num2)
'''


'''4)Desenvolver em Python um programa que tenha um módulo função que
apresenta um menu de opções e retorna a opção escolhida. Opções: 1 - Fatorial
do número; 2 - Tabuada do número; 3 - Mostrar se o número é par ou impar; 4 -
Sair do programa. Fazer os módulos correspondentes aos cálculos e as
chamadas dos mesmos.'''
'''def menu():
    print("\nOpção 1 função fatorial \nOpção 2 Tabuada do número \nOpção 3 Mostrar se o número é par ou impar \nOpção 4 Sair")
    op = int(input("Digite uma opção: "))
    return op
def fatorial (n1):
    fat = 1
    for x in range(1, n1 + 1):
        fat *= x
    print("Fatorial de {} = {}".format (n1, fat))
def tabuada(n1):
    for x in range(1, 11):
        print("{} x {} = {}".format(n1, x, n1 * x))
def par_impar(n1):
    if n1 % 2 == 0:
        print('{} é par'.format(n1))
    else:
        print("{} é impar".format(n1))
num1 = int(input("Digite um número: "))
opcao = -1
while opcao !=4 :
    opcao = menu()
    if opcao == 1 :
        fatorial(num1)
    elif opcao == 2 :
        tabuada(num1)
    elif opcao == 3 :
        par_impar(num1)
    elif opcao == 4 :
        print("Saindo do programa")
    else :
        print("opção inválida")
'''
