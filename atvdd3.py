
#Faça um Programa que leia 4 notas, adicione em uma lista e mostre as notas e a média na tela.

a = list()

nota1 = float (input('DIGITE A PRIMEIRA NOTA :'))
nota2 = float (input('DIGITE A SEGUNDA NOTA :'))
nota3 = float (input('DIGITE A TERCEIRA NOTA :'))
nota4 = float (input('DIGITE A QUARTA NOTA :'))

b = nota1+ nota2+nota3+nota4
media =  b / 4

a.append([[nota1,nota2,nota3,nota4],media])

print ('='*30)
print (' O SOMATORIO DAS NOTAS  É : {}'.format(b))
print ('='*30)
print (' A MEDIA É : {}'.format(media))
print ('='*30)

#OK
