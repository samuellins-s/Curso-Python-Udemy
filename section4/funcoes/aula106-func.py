'''
Introdução às funções (def)
Funções são trechos de código usados para replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) e retornar um valor específico.
Por padrão, funções Python retornam None (nada)

'''

def Printar():
    print('Python')

Printar() # chamada da função

def imprimir(a, b, c): # a, b e c são parâmetros (variáveis a serem definidas)
    print(a, b, c)

imprimir(1, 2, 3) # argumentos (valor da variável)
imprimir(4, 5, 6)

def saudacao(nome='Marian'): # se não houver argumento na chamada de função, será preechido por Marian
    print(f'Olá, {nome}!')

saudacao('Samuel')
saudacao()