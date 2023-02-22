
# Q.38 LEIA O SALARIO DE UM FUNCIONARIO. CALCULE E IMPRIMA O VALOR DO NOVO SALARIO, SABENDO SABENDO QUE ELE RECEBEU UM AUMEBTO DE 25%

print ("**********************************************************")
salario  = float (input ('DIGITE O VALOR DO SALARIO DO FUNCIONARIO  R$: '))

novoSalario = salario + (salario * 25 / 100)
print ("**********************************************************")
print (' O SALARIO ATUAL É  R${} , ACRESCENTANDO 25%  FICARA R${}' .format(salario, novoSalario))
print ("**********************************************************")

