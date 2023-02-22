import os
from Funcionario import Funcionario
from Funcao import Funcao
from Database import Database

funcionario = []
telefone = []

database :Database = Database()

def menuInicial():

    

    while True:
        os.system('cls')
        totalFuncao = database.total_funcao()
        print ('---MENU INICIAL---')
        print ('1: Manter funções')
        if totalFuncao>0:
            print ('2: Manter funcionario')
        print ('0: Sair')
        opcao = int (input("Qual sua opção?: "))

        if opcao == 0:
            exit()
        elif opcao == 1:
            menuFuncoes()
        elif opcao == 2 and totalFuncao>0:
            menuFuncionario()



def menuFuncionario():
    
    
    while True:
        totalFuncionario = database.total_funcionario()
        os.system('cls')
        print ('---MENU FUNCIONARIO---')
        print ('1: Cadastrar funcionario')
        if totalFuncionario>0:
            print ('2: Pesquisar um funcionario')
            print ('3: Editar funcionario')
            print ('4: Deletar funcionario')
        print ('0: Voltar')
        opcao = int (input("Qual sua opção?: "))

        if opcao == 0:
            menuInicial()
        elif opcao == 1:
            cadastrarFuncionario()
        elif opcao == 2 and totalFuncionario>0:
            pesquisarFuncionario()
        elif opcao == 3 and totalFuncionario>0:
            atualizarFuncionario()
        elif opcao == 4 and totalFuncionario>0:
            deletarFuncionario()


def pesquisarFuncionario():
    cpf = input("Digite o cpf do funcionario: ")
    result = database.search_funcionario(cpf)
    if result==None:
        print("Funcionario não encontrado!")
        os.system('pause')
        os.system('cls')
        return None
    print(result)
    os.system('pause')
    os.system('cls')
    return Funcionario(funcao=result["funcao"],nome=result["nome"],cpf=result["cpf"],salario=result["salario"],telefone=result["telefone"])


def pesquisarFuncao():
    cod = input("Digite o codigo da função: ")
    result = database.search_funcao(cod)
    if result==None:
        print("Função não encontrada!")
        os.system('pause')
        os.system('cls')
        return None
    print(result)
    os.system('pause')
    os.system('cls')
    return Funcao(cod=result["cod"],nome=result["nome"])


def deletarFuncao():
    cod = input("Digite o codigo da função: ")
    try:
        database.delete_funcao(cod)
    except:
        print("Não foi possivel deletar a função, existe funcionarios associados a essa função!")
    os.system('pause')
    os.system('cls')

def deletarFuncionario():
    cpf = input("Digite o cpf do funcionario: ")
    database.delete_funcionario(cpf)
    print("Funcionario deletado")
    os.system('pause')
    os.system('cls')

def cadastrarFuncao():
    nome = input("Digite o nome da função: ")
    cod = input("Digite o codigo da função: ")
    database.add_funcao(Funcao(cod=cod,nome=nome))


def cadastrarFuncionario():
    nome = input("Digite o nome: ")
    cpf = input("Digite o cpf: ")
    cod = int(input("Digite o codigo da função: "))
    salario = float(input("Digite o salario: "))
    telefone = input("Digite o telefone: ")
    resultFuncao = database.search_funcao(cod)
    if(resultFuncao==None):
        print("Função não encontrada!")
        os.system('pause')
        os.system('cls')
        return
    
    funcao = Funcao(cod=resultFuncao["cod"],nome=resultFuncao["nome"])
    database.add_funcionario(Funcionario(nome=nome,cpf=cpf,funcao=funcao,salario=salario,telefone=telefone))



def atualizarFuncionario():
    funcionario =  pesquisarFuncionario()
    if funcionario==None:
        return
    funcionario.nome = input("Digite o nome: ")
    cod = int(input("Digite o codigo da função: "))
    funcionario.salario = float(input("Digite o salario: "))
    funcionario.telefone = input("Digite o telefone: ")
    resultFuncao = database.search_funcao(cod)
    if(resultFuncao==None):
        print("Função não encontrada!")
        os.system('pause')
        os.system('cls')
        return
    
    funcionario.funcao = Funcao(cod=resultFuncao["cod"],nome=resultFuncao["nome"])
    database.update_funcionario(funcionario)
    print("Dados atualizados!")
    os.system('pause')
    os.system('cls')


def atualizarFuncao():
    funcao = pesquisarFuncao()
    if funcao == None:
        return
    funcao.nome = input("Digite o nome: ")
    database.update_funcao(funcao)
    print("Dados atualizados!")
    os.system('pause')
    os.system('cls')




def menuFuncoes():
    while True:
        totalFuncao = database.total_funcao()
        os.system('cls')
        print ('---MENU FUNÇÕES---')
        print ('1: Cadastrar função')
        if totalFuncao>0:
            print ('2: Pesquisar função')
            print ('3: Editar função')
            print ('4: Deletar função')
        print ('0: Voltar')
        opcao = int (input("Qual sua opção?: "))

        if opcao == 0:
           menuInicial()
        elif opcao == 1:
            cadastrarFuncao()
        elif opcao == 2 and totalFuncao>0:
            pesquisarFuncao()
        elif opcao == 3 and totalFuncao>0:
            atualizarFuncao()
        elif opcao == 4 and totalFuncao>0:
            deletarFuncao()

def main():
    database.connect()
    menuInicial()
main()
