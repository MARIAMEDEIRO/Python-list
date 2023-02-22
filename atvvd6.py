

#Escreva um programa que leia 5 números e escreva o menor valor lido e o maior valor lido.


a = 0
quant = 10
num = []
while a < quant:
   val = int(input("DIGITE UM VALOR\n"))
   a = a + 1
   num.append(val)
else:
   print("MENOR NUMERO:", (min(num)))
   print("MAIOR NUMERO:", (max(num)))

   #OK