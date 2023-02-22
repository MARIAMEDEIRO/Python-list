
taxap = 10.0

class Cliente:
    def __init__(self, nome:str, cpf:int, num_conta:int, taxa:float ):
        self.nome = nome
        self.cpf = cpf 
        self.num_conta = num_conta 
        self.taxa_padrao = taxap * taxa
        
    def mostrar_dados(self):
        print(self.nome)
        print(self.cpf)
        print(self.num_conta)

class Conta_corrente(Cliente):
    def __init__(self, nome, cpf, num_conta):
        super().__init__(nome, cpf, num_conta,5)
    def n (self):
        j =  taxap * 5
        print(j)
       

class Conta_poupanca(Cliente):
    def __init__(self, nome, cpf, num_conta):
        super().__init__(nome, cpf, num_conta,1.25)
    def m (self):
        t = taxap * 1.25
        print(t)


c1 = Conta_corrente("maria","21212","123456")
c2 = Conta_poupanca("maria","21212","123456")
c1.mostrar_dados()
c1.n()
c2.m()
