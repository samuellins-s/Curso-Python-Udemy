'''
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)

'''

def soma(x, y):
    print(f'{x} + {y} =', x + y)

soma(2, 3)

# argumento nomeado
soma(x=3, y=2)