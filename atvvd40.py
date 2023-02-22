# UMA EMPRESA CONTRATA UM ENCANADOR A R$ 30,00 POR DIA, FAÇA UM PROGRAMA QUE SOLICITE O NUMERO DE DIAS 
# TRABALHADOS PELO ENCANADOR E IMPRIMA A QUANTIA LIQUIDA QUE DEVERA SER PAGA, SABENDO -SE QUE SÃO 8% PARA IMPOSTO DE RENDA

diaTrabalhado = int (input('DIGITE O TOTAL DE DIAS TRABALHADOS :'))
diaria = 30
valorTotalDias = (diaTrabalhado * diaria)
imposto = valorTotalDias - (valorTotalDias * 8 / 100)
print (" TOTAL DE DIAS TRABALHADOS É DE {0}, O VALOR DE DIARIAS  É DE R$ {1}, O VALOR LIQUIDO É R$ {2}".format(diaTrabalhado, valorTotalDias, imposto))






