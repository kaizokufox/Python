#1)
'''
dolar = 4.09
n = float(input("Digite um valor em Dolar: "))
n = n * dolar
print("Valor do Dolar em reais é: %.2f" % n)
'''

#2)
'''
tempo = input("Digite um horario em horas, minutos e segundos: ")
vetor = tempo.split(":")
soma = 0
soma = soma + int(vetor[0]) * 3600
soma = soma + int(vetor[1]) * 60
soma = soma + int(vetor[2])

print("horario convertido em segundos: ", soma)
'''

#3)
'''
comprimento = int(input("Digite o Comprimento do Retângulo: "))
largura = int(input("Digite a Largura do Retângulo: "))
area = 0
perimetro = 0
area = comprimento * largura
perimetro = 2 * (comprimento + 2 * largura)
print("Calculo da area", area ," Perimetro", perimetro)
'''

#4)
'''
hp = float(input("Digite a altura da parede: "))
lp = float(input("Digite a largura da parede: "))
ha = float(input("Digite a altura da azulejo: "))
la = float(input("Digite a largura da azulejo: "))
area = 0
soma = 0
areap = hp * lp
areaa = ha * la
soma = areap / areaa
print("Quantidade de azulejo necessario é: %.2f" % soma)
'''

#5)
'''
areatotal = int(input("Digite a area total do terreno: "))
areacon = int(input("Digite a area construida do terreno: "))
m2ncons = 0
m2ncons = areatotal - areacon
impotsnao = m2ncons * 3.80
impost = areacon * 5

print("Valor total do Imposto a ser pago: ", impotsnao + impost)
'''

#6)
'''
ht = float(input("Digite quantidade de horas trabalhas: "))
rh = float(input("Digite o valor por horas trabalhas: "))
valor = 0
valor = rh * ht
print("Valor a receber: %.2f" % valor)
'''

#7
'''
cv = float(input("Digite o valor de pontecia em CV : "))
kw = float(input("Digite o valor de pontecia em KW : "))
soma1 = 0
soma2 = 0
soma1 = cv / 1.36
soma2 = kw * 1.36
print("Valor do CV equivalente em KW: %.3f" % soma1)
print("Valor do KW equivalente em CV: %.3f" % soma2)
'''

#8) 
'''
f = float(input("Digite a temperatura em ºF: "))
c = 0
c = ((f - 32)*5) / 9
print("A temperatura em ºC é: %.2f" % c)
'''

#9)
'''
n = 10
print("Numero interito compreendidos entre 10 a 150: ")
while n < 151:
    print("Numeros", n, "inteiros")
    n = n +1
'''

#10)

'''
n = int(input("Digite um numero inteiro para o calcular Fatorial: "))
cont = 2
f = 1
while cont <= n:# se "CONT" for menor ou igual a "N" entra no laço, senão pega o numero do "F"
    f = f * cont
    cont = cont + 1
print("valor do Fatorial %d! é: " %n, f)
''' 

#11)
'''
n = int(input("Digite um numero inteiro: "))
cont = 0
for i in range(2, n):
    if n % i ==0 :
        cont = cont + 1
        break
if cont == 0 :
    print("O numero %d é primo" % n)
else :
    print("O numero %d não é primo" % n)
'''

#12)
'''
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
cont = 0
v = []
for n1 in range(n2):
    if n2 % (n1+1):
        cont = cont +1
        v.append(n1+1)
    else:
        cont
if cont == 2:
        print("São divido por: ", v)
else:
    print("São divido por:", v)
'''

#13)
'''
cont = 0
soma = 0
media = 0
for i in range(1, 30):
   n = int(input("Digite 30 numeros: "))
   if n > 0:
        soma = soma + n
        cont +=1
media = soma / cont
print("A somatoria é: %.2f" % soma)
print("A media é: %.2f" % media)
'''
#14)
'''
v=[]
while len(v) < 10:
    n = int(input("Digite dez numeros inteiros: "))
    v.append(n)
print("o maior numeor é: ", max(v))
'''

















