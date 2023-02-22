
def receba_notas ():
    notas1 = float ((input ("DIGITE A 1 NOTA :")))
    notas2 = float ((input("DIGITE A 2 NOTA :")))
  
    return  (notas1,notas2)
    

def calcula_media(notas1,notas2):
      media = (notas1 + notas2) /2

def verificar_aprovacao(media):
    if media >= 7:
        print ("aprovado!")
    else :
        print("reprovado!")


verificar_aprovacao(receba_notas())
