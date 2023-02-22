# Crie um dicionário que é uma agenda e coloque nele os seguintes dados: chave (cpf), nome, idade, telefone.
# O programa deve ler um número indeterminado de dados, criar a agenda e imprimir todos os itens do dicionário no formato chave: nome-idade-fone
agenda  = dict()
pessoas = list()

while True:
    agenda.clear()
    agenda ['nome'] = str(input('Nome: '))
    agenda ['cpf'] = int (input('Cpf: '))
    agenda ['idade'] = int (input('Idade: '))
    agenda ['telefone'] = int (input('Telefone: '))
    pessoas.append(agenda.copy())
    while True:
        resp = str (input('Quer continuar ? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print  ('Erro! Responda apenas S ou N' )
    if resp == 'N':
        break
print ('+=' * 30)
print(pessoas)


