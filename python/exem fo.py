#primeiro exemplo for
'''x = 0
for x in range(3):# vai de 1 a 4
    print("O valor de X é: %d"% x)
print("Saiu do laço")
'''
'''
# segundo exemplo
x = 0
for x in range(50, 100): #vai de 50 a 99
    if x == 88:
'''

'''
# terceiro exemplo, menos soma dos numeros impares
total =0
numero = int(input("Digite um numero: "))
if (numero % 2) == 0:
    numero = numero -1
for i in range(numero,0,-2):
    total = total + i
    print("Valor de i %d:" %i)
print("A soma dos números impares é %d:" % total)
'''
'''
 #exercicios 1)
x = 0
for i in range(50, 151):
    print(" %d numero ao quandrado = %d" %(i,i*i))
'''

#2)
numero = int(input("Digite um numero: "))
f=1
#indo de 1 ate "numero"
for i in range (1, numero+1):
    f = f * i
print("Fatorial de %d: %d" % (numero, f))
f = 1
#indo de numero ate 1, decrementando em 1
for i in range(numero,0,-1):
    f=f*i
print("Faorial de %d: %d" % (numero, f))




















