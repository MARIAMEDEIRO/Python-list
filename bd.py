import mysql.connector
from mysql.connector import Error
#inserindo registros 

print ("Cadastro de cliente em conta corrente")
print("Entre com os dados solicitados")

idclient = input ("Id do cliente :")
titular = input ("Nome do titular: ")
cpfcli = input ("Cpf : ")
numerocon = input ("Numero da conta :")
taxacon = input ("Taxa :")

dados = idclient + ',' + titular + ',' + cpfcli  + ',' + numerocon + ',' + taxacon + ')'

dados_bd = """ INSERT INTO tbl_clientes
(id_clientes, nome_titular, cpf, numero_conta, taxa)
VALUES( """

sql = dados_bd + dados
print(sql)

try:
    con = mysql.connector.connect(host='localhost',port=3307, database='banco_poo', user='root', password='13@84mA.')
    inserir_clientes = sql
    cursor = con.cursor()
    cursor.execute(inserir_clientes)
    con.commit()
    print (cursor.rowcount, "registros inseridos na tabela")
    cursor.close

except Error as error:
    print ("erro ao inserir dados na tabela")
    print(error)
