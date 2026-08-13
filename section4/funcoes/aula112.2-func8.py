'''
args - argumentos não nomeados
* - *args (empacotamento e desempacotamento)

Com o return, podemos colocar a chamada de função em uma variavel


'''

def soma(*args): # empacota
    total = 0
    for i in args:
        total += i
    return total

soma1 = soma(1, 2, 3, 4, 5, 6)
print(soma1)

numeros = 1, 2, 3, 4, 5, 6
soma2 = soma(*numeros) # desempacota
print(soma2)

print(sum(numeros))