'''
args - argumentos não nomeados
* - *args (empacotamento e desempacotamento)

'''
# desempacotamento
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

def soma(*args):
    total = 0
    for i in args:
        total += i
        print(i, total)

soma(1, 2, 3, 4, 5, 6)