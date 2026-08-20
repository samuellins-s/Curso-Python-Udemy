'''
Exercicios com funções:

Crie uma função que multiplica todos os argumentos não nomeados recebidos.

Retorne o valor para uma variável e mostre o valor da variavel.

Crie uma função que fala se um numero é par ou impar.
    Retorne se o número e par o ímpar.

'''

def multiplicar_valores(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

resultado_multiplicacao = multiplicar_valores(1, 2, 3, 4, 5, 6)
print(resultado_multiplicacao)

def par_ou_impar(numero):
    numero = int(numero)

    if numero % 2 == 0:
        return (f'O numero {numero} é par.')
    else: 
        return (f'O numero {numero} é ímpar.')

print(par_ou_impar(2))