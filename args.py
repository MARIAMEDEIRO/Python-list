def soma(*args):
    print(args)
soma (1,2,3,4,5,6,7,7,8,9)


def somar (*args):
    soma = 0
    for i in args:
        soma +=i
    return soma

somar (1,2,3,4,5,6,7,7,8,9)
