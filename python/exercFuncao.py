'''1)Faça um programa que recebe um número inteiro e através de um módulo
função calcula e mostra se o número é primo ou não.'''
'''
def primo(num):
    cont = 0
    for i in range(2, num):
        if num % i == 0 :
            cont = cont +1
            break
    if cont == 0:
        return True
    else:
        return False
numero = int(input("Digite um numero: "))
prim = primo (numero)
if prim:
    print("%d é primo" % (numero))
else:
    print("%d não é primo" % (numero))
'''

'''2)Faça um programa que receba um número inteiro e através de um módulo
função calcule e mostre se este número é par ou ímpar.'''

