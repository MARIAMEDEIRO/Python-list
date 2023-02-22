#Considere um sistema onde os dados são armazenados em dicionários. Nesse sistema existe um dicionario principal e o dicionário de backup. 
#Cada vez que o dicionário principal atinge tamanho 5, ele imprime os dados na tela e apaga o seu conteúdo. Crie um programa que insira dados 
#em um dicionário, realizando o backup a cada dado e excluindo os dados do dicionário principal
#quando ele atingir tamanho 5

# agenda = principal e pessoas = backup


agenda = dict()
backup = dict()
indiceBkp = 1
indiceAgd = 1




while True:
    pessoa  = dict()
    pessoa ['nome'] = str(input('Nome: '))
    pessoa ['cpf'] = int (input('Cpf: '))
    pessoa ['idade'] = int (input('Idade: '))
    pessoa ['telefone'] = int (input('Telefone: '))

    #a agenda na chave (indiceAgd) recebe o dicionario com a pessoa
    agenda[indiceAgd] = pessoa
    #incrementa o indice da agenda que tá servindo como chave
    indiceAgd = indiceAgd+1

    # se o indice da agenda for maior que 5, faz o backup
    if(indiceAgd>5):
        print(agenda)
        #percorre todos ou valores da agenda
        for value in agenda.values():
            #adiciona na chave (indiceBkp) o valor contido na agenda fazendo o backup
            backup[indiceBkp] = value
            #incrementa o indice do backup que tá servindo como chave
            indiceBkp = indiceBkp + 1
        agenda.clear() #limpa todos os valores da agenda
        indiceAgd = 1 # reseta o indice para ser incrementado novamente

    while True:
       
        resp = str (input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print  ('Erro! Responda apenas S ou N' )
   
    if resp == 'N':
        break
print(agenda)
print(backup)




#dict_items([('nome', ), ('cpf', ), ('idade', ), ('telefone', )])

            


    

