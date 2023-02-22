# Crie um programa que cadastre informações de várias pessoas (nome, idade e cpf) e depois coloque em um dicionário. 
# Depois remova todas as pessoas menores de 18 anos do dicionário e coloque em outro dicionário


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
       
        resp = str (input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print  ('Erro! Responda apenas S ou N' )
   
    if resp == 'N':
        break

print ('+=' * 30)
print (' TODOS CADASTRADOS')
print ('+=' * 30)
print(pessoas)
for p in pessoas:
    if p ['idade'] <= 18:
        agenda.pop('idade')
        agenda.pop('nome')
        agenda.pop('cpf')
        agenda.pop('telefone')
        print(' +=' * 30)
print ('MAIORES DE 18 ANOS: ')
print(p)

        
   

