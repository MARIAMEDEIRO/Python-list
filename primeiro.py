import os

contas = []


def criarConta(numero_conta,titular,saldo):
    return {'numero':numero_conta,'titular':titular,'saldo':saldo}

def novoCadastro():
    os.system('cls')
    numero_conta = int (input("Numero da Conta:"))
    titular = str (input("Digite seu nome:"))
    saldo = float (input("Digite o saldo:"))

    contas.append(criarConta(numero_conta,titular,saldo))
    os.system('cls')
    print('a conta foi cadastrada com sucesso')
    os.system('pause')
    os.system('cls')


def removerConta(conta):
    contas.remove(conta)
    print('a conta foi removida com sucesso')
    os.system('pause')
    os.system('cls')
    menuInicial()

def encontrarContas():
    numero_conta = int (input("Digite o numero da conta:"))
    for conta in contas:
        if conta['numero'] == numero_conta:
            print('a conta foi encontrada')
            os.system('pause')
            os.system('cls')
            return menuConta(conta)

    print('a conta não foi encontrada')



def buscarConta():
    numero_conta = int (input("Digite o numero da conta:"))
    for conta in contas:
        if conta['numero'] == numero_conta:
            print('a conta foi encontrada')
            os.system('pause')
            os.system('cls')
            return conta
    print('a conta não foi encontrada')
    return None
    

def realizarTranferencia(conta):
    print ('Saldo: R${}'.format(conta['saldo']))
    print('Para realizar uma transferencia, primero')
    contaTransferencia = buscarConta()
    if(contaTransferencia == None):
        print('Não é possivel tranferir')
        return
    
    valor = int (input("Valor que deseja tranferir? :"))

    if(valor>conta['saldo'] or valor <= 0 or conta['numero']==contaTransferencia['numero']):
        print('Não é possivel tranferir')
        return

    index = contas.index(conta)
    conta['saldo'] = conta['saldo'] - valor
    contas[index] = conta


    index = contas.index(contaTransferencia)
    contaTransferencia['saldo'] = contaTransferencia['saldo'] + valor
    contas[index] = contaTransferencia
    
    print('Transferencia realizada com sucesso')
    os.system('pause')
    os.system('cls')
    menuConta(conta)


def exibirSaldo(conta):
    print ('Saldo: R${}'.format(conta['saldo']))
    os.system('pause')
    os.system('cls')


def depositar(conta):
    os.system('cls')
    index = contas.index(conta)
    valor = float(input("Digite o valor que deseja depositar:"))
    conta['saldo'] = conta['saldo'] + valor
    contas[index] = conta
    print('Deposito realizado com sucesso')
    print ('Saldo: R${}'.format(conta['saldo']))
    os.system('pause')
    os.system('cls')
    menuConta(conta)




def menuInicial():

    while True:
        os.system('cls')
        print ('---MENU INICIAL---')
        print ('1: Cadastrar Nova Conta')
        print ('2: Encontrar uma conta')
        print ('0: Sair')
        opcao = int (input("Qual sua opção?: "))

        if opcao == 0:
            exit()
        elif opcao == 1:
            novoCadastro()
        elif opcao == 2:
            encontrarContas()
            #encontrar conta


def menuConta(conta):

    while True:
        os.system('cls')
        print ('---CONTA {}---'.format(conta['numero']))
        print ('1: Remover conta')
        print ('2: Realizar tranferência')
        print ('3: Exibir saldo')
        print ('4: Depositar valor')
        print ('0: Sair')
        opcao = int (input("Qual sua opção?: "))

        if opcao == 0:
            menuInicial()
        elif opcao == 1:
            removerConta(conta)
        elif opcao == 2:
            realizarTranferencia(conta)
        elif opcao == 3:
            exibirSaldo(conta)
        elif opcao == 4:
            return depositar(conta)






def main():
    
    menuInicial()




main()
    
    