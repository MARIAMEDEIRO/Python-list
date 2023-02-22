


# Q.42 RECEBA O SALARIO- BASE DE UM FUNCIONARIO, CALCULE E IMPRIMA O SALARIO A RECEBER, SABENDO -SE QUE ESSE FUNCIONARIO
# TEM UMA GRATIFICAÇÃO DE 5% SOBRE O SALARIO- BASE. ALEM DISSO, ELE PAGA 7% DE IMPOSTO SOBRE O SALARIO-BASE

from ast import If


salarioAreceber = float (input("DIGITE O SEU SALARIO BASE R$: "))
gratificacao = salarioAreceber + (salarioAreceber * 5 /100)
imposto = salarioAreceber - (salarioAreceber * 7 / 100)


print ("SALARIO BASE É IGUAL A R$ : {} ".format(salarioAreceber))
print("SALARIO TOTAL COM GRATIFICAÇÃO R$ : ", format(gratificacao))
print ("SALARIO COM IMPOSTO TOTALIZA EM R$:",format(imposto))




    