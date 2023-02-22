
#Faça um Programa que receba uma lista de 10 números reais e mostre-os na ordem inversa.

list = [9,8,7,8,5,3,2]

#POSIÇÃO DA LISTA
n = len(list)


print ('+'*30)
print (list)
print ('+'*30)

#REVERTENDO OS VALORES
for i in range (n-1,-1,-1):
   print ('list [{}] = {} '.format(i,list[i]))


#ok