
# Q.39 A IMPORTANCIA DE 780.000,00 SERA DIVIDIDA ENTRE TRES GANHADORES DE UM CONCURSO, SENDO A QUANTIA TOTAL:
# O PRIMEIRO GANHADOR RECEBERA 46%
# O SEGUNDO RECEBERA 32%
# O TERCEIRO RECEBERA O RESTANTE 





premio = float =  780.000
print ("**********************************************************")
print (" O PREMIO SERA NO VALOR DE R$ :", premio)
print ("**********************************************************")

primeiroPremio = float
primeiroPremio = premio -  (premio * 46 / 100)
print (' O VALOR DO PRIMEIRO GANHADOR É R$ :',primeiroPremio)
print ("**********************************************************")

segundoPremio = float
segundoPremio = premio -  (premio * 32 / 100)
print (' O VALOR DO SEGUNDO GANHADOR É R$ :',segundoPremio)
print ("**********************************************************")


premioresto  = primeiroPremio + segundoPremio  
terceiroPremio = (premioresto % premio)

print (' O VALOR DO TERCEIRO GANHADOR É R$ :',terceiroPremio)
print ("**********************************************************")



