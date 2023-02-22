
#Escreva um algoritmo que leia um número inteiro entre 100 e 999 e imprima na saída cada um dos algarismos que compõem o número

num =  int ((input("DIGITE UM NUMERO :")))

if num >= 100:
    if num <= 999:
     print ("ANALISANDO O NUMERO..")
     u = num // 1 % 10
     d = num // 10 % 10
     c = num // 100 % 10
     print ('UNIDADE : {}'.format(u))
     print ('DEZENA : {}'.format(d))
     print ('CENTENA : {}'.format(c))
    else :
     print("NUMERO INVALIDO!")
else :
     print("NUMERO INVALIDO!")


#OK