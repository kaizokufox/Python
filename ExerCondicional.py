'''
#1)
num1 = int(input("Entre com o primeiro numero: "))
num2 = int(input("Entre com o segundo numero: "))
if num2 > num1:
    print(num1, num2)
else :
    print(num2, num1)
'''
'''
#2)
num = int(input("Entre com o numero:"))
if num % 2 == 0:
    print("Numero é Par: " + str (num))
else:
    print("Numero é Impar: " + str (num))
'''
'''
#3)
altura = float(input("Entra com a sua Altura: "))
sexo = input("Qual o sexo, F = Feminino e M = Masculino: ")

if sexo == 'f':
    resultado = (62.1*altura)-44.7
    print("Resultado: %.2f" % resultado)
elif sexo == 'm':
    resultado = (72.7*altura)-58
    print("Resultado: %.2f" % resultado)
'''
#4)
idade = int(input("Entra com a Idade: "))
if idade < 16:
    print("Não pode votar e nem dirigir")
elif idade >= 16 and idade < 18:
    print("Pode votar mas não dirigir")
elif idade >=18 :
    print("Pode votar e dirigir")


