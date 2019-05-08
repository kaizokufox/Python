#Operadores Relacionais
'''Em pseudocódigo
  >    maior que      3 > 2   verdadeiro
  <    menor que      3 < 2   falso
  >=   maior ou igual que   5 >= 7   falso
  <=   menor ou igual que   5 <= 7   verdadeiro
  =    igual 4 = 4 verdadeiro
  <>   diferente 4    <> 4 falso

• Em Python
> maior que 3 > 2 verdadeiro
< menor que 3 < 2 falso
>= maior ou igual que 5 >= 7 falso
<= menor ou igual que 5 <= 7 verdadeiro
== igual 4 == 4 verdadeiro
!= diferente 4 != 4 falso'''

#Operadores Lógicos
'''Em pseudocódigo
     não negação
     e conjunção
     ou disjunção
• Em Python
     not negação
     and conjunção
     or disjunção
• Prioridades da esquerda para a direita, de cima para baixo não e ou'''

#Estruturas Condicionais
'''Comando if
Por exemplo, se o valor da média final for maior ou igual a 5, o aluno está aprovado:
se (media >= 5)
então mostrar “APROVADO”

• Por exemplo, se o salário bruto for maior que 1000 e menor que 2500, então
o percentual de desconto do imposto de renda será de 10%:
se ( (SB >= 1000) e (SB<=2500) )
então IR = 10

• Nestas duas situações existe um teste (condição) para que alguma
operação seja executada.

Por exemplo, se o valor da média final for maior ou igual a 5, o aluno está aprovado:

se (media >= 5)
então mostrar “APROVADO”.'''

#Primeiro exemplo estrutura condicional
'''print("Exemplo1")
nota1 = float(input('Entre com a primeira nota: '))
nota2 = float(input('Entre com a segunda nota: '))
media = (nota1 + nota2)/2
if media >= 5 :
    print('Aprovado com média %2.f' % media)
else :
    print('Reprovado com média %.2f' % media)'''

#Se ( (SB >= 1000) e (SB<=2500) )
#então IR = 10

'''print("Exemplo2")
sb = float(input('Entre com o salário base: '))
if sb >= 1000 and sb <=2500 :
    ir = sb * 0.10
print('Imposto de renda a pagar: %.2f' % ir)'''


#se ( (SB >= 1000) e (SB<=2500) )
#então IR = 10
#senão
#se (SB > 2500)
#então IR = 15
#senão
#IR = 0

'''print("Exemplo3")
sb = float(input('Entre com o salário base: '))
if sb >= 1000 and sb <=2500 :
    ir = sb * 0.10
elif sb > 2500 :
     ir = sb * 0.15
elise :
    ir = 0
print('Imposto de renda a pagar: %.2f' % ir)'''


#Estrutura de repetição enquanto - pseu
'''Sintaxe da Estrutura de Repetição enquanto
<inicialização da variável de controle>;
enquanto (<condição>) faça
<comando_1>;
<comando_2>;
...
<comando_n>;
<atualização da variável de controle>;
fimenquanto;'''

#Exemplo While

'''x = 0
while x < 3 :
    print('O valor de x é: %d' % x)
    x = x +1
print('Saiu do while')'''

#Exemplo1 de FOR

'''x = 0
for x in range (3) : #x vai de 0 a 2
    print('O valor de x é: %d' % x)
print ('Saiu do laço')'''

#Exemplo2 FOR
# x vai de 50 99
'''for x in range (50, 100) :
     if x == 88 : 
        break
    # se x for igual a 88 sai do laço
        print(x)
print('Saiu do FOR')'''

#Exemplo3 FOR
total = 0
numero = int(input('Digite um numero: '))
if (numero %2) == 0:
    numero = numero -1
    for i in range(numero,0,-2):
#i vai de numero ate 0, decrementando de 2
        total = total + 1
        print('Valor de i %d: ' % i)
print("A soma dos números impares é %d" % total)





