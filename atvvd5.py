
#Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior que 20% do salário imprima: Empréstimo não concedido, caso contrário imprima: Empréstimo concedido.


salario = int (input("DIGITE O SALARIO: "))
emprestimo = int (input("DIGITE O VALOR DO EMPRESTIMO: "))

consignado = salario - (salario * 20) / 100
print (" O VALOR DE EMPRESTIMOS QUE VC PODE FAZER É ATE :", consignado)

if consignado >= emprestimo:
    print ("EMPRESTIMO CONSIGNADO")
if consignado < emprestimo:
    print ("NÃO CONSIGNADO")