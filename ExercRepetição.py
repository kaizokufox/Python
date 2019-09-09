#1) calcular a soma dos numeros digitados e a media
'''
soma = 0
media = 0
numero = 1
qdt = 0
while numero != 0 :
    numero = int(input("Digite um numero: "))
    if numero != 0:
       soma = soma + numero
       qdt = qdt + 1
    media = soma / qdt
print("A soma dos números é: %d " % soma)
print("A media dos números é: %d " % media)
'''
#2) somar os pares de 10 numeros
'''
soma = 0
x = 0
while x <10 :
    numero = int(input("Digite um número: "))
    if (numero % 2) == 0 :
        soma = soma + numero # somando o contador
    x = x +1
print("A soma dos numeros pares: %d " % soma)            
'''
#3)programa q ler 10 numero e mostra os positivos, negativos e 0
'''
x = 0
soma = 0
negat = 0
zero = 0
while x < 5:
    numero = int(input("Digite um numero: "))
    if numero < 0:
        negat = negat + 1
    elif numero > 0 :
        soma = soma + 1# contador da condição
    else:
        zero = zero + 1
    x=x+1# contador do while
print("Soma dos numeros negativos: %d e dos numeros zero: %d e numeros inteiros: %d" % (negat, zero, soma))
'''

#4)Repetidor de 0 a 50 convertendo celsius para farenheit
'''
tf = 0
tc = 0
while tc < 51:
    print("%.2f Graus Celsius para %.2f graus Farenheit:" % (tc, tf ))
    tf = (1.8 * tc) + 32
    tc = tc +1
print("saiu")
'''
'''
#5)
media = 0
media_turma = 0
soma = 0
conta = 0
while media >= 0:
    media = float(input("Digite a media do aluno: "))
    if media >=0:
        soma = soma + media
        conta += 1
media_turma = soma / conta
print("A media da turma é: %.2f " % media_turma)
'''

#Exercicios de FOR
#1)
'''
for i in range (10, 151):
    print("%d ao quadrado = %d" % (i, i * i))
'''
#2)
'''
numero = int(input("Digitr um numero: "))
f = 1
#indo de 1 ate numero
for i in range (1, numero+1):
    f = f *i
print("Fatorial de %d: %d " % (numero, f))
f = 1
# indo de numero até 1, decrementando em 1
for i in range (numero,0 ,-1):
    f = f *i
print("Fatorial de %d: %d " % (numero, f))
'''
#3)
'''
numero = int(input("Digite um numero: "))
for i in range (1, 11):
    print("%d X %d = %d" % (numero, i, numero*i))
'''
'''
#4)
numero = int(input("Digite um número: "))
cont = 0
for i in range(2, numero):
    if numero % i == 0:
        cont = cont + 1
        break
if cont == 0:
    print("%d é primo" % numero)
else:
    print("%d não é primo" % numero)
'''






