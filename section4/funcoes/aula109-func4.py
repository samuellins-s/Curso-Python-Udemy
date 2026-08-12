'''
Escopo de funções em Python
    Escopo = local onde aquele código pode atingir (ñ afeta o que está fora do escopo)
    O que é definido dentro da função fica "protegido".


'''

def escopo():
    x = 1
    print(x)

# print(x) -> não existe fora da função

escopo()

# CASO 2 (má prática de programação)

y = 2

def escopoy():
    print(y) # se variavel existe antes da chamada de função, funciona

escopoy() # chamada de func