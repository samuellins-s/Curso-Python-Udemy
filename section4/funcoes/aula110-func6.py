'''
Retorno de valores das funções pelo return
    return só pode ser utilizado dentro da função
    return termina a execução da função

'''

def soma(x, y):
    if x > 10:
        return 10

    return x + y # agora poderá ser atribuído a uma variável.
    print('sou inalcansável......')

soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1 + soma2)