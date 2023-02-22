

def menu ():
    print ('-=' * 50)
    print ("ESCOLHA UMA OPÇÃO:")
    print ("1. Nova conta:")
    print ("2. Logar:")
    print ('-=' * 50)
    a = int (input ("="))
    if a == 2:
        print ("login...")
    else:
        print ("Tela de cadastro...")
    return (a)
def submenu ():
    print ("Remover conta")
    print ("Transferir")
    print ("Saldo em conta")
    print ("Deposito")

submenu (menu())
# def NovaConta (novo):
    
    # numero = int (input ("Digite o numero: "))
    # titular = str (input ("Digite seu Nome: "))
    # saldo = float (input ("Digite o saldo: "))
   

# def Logar (cadastro):









