#Q.43 ESCREVA UM PROGRAMA DE AJUDA PARA VENDEDORES. A PARTIR DE UM VALOR LIDO, MOSTRE:
# O TOTAL A PAGAR COM DESCONTO DE 10%
# O VALOR DE CADA PARCELA, NO PARCELAMENTO DE 3X SEM JUROS.
# A COMISSÃO DO VENDEDOR, NO CASO DA VENDA SER A VISTA 5% SOBRE O VALOR COM DESCONTO
# A COMISSÃO DO VENDEDOR, NO CASO DA VENDA SER PARCELADA 5% SOBRE O VALOR TOTAL

from xmlrpc.client import boolean


nome = input('QUAL NOME DA VENDEDOR(A)? ')
print(f'VENDEDORA ATUAL:  {nome}, VAMOS CONTINUAR A VENDA..')
parcelar = int 
valorProduto = int (input("DIGITE O VALOR TOTAL DA VENDA R$: "))
print (" O VALOR DO PRODUTO É : ", format(valorProduto))
print ("**********************************************************")

print ("> 1 SE FOR AVISTA")
print ("> 2 SE FOR CARTAO")
print ("> 3 SE FOR PIX")
print ("> 4 SE FOR APRAZO")
formaDePagamento = int  (input("DIGITE UM NUMERO PARA FORMA DE PAGAMENTO : "))

if formaDePagamento % 2 == 0 :
    print ("DESEJA PARCELAR?  : ")
    print (" DIGITE (1) SIM OU (2) NAO: ", parcelar )   
    if parcelar % 2 == 0:
        
       comisaoDesconto = int - (valorProduto * 5 / 100)
else:  
    desconto = valorProduto - (valorProduto * 10 / 100)
    print ("COMPRA A VISTA! DESCONTO DE 5%, PORTANTO O VALOR TOTAL R$: {} ".format(desconto))



    # INCOMPLETA
 




