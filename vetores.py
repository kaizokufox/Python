'''x = []
for y in range(5):
    print(y)
    x.append(int(input("Digite o " + str(y+1) + "ª numero: ")))
print(x) #mostrando os valores da lista
'''

'''x = [0,0,0,0,0]
for y in range(5):
    print(y)
    x[y] = int(input("Digite o " + str(y+1) + "ª número: "))
print(x) #mostrando os valores da lista
'''
'''
continua = 's'
lista = []
while (continua == 's' or continua == 'S'):
    n = int(input("Digite um numero: "))
    lista.append(n) #inserindo no vetor
    continua = input("Deseja continuar? (s/n): ")
print(lista)
for i in range(len(lista)):
    lista[i] = lista[i] + 1 # soma 1 ao elemento
print(lista)
'''
'''
num_alunos = 5
nomes = []
notas = []
media = 0 # = zero
for i in range(num_alunos):
    nomes.append(input("Informe o nome do aluno: "))
    notas.append(float(input("Informe a nota de " + nomes[i] + ":")))
    media = media + notas[i]
media = media / num_alunos
print("A media da turma é ", media)
for i in range (num_alunos):
    if notas[i] > media:
        print("Parabens", nomes[i])
'''

#1)Fazer um programa que armazena 10 números inteiros e soma os pares, mostrando
#o resultado em seguida
'''cont = 10
num1 = []
soma = 0
for i in range(cont):
    num1.append(int(input("Informe o numero: ")))
    if num1[i] % 2 == 0:
        soma = soma + num1[i]
print("A soma dos pares é", soma)
'''
    
#2) Fazer um programa que recebe os nomes de 5 pessoas com suas respectivas idades e mostra qual a
#pessoa mais velha.
nome_idade = 2
nomes = []
idade = []
ind = 0
for i in range(nome_idade):
    nomes.append(input("Informe seu nome: "))
    idade.append(float(input("Informe sua idade: ")))
for i in range(nome_idade):
    if idade[i] > idade[ind]:
        ind = idade[i]
print(ind)




                

