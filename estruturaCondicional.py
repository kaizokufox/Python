#primeiro exemplo Estrutura condicional
'''
nota1 = float(input("Entre com a primeira nota: "))
nota2 = float(input("Entre com a segunda nota: "))
media = (nota1 + nota2)/2
if media >= 5 :
    print("Aprovado com a media %2.f" % media)
else:
    print("Reprovado com a media %2.f" % media)
'''

'''
#Segundo exemplo Estrutura condicional
#if (SB >= 1000) and (SB <= 2500)). salario for maior que 1000 e menor que 2500 o percentual
de 10%
# ir = 10

sb = float (input("Entre com o salário base: "))
if sb >= 1000 and sb <=2500 :
    ir = sb *0.10
    print("Imposto de renda a pagar: %.2f" % ir)
'''
'''
#Terceiro exemplo Estrutura condicional 
# se (SB >= 1000) e (SB <= 2500))
#então IR = 10
#senão
#   se(SB > 2500)
#   então IR = 15
#   senão IR = 0

sb = float (input("Entre com o salário base: "))
if sb >= 1000 and sb <= 2500:
    ir = sb * 0.10
elif sb > 2500 :
        ir = sb * 0.15
else :
   ir = 0
print("Imposto de renda a pagar: %2.f" % ir)
'''
'''
#Fazer um programa que recebe duas notas do
#aluno, calcula a média aritmética e mostra sua
#média e situação.

nota1 = float(input("Entre com a primeira nota: "))
nota2 = float (input("Entre com a segunda nota: "))
media = (nota1 + nota2)/2
if media >= 5 :
    print("Aprovado")
elif media > 3 and media <= 5:
    print("Exame")
else :
        print("Reprovado")
'''














