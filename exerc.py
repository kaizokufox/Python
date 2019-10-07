'''4)Desenvolver em Python um programa que tenha um módulo função que
apresenta um menu de opções e retorna a opção escolhida. Opções: 1 - Fatorial
do número; 2 - Tabuada do número; 3 - Mostrar se o número é par ou impar; 4 -
Sair do programa. Fazer os módulos correspondentes aos cálculos e as
chamadas dos mesmos.'''
def menu():
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
