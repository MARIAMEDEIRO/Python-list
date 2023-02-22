from Funcao import Funcao


class Funcionario():

    def __init__(self,nome, cpf,funcao: Funcao,salario,telefone):
        self.nome = nome
        self.cpf = cpf
        self.funcao = funcao
        self.salario = salario
        self.telefone = telefone

