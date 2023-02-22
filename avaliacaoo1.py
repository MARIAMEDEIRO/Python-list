import os

funcionario = []

def criarConta(nome,cpf,cargo,salario):
    return {'nome':nome,'cpf':cpf,'cargo':cargo,'salario':salario}

def novoCadastro():
    os.system('cls')
    nome = str  (input("Qual seu nome?:"))
    cpf = int (input("Digite seu cpf:"))
    cargo = str (input("Digite seu cargo:"))
    salario = float (input("Digite o salario:"))

    funcionario.append(novoCadastro(nome,cpf,cargo,salario))
    os.system('cls')
    print('a conta foi cadastrada com sucesso')
    os.system('pause')
    os.system('cls')

def menuInicial(funcionario):
    
    while True:
        os.system('cls')
        print ('---MENU INICIAL---')
        print ('1: Cadastrar funcionario')
        print ('2: Encontrar um funcionario')
        print ('3: Cadastrar telefone')
        print ('4: Editar dados do  funcionario')
        print ('5: Deletar funcionario')
        print ('0: Sair')
        opcao = int (input("Qual sua opção?: "))

        if opcao == 0:
            exit()
        elif opcao == 1:
            novoCadastro(funcionario)
        # elif opcao == 2:
            # encontrarContas(funcionario)
            #encontrar conta
        # elif opcao == 3:
            # encontrarContas(funcionario)
        # elif opcao == 4:
            # editarContas(funcionario)
def main():
    
    menuInicial()


main()