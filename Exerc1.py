'''nome = "Luccas"
idade = 21
altura = 1.75
peso = 80
endereco = "rua luiz nadalin, n76"
print("Nome: " + nome)
print("Idade: ",idade)
print("Altura: ", altura)
print("peso: ", peso)
print("Endereço: " + endereco)'''

# com STR, concatenar
'''nome = "Luccas"
idade = 21
altura = 1.75
peso = 80
endereco = "rua luiz nadalin, n76"
print('Nome:' + nome)
print('Idade: ' + str(idade))
print('Altura' + str(altura))
print('peso: ' + str(peso))
print('Endereço: ' + endereco)'''


# Com Entrada de Dados
print("Exercicio de Entrada de dados")
#RichardCornoMan -> ideia dele de colocar print acima
nome = input ("Digite o seu nome: ")

idade = input ("Digite a sua idade: ")
'''conversao de dados '''
idade = int(idade)

altura = input ("Digite a sua altura: ")
'''conversao de dados ->'''
altura = float (altura)

peso = input ("Digite o seu peso: ")
'''conversao de dados ->'''
peso = float(peso)

endereco = input ("Digite o seu endereço: ")

print("Nome: %s " % nome)
print("Idade: %d anos" % idade)
print("Altura: %.2f" % altura)
print("peso: %.2f" % peso)
print("Endereço: %s " % endereco)

# tipos de dados
'''Int -> %d ou %i
float -> %f
String %s
'''
#Operadores aritméticos auxiliares em python
''' ** potenciação Exemplo -> 2**3 = 8
 math.sqr Radiciação exemplo -> math.sqrt(4) = 2
 % Resto de Divisão Exempl -> 4%3 = 1'''









