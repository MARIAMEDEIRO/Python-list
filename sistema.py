#CONTROLE ACADEMICO

import os

pessoas = []

class Pessoas_fisica:
    def __init__(self, nome:str, data_nascimento:int, cpf:int, aluno:bool):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.aluno = aluno

    def novo_cadastro():
        nome =str (input ("Digite seu nome: "))
        data_nascimento = int (input ("Digite sua data: "))
        cpf = int (input ("Digite seu cpf: "))
        aluno = bool (input ("Voce é aluno? :"))
        pessoa = Pessoas_fisica(nome, data_nascimento, cpf, aluno)
        return pessoa

    def curso(pessoas):
        nome = str (input ("Digite seu nome: "))
        curso = str (input ("Digite seu curso : "))
        inicio  = int (input ("Digite o inicio do curso: "))
        fim  = int (input ("Digite o fim do curso :"))
        duracao  = int (input ("carga horaria do curso :"))
        curso = Pessoas_fisica(nome, curso, inicio, fim, duracao)
        return curso

    def exibirDados(pessoas):
        print('nome: {}\ncpf: {}\ndata_nascimento: {}\naluno: {} \ncurso: {}'.format(
        pessoas[0], pessoas[1], pessoas[2], pessoas[3], " | ".join(pessoas[4])))
        os.system('pause')
         
def menuInicial():

    while True:
        #os.system('cls')
        print('---MENU INICIAL---')
        print('1: Manter aluno')
        print('2: manter curso')
        print('3: manter disciplina')
        print('4: matricular aluno')
        print('5: listar todos os alunos da turma')
        print('0: Sair')
        opcao = int(input("Qual sua opção?: "))

        if opcao == 0:
            exit()

        if opcao == 1:
            pessoas.append(Pessoas_fisica.novo_cadastro())
        if opcao == 3 :
            pessoas.append(Pessoas_fisica.curso())

        if opcao == 5:
            for i in pessoas:
                print ('#----------------> Exibindo Dados < -------------------#')
                print(f"nome: {i.nome}, nascimento: {i.data_nascimento}, cpf: {i.cpf}, Aluno? {i.aluno}, curso: {i.curso}")
               




def main():
    menuInicial()
main()




